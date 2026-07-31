import os
import joblib
import openrouteservice
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import pandas as pd
import logging
import time

load_dotenv()


logging.basicConfig(level=logging.DEBUG)

model_path = "crime_model.pkl"
model = None
if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully")
    except Exception as e:
        print("Model loading failed:", e)
        model = None



crime_data_path = "crime_data.csv"
df = pd.read_csv(crime_data_path) if os.path.exists(crime_data_path) else None


ORS_API_KEY = os.getenv("OPENROUTESERVICE_API_KEY")
if not ORS_API_KEY:
    raise ValueError("❌ Missing OpenRouteService API Key in .env file")


app = Flask(__name__)
CORS(app)


client = openrouteservice.Client(key=ORS_API_KEY)

def get_coordinates(location, retries=3, delay=2):
    """Fetch [lon, lat] for a place name using Nominatim."""
    if isinstance(location, list) and len(location) == 2:
        return location

    url = "https://nominatim.openstreetmap.org/search"
    params = {"format": "json", "q": location}
    headers = {"User-Agent": "SafeRouteApp/1.0 (contact@gayatriadatiya.dev)"}

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data:
                    lon, lat = float(data[0]["lon"]), float(data[0]["lat"])
                    logging.debug(f"✅ Coordinates for '{location}': {[lon, lat]}")
                    return [lon, lat]
                else:
                    logging.warning(f"⚠ No results for location: '{location}'")
            else:
                logging.warning(f"⚠ Status {response.status_code} for location: '{location}'")
        except requests.RequestException as e:
            logging.error(f"❌ Request error for '{location}': {e}")
        time.sleep(delay)

    logging.error(f"❌ Failed to get coordinates after {retries} retries: '{location}'")
    return None

@app.route("/")
def home():
    return "🚀 Welcome to the Safe Route Recommendation API!"

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"message": "✅ API is working!"})

@app.route("/recommend_route", methods=["POST"])
def recommend_route():
    data = request.get_json()
    logging.debug(f"🔍 Incoming request: {data}")

    if not data or "start" not in data or "end" not in data:
        return jsonify({"error": "❌ Missing 'start' or 'end' fields"}), 400

    try:
        start = data["start"]
        end = data["end"]
        logging.debug(f"📨 Requested locations: start='{start}', end='{end}'")

        start_coords = get_coordinates(start)
        end_coords = get_coordinates(end)
        mode = data.get("mode", "driving-car")

        if not start_coords or not end_coords:
            return jsonify({
                "error": "❌ Could not get coordinates for locations",
                "details": {
                    "start": start,
                    "start_coords": start_coords,
                    "end": end,
                    "end_coords": end_coords
                }
            }), 400

        logging.debug(f"📍 Coordinates resolved: Start={start_coords}, End={end_coords}, Mode={mode}")

        directions = client.directions(
            coordinates=[start_coords, end_coords],
            profile=mode,
            format="geojson"
        )

        if "features" not in directions or not directions["features"]:
            return jsonify({"error": "⚠ No route found"}), 404

        routes = []
        for route in directions["features"]:
            coords = route["geometry"]["coordinates"]
            travel_time = route["properties"]["segments"][0]["duration"]  # seconds

           
            route_risk  = calculate_risk_score(coords)

          
            normalized_time = travel_time / 60

            
            final_score = (0.9 * route_risk) + (0.1 * normalized_time)

            routes.append({
                "geometry": route["geometry"],
                "duration": travel_time,
                "route_risk": round(route_risk, 2),
                "final_score": round(final_score, 2)
            })

       
        routes.sort(key=lambda r: r["route_risk"])

        return jsonify({"routes": routes})

    except openrouteservice.exceptions.ApiError as e:
        logging.error("🛑 ORS API Error", exc_info=True)
        return jsonify({"error": f"ORS API error: {str(e)}"}), 500
    except Exception as e:
        logging.error("⚠ Unexpected error", exc_info=True)
        return jsonify({"error": f"Internal error: {str(e)}"}), 500

def calculate_risk_score(route_coords):
    """Calculate route risk score (0–10) based on nearby crime density."""
    if not route_coords or df is None:
        return 0

    try:
        longitudes, latitudes = zip(*route_coords)

        
        nearby_crimes = df[
            (df["latitude"].between(min(latitudes) - 0.02, max(latitudes) + 0.02)) &
            (df["longitude"].between(min(longitudes) - 0.02, max(longitudes) + 0.02))
        ]

        if nearby_crimes.empty:
            return 0

        total_risk = nearby_crimes["crime_per_area"].sum()
        raw_score = total_risk / len(route_coords)

        
        max_risk_score = 20  
        scaled_score = min((raw_score / max_risk_score) * 10, 10)

        return scaled_score

    except Exception as e:
        logging.error(f"⚠ Error calculating risk score: {str(e)}")
        return 0

if __name__ == "__main__":
    logging.info("🚀 Starting Flask backend...")
    app.run(debug=True)

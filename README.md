# 🚦 ChaloSafe – Safe Route Recommendation System

ChaloSafe is a web-based Safe Route Recommendation System that helps users estimate the relative safety of a travel route by combining crime data with route planning.

Unlike traditional navigation systems that primarily optimize travel time or distance, ChaloSafe considers nearby crime density to provide a route risk estimate, enabling users to make more informed travel decisions.

This project was developed using **Python (Flask)** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

## 📌 Problem Statement

Navigation applications usually recommend the fastest or shortest path without considering public safety.

ChaloSafe addresses this problem by estimating the risk associated with a route using nearby crime statistics. The application calculates a Route Risk Score based on crime density around the generated path and presents the safest available route to the user.

---

## ✨ Features

- User Sign Up and Sign In (Browser Local Storage)
- Search routes between any two locations
- Supports multiple travel modes
  - 🚗 Driving
  - 🚶 Walking
  - 🚴 Cycling
- Convert location names into coordinates using Nominatim
- Generate routes using OpenRouteService
- Interactive map visualization using Leaflet.js
- Route Risk estimation using nearby crime statistics
- Displays:
  - Travel Time
  - Route Risk Score
  - Risk Level (Low / Medium / High)

---

## 🛠 Tech Stack

### Backend

- Python
- Flask
- Flask-CORS
- Pandas
- Requests
- Joblib
- python-dotenv
- OpenRouteService Python SDK

### Frontend

- HTML5
- CSS3
- JavaScript
- Leaflet.js
- OpenStreetMap

### APIs

- Nominatim Geocoding API
- OpenRouteService Directions API

---

## 📂 Project Structure

```
ChaloSafe/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets/
│
├── app.py
├── crime_data.csv
├── crime_model.pkl
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### Step 1

The user signs in and enters:

- Current Location
- Destination
- Travel Mode

---

### Step 2

The backend converts the entered place names into latitude and longitude using the **Nominatim Geocoding API**.

---

### Step 3

The coordinates are sent to the **OpenRouteService Directions API**, which generates the travel route and estimates the travel duration.

---

### Step 4

The generated route consists of multiple coordinate points.

The backend checks the crime dataset for locations lying close to the generated route.

---

### Step 5

Nearby crime density (`crime_per_area`) is aggregated and normalized to calculate a **Route Risk Score**.

Risk Classification:

| Route Risk | Level |
|------------|-------|
| 0 – 4 | 🟢 Low Risk |
| 4 – 7 | 🟡 Medium Risk |
| 7 – 10 | 🔴 High Risk |

---

### Step 6

The frontend displays:

- Recommended Route
- Interactive Map
- Estimated Travel Time
- Route Risk Score
- Risk Level

---

## 🧠 Algorithms Used

### 1. Geocoding

**Nominatim OpenStreetMap API**

Converts user-entered place names into latitude and longitude coordinates.

---

### 2. Route Generation

**OpenRouteService Directions API**

Generates the travel route based on:

- Source
- Destination
- Travel Mode

---

### 3. Route Risk Calculation

For every generated route:

1. Extract all route coordinates.
2. Search nearby crime locations within approximately ±0.02° latitude and longitude.
3. Sum nearby `crime_per_area` values.
4. Normalize the value to a score between **0–10**.
5. Display the calculated Route Risk Score.

---

### 4. Route Ranking

Routes are sorted according to their calculated risk score.

Routes with lower risk values are considered safer.

---

## 🤖 Machine Learning

The project also includes a **Random Forest Classifier** trained using:

- Latitude
- Longitude
- Crime Per Area

The model (`crime_model.pkl`) classifies crime-risk levels.

> **Note:** The trained model is included as part of the project. In the current implementation, route recommendation is based on crime-density calculations from the dataset rather than direct model predictions.

---

## 📊 Dataset

The project uses a sample dataset (`crime_data.csv`) containing information such as:

- Area Name
- Latitude
- Longitude
- Murder Cases
- Theft Cases
- Assault Cases
- Robbery Cases
- Sexual Harassment Cases
- Total Crime
- Crime Per Area

> **Note:** The dataset used in this project is AI-generated for educational and demonstration purposes and does not represent official crime statistics.

---

## 🌍 APIs Used

### Nominatim

Used to convert user-entered place names into geographic coordinates.

---

### OpenRouteService

Used for route generation and travel time estimation.

---

### OpenStreetMap + Leaflet

Used to visualize routes on an interactive map.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Gayatri757/ChaloSafe.git
```

Move into the project directory:

```bash
cd ChaloSafe
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTESERVICE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

## 📸 Screenshots

### Sign Up

(Add screenshot here)

---

### Login

(Add screenshot here)

---

### Route Search

(Add screenshot here)

---

### Route Recommendation

(Add screenshot here)

---

## 🔮 Future Enhancements

- Use official real-time crime datasets
- Integrate live police APIs
- Improve route ranking using machine learning predictions
- Crime heatmap visualization
- Real-time traffic integration
- Emergency SOS functionality
- User profile management with a database
- Mobile application support

---

## 👩‍💻 Author

**Gayatri Adatiya**

AI & Data Science Student | Python Developer

GitHub: https://github.com/Gayatri757/ChaloSafe

# 🚦 ChaloSafe – Safe Route Recommendation System

ChaloSafe is a web-based **Safe Route Recommendation System** that helps users estimate the relative safety of a travel route by combining crime data with route planning.

Unlike traditional navigation systems that primarily optimize travel time or distance, ChaloSafe considers nearby crime density to estimate the **Route Risk** and help users make more informed travel decisions.

The project is developed using **Python (Flask)** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

# 📌 Problem Statement

Most navigation applications recommend the fastest or shortest route without considering public safety.

ChaloSafe addresses this limitation by analyzing nearby crime statistics and estimating the **Route Risk** for a journey. This allows users to choose routes that are not only efficient but also comparatively safer.

---

# ✨ Features

- User Sign Up & Sign In (Browser Local Storage)
- Search routes between any two locations
- Multiple travel modes
  - 🚗 Driving
  - 🚶 Walking
  - 🚴 Cycling
- Location geocoding using Nominatim API
- Route generation using OpenRouteService
- Interactive route visualization using Leaflet.js
- Route Risk estimation using nearby crime statistics
- Displays:
  - Travel Time
  - Route Risk Score
  - Risk Level (Low / Medium / High)

---

# 🛠 Tech Stack

## Backend

- Python
- Flask
- Flask-CORS
- Pandas
- Requests
- Joblib
- python-dotenv
- OpenRouteService Python SDK

## Frontend

- HTML5
- CSS3
- JavaScript
- Leaflet.js
- OpenStreetMap

## APIs

- Nominatim Geocoding API
- OpenRouteService Directions API

---

# 📂 Project Structure

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
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

# ⚙️ How It Works

### Step 1

The user enters:

- Current Location
- Destination
- Travel Mode

### Step 2

The backend converts the entered locations into latitude and longitude coordinates using the **Nominatim Geocoding API**.

### Step 3

The coordinates are sent to the **OpenRouteService Directions API**, which generates the travel route and estimates the travel duration.

### Step 4

The generated route contains multiple coordinate points.

For each route, nearby crime records are extracted from the dataset based on geographic proximity.

### Step 5

The application calculates a **Route Risk Score** by:

- Finding nearby crime records
- Summing their crime density values (`crime_per_area`)
- Normalizing the result to a score between **0 and 10**

### Step 6

The frontend displays:

- Interactive Route Map
- Estimated Travel Time
- Route Risk Score
- Risk Level

---

# 🚦 Route Risk Classification

| Route Risk | Level |
|------------|-------|
| 0 – 4 | 🟢 Low Risk |
| 4 – 7 | 🟡 Medium Risk |
| 7 – 10 | 🔴 High Risk |

Lower Route Risk indicates a comparatively safer route.

---

# 🧠 Algorithms Used

## 1. Geocoding

**Nominatim OpenStreetMap API**

Converts user-entered place names into latitude and longitude coordinates.

---

## 2. Route Generation

**OpenRouteService Directions API**

Generates travel routes based on:

- Source
- Destination
- Travel Mode

---

## 3. Route Risk Calculation

For each generated route:

- Extract route coordinates.
- Search nearby crime locations within approximately ±0.02° latitude and longitude.
- Aggregate nearby `crime_per_area` values.
- Normalize the result to a Route Risk score between **0 and 10**.
- Rank routes according to their calculated risk.

Routes with lower risk scores are considered safer.

---

# 🤖 Machine Learning Experimentation

As part of the project development, a **Random Forest Classifier** was trained to classify crime-risk levels using the following features:

- Latitude
- Longitude
- Crime Per Area

The training code is provided in **train_model.py**, and the trained model is stored as **crime_model.pkl**.

**Current Implementation**

The deployed application **does not use the Random Forest model for route recommendation**.

Instead, route risk is calculated directly from nearby crime-density values (`crime_per_area`) to provide a transparent and deterministic risk estimate.

The machine learning model has been retained in the repository as an experimental component and for future enhancements.

---

# 📊 Dataset

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

# 🌍 APIs Used

## Nominatim

Used to convert user-entered place names into geographic coordinates.

---

## OpenRouteService

Used for:

- Route generation
- Travel time estimation

---

## OpenStreetMap + Leaflet

Used to display routes on an interactive map.

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/Gayatri757/ChaloSafe.git
```

## Navigate to the project

```bash
cd ChaloSafe
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create a `.env` file

```
OPENROUTESERVICE_API_KEY=YOUR_API_KEY
```

## Run the backend

```bash
python app.py
```

## Open the frontend

Open:

```
frontend/index.html
```

or run it using **VS Code Live Server**.

The frontend communicates with the Flask backend running on:

```
http://localhost:5000
```

---

# 📸 Screenshots

## Sign Up

*(Add screenshot)*

---

## Sign In

*(Add screenshot)*

---

## Route Search

*(Add screenshot)*

---

## Route Recommendation

*(Add screenshot)*

---

# 🔮 Future Enhancements

- Integration with official crime datasets
- Real-time crime updates
- Crime heatmap visualization
- Live traffic integration
- Emergency SOS feature
- User authentication using a database
- Personalized route recommendations
- Mobile application
- Integrate the experimental machine learning model into the route recommendation pipeline

---

# 👩‍💻 Author

**Gayatri Adatiya**

B.E. Artificial Intelligence & Data Science

Python Developer | AI & ML Enthusiast

GitHub: **https://github.com/Gayatri757/ChaloSafe**

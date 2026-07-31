# 🛡️ ChaloSafe - Safe Route Recommendation System

A Flask-based web application that recommends safer travel routes by combining route generation with historical crime data. The application integrates geocoding and routing APIs to calculate a safety score for the generated route and display it on an interactive map.

> **Note:** This project was developed as an academic prototype. The crime dataset used is **synthetically generated** for demonstration purposes.

---

## 📌 Problem Statement

Traditional navigation systems recommend the shortest or fastest route without considering the safety of travelers. ChaloSafe addresses this limitation by analyzing crime statistics near a route and providing users with additional safety information to support informed travel decisions.

---

## ✨ Features

- 📍 Convert source and destination into geographic coordinates.
- 🗺️ Generate travel routes using OpenRouteService.
- 🔒 Calculate a route safety score based on nearby crime data.
- 📊 Display travel duration and safety score.
- 🌍 Interactive map using Leaflet and OpenStreetMap.
- 🤖 Random Forest model for crime risk classification.
- ⚡ RESTful backend built with Flask.

---

# 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-CORS

### Frontend
- HTML
- CSS
- JavaScript
- Leaflet.js

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Joblib

### Data Processing
- Pandas
- NumPy

### APIs
- OpenRouteService API
- Nominatim (OpenStreetMap)

---

# 🏗️ System Architecture

```text
                  User
                    │
                    ▼
        HTML + CSS + JavaScript
                    │
           HTTP POST Request
                    │
                    ▼
              Flask Backend
                    │
      ┌─────────────┼──────────────┐
      ▼             ▼              ▼
 Nominatim API  OpenRouteService   Crime Dataset
  (Geocoding)      (Routing)        (CSV)
      │             │
      └─────────────┼──────────────┘
                    ▼
         Safety Score Calculation
                    ▼
           JSON Response Returned
                    ▼
        Route Displayed on Leaflet
```

---

# ⚙️ How It Works

1. User enters the source and destination.
2. The frontend sends the request to the Flask backend.
3. Nominatim converts place names into latitude and longitude.
4. OpenRouteService generates the travel route.
5. Crime records near the generated route are identified.
6. A custom safety score is calculated using crime density.
7. The backend returns the route geometry, duration, and safety score.
8. The frontend displays the recommended route on the map.

---

# 🧠 Algorithms Used

### Geocoding
- Nominatim API converts place names into latitude and longitude coordinates.

### Route Generation
- OpenRouteService Routing API generates routes between two locations.

### Custom Route Safety Algorithm
The backend:
- Extracts route coordinates.
- Finds nearby crime records using latitude and longitude filtering.
- Calculates the total crime density.
- Normalizes the value to generate a safety score.
- Returns the safety score along with travel duration.

### Machine Learning
A Random Forest classifier is trained to classify locations into:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

Features Used:
- Latitude
- Longitude
- Crime per Area

---

# 📂 Project Structure

```text
ChaloSafe/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
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

# 📊 Dataset

The project uses a **synthetic crime dataset** created for educational and prototype purposes.

The dataset contains:

- Area Name
- Latitude
- Longitude
- Murder Cases
- Theft Cases
- Robbery Cases
- Assault Cases
- Sexual Harassment Cases
- Total Crimes
- Crime per Area

The synthetic data demonstrates how crime-aware route recommendation can be implemented. In a production environment, this dataset can be replaced with verified crime records from official government or law enforcement sources.

---

# 👩‍💻 My Contribution

I was responsible for the backend development of the project.

My contributions include:

- Developed the Flask backend.
- Designed REST API endpoints.
- Integrated the frontend with the backend using Fetch API and JSON.
- Integrated Nominatim API for geocoding.
- Integrated OpenRouteService API for route generation.
- Implemented the custom route safety scoring algorithm.
- Processed the crime dataset using Pandas.
- Trained and integrated a Random Forest model for crime risk classification.
- Added error handling and API validation.
- Assisted in deployment configuration.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Gayatri757/ChaloSafe.git
```

Navigate to the project directory

```bash
cd ChaloSafe
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENROUTESERVICE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📡 API Endpoint

### POST `/recommend_route`

#### Request

```json
{
  "start": "Swargate",
  "end": "Kothrud",
  "mode": "driving-car"
}
```

#### Response

```json
{
  "routes": [
    {
      "geometry": { ... },
      "duration": 520,
      "safety_score": 6.8,
      "final_score": 7.1
    }
  ]
}
```

---

# 📸 Screenshots

## Home Page

> Add a screenshot here.

## Route Recommendation

> Add a screenshot here.

## Interactive Map

> Add a screenshot here.

---

# ⚠️ Challenges Faced

- Integrating multiple third-party APIs.
- Handling geocoding failures and invalid locations.
- Designing a custom algorithm to estimate route safety.
- Processing crime data efficiently.
- Managing API keys securely during deployment.

---

# 🚀 Future Enhancements

- Integrate official crime datasets.
- Add real-time crime and traffic information.
- Implement GPS-based live navigation.
- Use PostgreSQL/PostGIS for efficient spatial queries.
- Improve the machine learning model using additional real-world features.
- Add user authentication and profile management.

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Backend development using Flask
- REST API development
- Third-party API integration
- Data processing with Pandas
- Machine Learning model integration
- JSON-based client-server communication
- Deployment of Python web applications

---

# 👤 Author

**Gayatri Adatiya**

B.E. Artificial Intelligence & Data Science

PES Modern College of Engineering, Pune

GitHub: https://github.com/Gayatri757

---

# 🙏 Acknowledgements

- Flask
- OpenStreetMap
- Nominatim
- OpenRouteService
- Scikit-learn
- Leaflet.js

document.addEventListener("DOMContentLoaded", function () {
    console.log("🚀 DOM loaded");

    const API_BASE_URL = "https://chalosafe-production.up.railway.app";


    const signupContainer = document.getElementById("signup-container");
    const signinContainer = document.getElementById("signin-container");
    const authContainer = document.getElementById("auth-container");
    const appContainer = document.getElementById("app-container");
    const mapContainer = document.getElementById("map-container");
    const routeInfoContainer = document.getElementById("route-info");
    const travelTimeElement = document.getElementById("travel-time");
    const safetyScoreElement = document.getElementById("safety-score");

    let map;
    let routeLayers = [];

    function toggleVisibility(element, show) {
        if (element) {
            element.style.display = show ? "block" : "none";
            element.classList.toggle("hidden", !show);
        }
    }

    function initMap() {
        if (map) return; 
        map = L.map("map").setView([28.6139, 77.2090], 12); 
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "© OpenStreetMap contributors"
        }).addTo(map);
    }

    async function handleSubmit(event) {
        event.preventDefault();

        const startLocation = document.getElementById("current-location").value.trim();
        const endLocation = document.getElementById("destination").value.trim();
        const mode = document.getElementById("travel-mode").value;

        if (!startLocation || !endLocation) {
            alert("❌ Please enter both start and destination locations.");
            return;
        }

        const routeRequest = {
            start: startLocation,
            end: endLocation,
            mode: mode
        };

        try {
            console.log("📡 Sending route request...", routeRequest);
            travelTimeElement.textContent = "Loading...";
            safetyScoreElement.textContent = "Loading...";

            const response = await fetch(`${API_BASE_URL}/recommend_route`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(routeRequest)
            });

            const data = await response.json().catch(() => {
                throw new Error("Invalid JSON from server");
            });

            if (!response.ok) {
                console.error("🚨 API error:", data);
                alert(`❌ ${data.error || "Unknown server error"}`);
                travelTimeElement.textContent = "N/A";
                safetyScoreElement.textContent = "N/A";
                return;
            }

            console.log("🗺️ Full route response:", data);
            const routes = data.routes || [data.best_route];

            if (!routes || routes.length === 0) {
                alert("⚠ No routes found.");
                return;
            }

            routeLayers.forEach(layer => map.removeLayer(layer));
            routeLayers = [];

            routes.sort((a, b) => a.safety_score - b.safety_score);

            routes.forEach((route, index) => {
                const coords = route.geometry.coordinates.map(c => [c[1], c[0]]);
                const color = index === 0 ? "green" : "gray";

                const polyline = L.polyline(coords, {
                    color,
                    weight: 5,
                    opacity: 0.8
                }).addTo(map);

                routeLayers.push(polyline);

                if (index === 0) {
                    map.fitBounds(polyline.getBounds());
                    travelTimeElement.textContent = `${(route.duration / 60).toFixed(2)} mins`;
                    safetyScoreElement.textContent = route.safety_score.toFixed(2);
                }
            });

            toggleVisibility(routeInfoContainer, true);
        } catch (error) {
            console.error("❌ Fetch error:", error);
            alert("🚫 Could not connect to the server. Is the backend running?");
            travelTimeElement.textContent = "N/A";
            safetyScoreElement.textContent = "N/A";
        }
    }

    
    document.getElementById("signup-form").addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (localStorage.getItem(email)) {
            alert("⚠ User already exists! Please sign in.");
            toggleVisibility(signupContainer, false);
            toggleVisibility(signinContainer, true);
            document.getElementById("signin-email").focus();
        } else {
            localStorage.setItem(email, JSON.stringify({ username, email, password }));
            alert("✅ Sign-up successful! Please sign in.");
            toggleVisibility(signupContainer, false);
            toggleVisibility(signinContainer, true);
            document.getElementById("signin-email").focus();
        }
    });

    
    document.getElementById("signin-form").addEventListener("submit", (e) => {
        e.preventDefault();
        const email = document.getElementById("signin-email").value;
        const password = document.getElementById("signin-password").value;

        const userData = localStorage.getItem(email);
        if (userData) {
            const user = JSON.parse(userData);
            if (user.password === password) {
                alert("✅ Sign-in successful!");
                toggleVisibility(authContainer, false);
                toggleVisibility(appContainer, true);
                toggleVisibility(mapContainer, true);
                initMap(); 
            } else {
                alert("❌ Incorrect password.");
            }
        } else {
            alert("❌ User not found. Please sign up.");
        }
    });

    
    document.getElementById("show-signin").addEventListener("click", (e) => {
        e.preventDefault();
        toggleVisibility(signupContainer, false);
        toggleVisibility(signinContainer, true);
        document.getElementById("signin-email").focus();
    });

    document.getElementById("show-signup").addEventListener("click", (e) => {
        e.preventDefault();
        toggleVisibility(signinContainer, false);
        toggleVisibility(signupContainer, true);
        document.getElementById("username").focus();
    });

    
    document.getElementById("route-form").addEventListener("submit", handleSubmit);
});

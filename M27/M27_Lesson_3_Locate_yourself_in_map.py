# M27 Lesson 1 – Introduction to Flask
# Short Description: Getting started with Flask, a lightweight Python web framework for building web applications.
# index.html ========================.
# <!DOCTYPE html>
# <html>
# <head>
#   <meta charset="utf-8" />
#   <title>Map Location Finder</title>

#   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
#   <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

#   <style>
#     html, body { margin: 0; padding: 0; height: 100%; }
#     form { padding: 12px; }
#     #mapContainer { width: 100vw; height: 80vh; }
#   </style>
# </head>

# <body>
#   <form method="POST" action="/">
#     <label>Enter the location here:</label>
#     <input type="text" name="location" required>
#     <button type="submit">Search</button>
#   </form>

#   {% if error %}
#     <p style="padding: 0 12px; color: red;">{{ error }}</p>
#   {% endif %}

#   {% if data and data.latitude and data.longitude %}
#     <h1 style="padding: 0 12px;">Details</h1>
#     <p style="padding: 0 12px;">The latitude is {{ data.latitude }}</p>
#     <p style="padding: 0 12px;">The longitude is {{ data.longitude }}</p>
#   {% endif %}

#   <!-- put values safely into HTML attributes -->
#   <div
#     id="mapContainer"
#     data-lat="{{ data.latitude if data and data.latitude else '' }}"
#     data-lon="{{ data.longitude if data and data.longitude else '' }}"
#   ></div>

#   <script>
#     const container = document.getElementById("mapContainer");
#     const latStr = container.dataset.lat;
#     const lonStr = container.dataset.lon;

#     // defaults so map always shows
#     let lat = 20.5937, lon = 78.9629, zoom = 4;

#     if (latStr && lonStr) {
#       lat = parseFloat(latStr);
#       lon = parseFloat(lonStr);
#       zoom = 12;
#     }

#     const map = L.map("mapContainer").setView([lat, lon], zoom);

#     L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
#       maxZoom: 19,
#       attribution: "&copy; OpenStreetMap contributors"
#     }).addTo(map);

#     if (latStr && lonStr) {
#       L.marker([lat, lon]).addTo(map);
#     }
#   </script>
# </body>
# </html>
# app.py ================================================
from flask import Flask, render_template, request
import json
import urllib.parse
import urllib.request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def details():
    if request.method == "GET":
        return render_template("index.html")

    location = request.form.get("location", "").strip()
    if not location:
        return render_template("index.html", error="Give the correct location")

    try:
        q = urllib.parse.quote(location)

        # ✅ Free working endpoint (no key): Photon (Komoot)
        url = f"https://photon.komoot.io/api/?q={q}&limit=1"
        req = urllib.request.Request(url, headers={"User-Agent": "FlaskGeocoder/1.0"})

        source = urllib.request.urlopen(req).read()
        responseData = json.loads(source)

        features = responseData.get("features", [])
        if not features:
            return render_template("index.html", error="Give the correct location")

        # Photon returns [longitude, latitude]
        lon, lat = features[0]["geometry"]["coordinates"]

        data = {
            "latitude": str(lat),
            "longitude": str(lon),
        }

        return render_template("index.html", data=data)

    except Exception:
        return render_template("index.html", error="Give the correct location")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
import folium
import pandas as pd

# Load the data from a CSV file containing volcano information
data = pd.read_csv("Volcanoes.txt")

# Extract latitude, longitude, and elevation data into separate lists
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Function to determine the marker color based on the elevation of the volcano
def color_producer(elevation):
    if elevation < 1000:
        return "green"  # Green for low elevation
    elif 1000 <= elevation < 3000:
        return "orange"  # Orange for medium elevation
    else:
        return "red"  # Red for high elevation

# Create a folium map object centered on a specific location with a starting zoom level
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

# Create a feature group for volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")

# Add markers to the map for each volcano using a circle marker with color based on elevation
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, color='grey', 
                                      popup=str(el) + " m", fill=True, 
                                      fill_color=color_producer(el), fill_opacity=0.7, weight=1))

# Create a feature group for population data
fgp = folium.FeatureGroup(name="Population")

# Load GeoJSON data for world population
with open("world.json", 'r', encoding="utf-8-sig") as f:
    geojson_data = f.read()

# Add population data to the map, coloring countries based on population size
fgp.add_child(folium.GeoJson(data=geojson_data,
                             style_function=lambda x: {
                                 "fillColor": "green" if x["properties"]["POP2005"] < 10000000 
                                 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 
                                 else "red",
                                 "color": "blue",  # Border color for countries
                                 "weight": 2,  # Border thickness
                                 "fillOpacity": 0.5  # Opacity of the fill color
                             }))

# Add both feature groups (volcanoes and population) to the map
map.add_child(fgv)
map.add_child(fgp)

# Add a layer control panel to allow users to toggle between volcano and population data
map.add_child(folium.LayerControl())

# Save the map to an HTML file
map.save("Map1.html")

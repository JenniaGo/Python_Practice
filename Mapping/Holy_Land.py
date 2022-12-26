import folium

# Create a map centered on Israel
m = folium.Map(location=[31.0461, 34.8516], zoom_start=7)

# Add markers for the main cities
folium.Marker(location=[31.0461, 34.8516], popup='Tel Aviv').add_to(m)
folium.Marker(location=[31.7683, 35.2137], popup='Jerusalem').add_to(m)
folium.Marker(location=[32.0853, 34.7818], popup='Haifa').add_to(m)
folium.Marker(location=[31.2518, 34.7913], popup='Ashdod').add_to(m)

# Display the map
m

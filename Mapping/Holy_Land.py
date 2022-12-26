import folium
from IPython.display import display

# Create a map centered on Israel
m = folium.Map(location=[31.0461, 34.8516], zoom_start=7)

# Add markers for the main cities
folium.Marker(location=[31.0461, 34.8516], popup='Tel Aviv').add_to(m)
folium.Marker(location=[31.7683, 35.2137], popup='Jerusalem').add_to(m)
folium.Marker(location=[32.0853, 34.7818], popup='Haifa').add_to(m)
folium.Marker(location=[31.2518, 34.7913], popup='Ashdod').add_to(m)
folium.Marker(location=[31.6697, 34.5681], popup='Ashqelon').add_to(m)
folium.Marker(location=[31.7174, 34.5858], popup='Shderot').add_to(m)

# Add a form to input the name and coordinates of a location
form = """
<form action="/add_marker" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="lat">Latitude:</label><br>
    <input type="text" id="lat" name="lat"><br>
    <label for="lon">Longitude:</label><br>
    <input type="text" id="lon" name="lon"><br><br>
    <input type="submit" value="Submit">
</form> 
"""

# Add the form to the map as a layer
form_layer = folium.IFrame(html=form, width=300, height=200)
form_popup = folium.Popup(form_layer, max_width=2650)
folium.Marker(location=[31.0461, 34.8516], popup=form_popup).add_to(m)

# Display the map
display(m)

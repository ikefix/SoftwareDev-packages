import folium

# Create a map centered at a specific location
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Add a circle marker to the map
folium.CircleMarker(
    location=[45.5215, -122.6764],
    radius=50,
    popup='The Waterfront',
    color='#3185cc',
    fill=True,
    fill_color='#3187cc'
).add_to(m)

# Add a tile layer to the map
folium.TileLayer('Stamen Terrain').add_to(m)

# Add a layer control to the map
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('map.html')

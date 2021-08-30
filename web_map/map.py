import folium

map = folium.Map(location=[54.72105836758883, 20.493974315870876], zoom_start=20, tiles='Stamen Terrain')

map.add_child(folium.Marker(location=[54.7, 20.4], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.save("Map1.html")

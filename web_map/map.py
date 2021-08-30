import folium

map = folium.Map(location=[54.72109254419616, 20.494004804299397], zoom_start=15, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[54.72109254419616, 20.494004804299397], popup='Шарага', icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")

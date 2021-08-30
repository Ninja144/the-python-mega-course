import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LON'])
lon = list(data['LAT'])

map = folium.Map(location=[54.72109254419616, 20.494004804299397], zoom_start=15, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[54.72109254419616, 20.494004804299397],[54.719608760713655, 20.492782895612876]]:
    fg.add_child(folium.Marker(location=coordinates, popup='Шарага', icon=folium.Icon(color='red')))
    # fg.add_child(folium.Marker(location=[54.719608760713655, 20.492782895612876], popup='Драмтеатр', icon=folium.Icon(color='pink')))

map.add_child(fg)

map.save("Map1.html")

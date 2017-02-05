from arcgis.gis import GIS 
from IPython.display import display

# gis = GIS()

# map1 = gis.map("Palm Springs, CA")

# items = gis.content.search('Palm Springs Trails')
# for item in items:
# 	display(item)

gis = GIS()
freeways = gis.content.get('91c6a5f6410b4991ab0db1d7c26daacb')
freeways

freeways.layers

for lyr in freeways.layers:
	print(lyr.properties.name)
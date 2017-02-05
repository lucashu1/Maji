locations = {
	"LOS ANGELES" : 
	{
		"Marina del Rey" : "Clean",
		"Venice" : "Dirty",
		"Santa Monica" : "Dirty"
	},
	"MICHIGAN" : 
	{
		"Flint" : "Dirty",
		"Lake Michigan" : "Clean"
	}
}

location = "LOS ANGELES"

print (locations["LOS ANGELES"].items())

for source, state in locations[location].items():
	print('Water source: {}. Status: {}'.format(source, state))
# An attempt to use a CSV file to create a world map model of population growth using the pygal module. 
import csv
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle

filename = 'pop_growth.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
# Printing the header row, in order to accurately parse the file. 
	for index, column_header in enumerate(header_row):
		print(index, column_header)

# Creating a dictionary of country codes as keys, pop growth is the value. 
	pop_growth_2017 = {}
	for row in reader:
		'''Loop through each row and convert the country into a country code and the the row for 2017 into a key'''
		country_code = get_country_code(row[0])
		if country_code == None:
			continue
		else:
			try:
				pop_growth_2017[country_code] = float(row[61])
			except ValueError:
				continue

# Format and render file. 
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Population Growth in 2017 by Country'
wm.add('2017', pop_growth_2017)
wm.render_to_file('pop_growth.svg')

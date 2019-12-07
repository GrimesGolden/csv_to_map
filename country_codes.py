'''A module containing get_country_code. Function returns the 2 digit country codes for given country'''

from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

def get_country_code(country_name):
	'''Return the pygal 2-digit country code for the given country'''
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
		elif country_name == 'Andorra':
			return 'ad'
		elif country_name == 'Bolivia':
			return 'bo'
		elif country_name == 'Dominica':
			return 'do'
		elif country_name == 'Egypt, Arab Rep.':
			return 'eg'
		elif country_name == 'Hong Kong SAR, China':
			return 'hk'
		elif country_name == 'Iran, Islamic Rep.':
			return 'ir'
		elif country_name == 'Korea, Dem. Rep.':
			return 'kp'
		elif country_name == 'Korea, Rep':
			return 'kr'
		elif country_name == 'Kyrgyz Republic':
			return 'kg'
		elif country_name == 'LAO PDR':
			return 'la'
		elif country_name == 'Libya':
			return 'ly'
		elif country_name == 'Macedonia, FYR':
			return 'mk'
		elif country_name == 'Yemen, Rep.':
			return 'ye'

	#If country not found return None.
	return None



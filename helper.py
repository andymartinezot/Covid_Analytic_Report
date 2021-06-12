import pandas as pd

class Mode:
    CASES = "Cases"
    DEATHS = "Deaths"
    VACCINES = "Vaccines"

def load_relevant_data(us_data=True, mode=Mode.CASES):
	# This can be changed to your local directory (./) for testing purposes
	BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
	#BASE_PATH = './data/'
	if us_data and mode == Mode.CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_US.csv'
	elif us_data and mode == Mode.DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_US.csv'
	elif not us_data and mode == Mode.CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_global.csv'
	elif not us_data and mode == Mode.DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_global.csv'

	return pd.read_csv(PATH)

def load_relevant_data_ar(ar_data=True, mode=Mode.CASES):
    #BASE_PATH = '/home/andy/Documents/PythonExercises/Analytics_Report/data/'
    BASE_PATH = 'https://raw.githubusercontent.com/andymartinezot/Covid_Analytic_Report/main/data/'
    if ar_data and mode == Mode.CASES:
        PATH = BASE_PATH + 'Covid19Cases_FINAL.csv'
    elif ar_data and mode == Mode.DEATHS:
        PATH = BASE_PATH + 'Covid19Deaths_FINAL.csv'
    elif ar_data and mode == Mode.VACCINES:
        PATH = BASE_PATH + 'Covid19VacunasAgrupadas.csv'

    
    return pd.read_csv(PATH)


def get_state_names():
    df = load_relevant_data()
    return df['Province_State'].unique()

def get_country_names():
    df = load_relevant_data(us_data=False)
    return df['Country/Region'].unique()

# United States of America Python Dictionary to translate States,
# Districts & Territories to Two-Letter codes and vice versa.
#
# https://gist.github.com/rogerallen/1583593
#
# Dedicated to the public domain.  To the extent possible under law,
# Roger Allen has waived all copyright and related or neighboring
# rights to this code.

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# thank you to @kinghelix and @trevormarburger for this idea
abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

ar_state_abbrev = {
    'Buenos Aires': 'BA',
    'Catamarca': 'CA',
    'Chaco': 'CH',
    'Chubut': 'CT',
    'Córdoba': 'CB',
    'Corrientes': 'CR',
    'Entre Ríos': 'ER',
    'Formosa': 'FO',
    'Jujuy': 'JY',
    'La Pampa': 'LP',
    'La Rioja': 'LR',
    'Mendoza': 'MZ',
    'Misiones': 'MI',
    'Neuquén': 'NQ',
    'Río Negro': 'RN',
    'Salta': 'SA',
    'San Juan': 'SJ',
    'San Luis': 'SL',
    'Santa Cruz': 'SC',
    'Santa Fe': 'SF',
    'Santiago del Estero': 'SE',
    'Tierra del Fuego': 'TF',
    'Tucumán': 'TU'
    }

abbrev_ar_state = dict(map(reversed, ar_state_abbrev.items()))

# Simple test examples
if __name__ == '__main__':
    print("Wisconin --> WI?", us_state_abbrev['Wisconsin'] == 'WI')
    print("WI --> Wisconin?", abbrev_us_state['WI'] == 'Wisconsin')
    print("Number of entries (50 states, DC, 5 Territories) == 56? ", 56 == len(us_state_abbrev))

    print("Buenos Aires --> BA?", ar_state_abbrev['Buenos Aires'] == 'BA')
    print("BA --> Buenos Aires?", abbrev_ar_state['BA'] == 'Buenos Aires')
    print("Number of entries (23 states) == 23? ", 23 == len(ar_state_abbrev))



# Python libraries
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Local files
from helper import load_relevant_data, load_relevant_data_ar, us_state_abbrev, ar_state_abbrev

def plot_usa_case_map(filename=None, day=None):
	df = load_relevant_data()
	dates = list(df.columns)
	df = df.groupby('Province_State')[dates].agg('sum')
	create_usa_figure(df, filename, day)

def plot_ar_case_map(filename=None, day=None):
	df = load_relevant_data(us_data=False)
	dates = list(df.columns)
	df = df.loc[(df['Country/Region'] == 'Argentina')]
	df = df.groupby('Country/Region')[dates].agg('sum')
	create_global_figure_ar(df, filename, day)

def plot_global_case_map(filename=None, day=None):
	df = load_relevant_data(us_data=False)
	dates = list(df.columns)
	df = df.groupby('Country/Region')[dates].agg('sum')
	create_global_figure(df, filename, day)

def create_usa_figure(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['state'] = [us_state_abbrev.get(x, None) for x in list(df.index)]
	

	fig = px.choropleth(df,
                    locations="state",
                    locationmode="USA-states",
                    scope="usa",
                    color="Cases",
                    hover_name="state",
                    color_continuous_scale='Peach',
                    title=f"US Daily Cases, {day}",
                    width=1000,
                    #height=500,
                    range_color=[0,3000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=0), title={"font": {"size": 20}, "x":0.5},)
	filename = filename if filename else "usa_chart.png"
	fig.write_image(filename, engine='kaleido')

#https://towardsdatascience.com/covid-19-map-animation-with-python-in-5-minutes-2d6246c32e54

def create_global_figure(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['Country'] = df.index

	fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    scope="world", # Try 'europe', 'africa', 'asia', 'south america', 'north america, world'
                    color="Cases",
                    hover_name="Country",
                    #projection="miller",
                    color_continuous_scale='Peach',
                    title=f"Global Daily Cases, {day}",
                    width=1000,
                    #height=500,
                    range_color=[0,50000])


	fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 20}, "x":0.5},)
	filename = filename if filename else "global_chart.png"
	fig.write_image(filename, engine='kaleido')

def create_global_figure_ar(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['Country'] = df.index

	fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    scope="south america", # Try 'europe', 'africa', 'asia', 'south america', 'north america, world'
                    color="Cases",
                    hover_name="Country",
                    #projection="miller",
                    color_continuous_scale='Peach',
                    title=f"Argentina Daily Cases, {day}",
                    width=1000,
                    #height=500,
                    range_color=[0,50000])


	fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 20}, "x":0.5},)
	filename = filename if filename else "argentina_chart.png"
	fig.write_image(filename, engine='kaleido')

if __name__ == '__main__':
	yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y")
	# Uncomment below line for testing
	yesterday = "10/10/20"

	#plot_usa_case_map(day=yesterday) # saves as usa_chart.png by default
	#plot_global_case_map(day=yesterday) # saves as global_chart.png by default
	plot_ar_case_map(day=yesterday)
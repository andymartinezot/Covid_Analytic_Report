# Python Libraries
from numpy.lib.function_base import place
from daily_counts import plot_data_new
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Local files
from helper import Mode, load_relevant_data, load_relevant_data_ar

def plot_total_vaccines_ar(states=['CABA'], column_dosis='dosis_totales', mode=Mode.VACCINES, filename=None):
    COLUMN = 'jurisdiccion_nombre'
    df = load_relevant_data_ar(True, mode)
    df = df.sort_values(['jurisdiccion_nombre'], ascending=True)
    df['dosis_totales'] = df['primera_dosis_cantidad'] + df['segunda_dosis_cantidad']
    df = df.groupby('jurisdiccion_nombre').sum().reset_index()
    plot_data_new(df, states, column_dosis, mode, COLUMN, filename)

def plot_total_vaccines_twodoses_ar(states=['CABA'], column1='primera_dosis_cantidad', column2='segunda_dosis_cantidad', mode=Mode.VACCINES, filename=None):
	df = load_relevant_data_ar(True, mode)
	df = df.sort_values(['jurisdiccion_nombre'], ascending=True)
	df['dosis_totales'] = df['primera_dosis_cantidad'] + df['segunda_dosis_cantidad']
	df = df.groupby('jurisdiccion_nombre').sum().reset_index()
	plot_data_two_doses(df, states, mode, column1, column2, filename)

def plot_data_new(df, places, column_value, mode, column, filename):
	n = len(places)
	colors = plt.cm.Reds(np.linspace(0.35,0.65,n))

	values = []
	for index, place in enumerate(places): #https://www.geeksforgeeks.org/enumerate-in-python/
		cumulative_data = df[df[column] == place]
		values.append(int(cumulative_data[column_value]))

	plt.figure(figsize=(15,10))
	plt.bar(places, values, color=colors)
	label_figure(places,column_value, mode, filename)

def set_size(w,h, ax=None):
    " w, h: width, height in inches"
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

def plot_data_two_doses(df, places, mode, column1, column2, filename):
	n = len(places)
	colors = plt.cm.Reds(np.linspace(0.35,0.65,n))
	deegres = 70

	first_dose = list(df[column1])
	second_dose = list(df[column2])
	province = df['jurisdiccion_nombre']
	dfnew = pd.DataFrame({'first_dose': first_dose,
                   		'second_dose': second_dose},
						index=province)

	ax = dfnew.plot.bar(rot=0, width=0.8, color=plt.cm.Reds(np.linspace(0.35,0.65,n)))
	set_size(10,7)
	
	ax.set_xticklabels(df['jurisdiccion_nombre'], rotation=deegres, size=10)
	plt.title(f'{mode}, Two Doses')
	plt.ylabel(f"{mode}")
	plt.ticklabel_format(style='plain', axis='y')
	plt.grid(True, axis='y', ls = '-.',lw = 2)
	filename = filename if filename else f'{mode}_twodoses.png'
	plt.savefig(filename)
	#plt.show()
	plt.close()
	
def label_figure(places, column_value, mode, filename):
	deegres=70
	plt.xticks(places, rotation=deegres, size=12)
	plt.title(f'{mode}, Total Doses')
	plt.ylabel(f"{mode}")
	plt.ticklabel_format(style='plain', axis='y')
	plt.grid(True, axis='y', ls = '-.',lw = 2)
	filename = filename if filename else f'{mode}_{column_value}.png'
	plt.savefig(filename)
	#plt.show()
	plt.close()


if __name__ == '__main__':
	
	states = ["Buenos Aires", "CABA"]
	#plot_total_vaccines_ar(states, column_dosis="dosis_totales")
	plot_total_vaccines_twodoses_ar(states)
	#plot_daily_count_states(states, mode=Mode.DEATHS)
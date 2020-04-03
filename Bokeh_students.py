#!/usr/bin/env python3.7
####################################################
#
# Author: M Joyce
# For use with ASTR3007/6007 MESA-based assignments
#
####################################################
import numpy as np
import pandas as pd
import bokeh
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file 

MESA_file = 'trimmed_history.data'

#0 			  1 	   2 		 3 	    4		5
#model_number star_age star_mass log_L  log_R   log_Teff 
model_number, star_age, log_Teff, log_L= np.loadtxt(MESA_file, usecols=(0,1,5,3), unpack=True, skiprows=6)


star_age = star_age/1e9
select = np.where( (star_age <= 13.9) & (star_age >= 0.5) )[0]
model_number = model_number[select]
star_age = star_age[select]
log_Teff = log_Teff[select]
log_L = log_L[select]


## the dictionary
star_features ={
	 'star_age': star_age,
	 'model_number': model_number,
	 'log_Teff': log_Teff,
	 'log_L': log_L
	 }

df = pd.DataFrame(data=star_features)
source = ColumnDataSource(data=df)

TITLE = "Interactive HR"
TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS, toolbar_location="above", plot_width=600, plot_height=800, title=TITLE)
p.toolbar.logo = "grey"
p.background_fill_color = "#dddddd"
p.xaxis.axis_label = "log Teff"
p.yaxis.axis_label = "log L"
p.grid.grid_line_color = "white"

## the labels
p.hover.tooltips = [
    ("star age (Gyr):", "@star_age"),
    ]#("model number", "@model_number"),
	#]

p.circle('log_Teff', 'log_L', size=5, source = source, 
         color='green',  fill_alpha=0.8) #line_color="black",
p.x_range.flipped = True

output_file("HR.html", title="Bokeh HR plot example")#, mode='inline')
show(p)

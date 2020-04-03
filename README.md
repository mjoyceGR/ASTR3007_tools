# ASTR3007_tools 

## requires Python version 3.7

## Dependencies:
### numpy

### pandas

### ColumnDataSource 

## Installation

## Use
Once you have Python3.7 and the other packages installed, type this in the terminal:

	python3 Bokeh_students.py

the result should be that an interactive HR diagram pops up in your web browser

## Data inspection
One way to change the file you are viewing is to open the script

	Bokeh_students.py

in Sublime, gedit, Atom, Nano, or any other text editor and change the name of the file to be loaded in line 14:

	MESA_file = 'trimmed_history.data' --> MESA_file = 'folder_name/whatever_your_file_is_called'

Note that you can include folders in your path. Since you are downloading multiple tracks, make sure you do not accidentally overwrite any of the history data by putting files with the same name in the same location!

Note that lines 16-18 in the Bokeh_students.py script tell the script which columns to read from trimmed_history.data. You may also change these manually to inspect other elements of the MESA evolutionary data. The quantity "star_age" is the default value that appears when you hover your curser in the browser. 

This tool is intended only as a guide or starting point. If those of you with more advanced programming skills choose to modify this to help answer assignment questions more efficiently, please share your modifications with the rest of the class either here or via the Wattle forum.


"""
Copyright 2022 Yoan POUZET
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or 
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
import csv
import bokeh
import os
from bokeh.plotting import figure, show, output_file
from bokeh.models import DatetimeTickFormatter, WheelZoomTool, HoverTool
from bokeh.themes import built_in_themes
from bokeh.io import curdoc

# Declaration des variables
output_file("graphique.html",title='Graphique')

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []

format = '%y-%m-%d %H:%M'


# On importe les fichiers CSV
with open('/home/yoan/NotSoEasyPref/Data/depot_1er_TDS.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x1.append(datetime.datetime.strptime(str(row[0]), format))
        y1.append(row[1])
with open('/home/yoan/NotSoEasyPref/Data/renouvelement_TDS.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x2.append(datetime.datetime.strptime(str(row[0]), format))
        y2.append(row[1])
with open('/home/yoan/NotSoEasyPref/Data/retrait_TDS.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x3.append(datetime.datetime.strptime(str(row[0]), format))
        y3.append(row[1])
with open('/home/yoan/NotSoEasyPref/Data/retrait_recepisse.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x4.append(datetime.datetime.strptime(str(row[0]), format))
        y4.append(row[1])
with open('/home/yoan/NotSoEasyPref/Data/retrait_DCEM_TVR_TIV.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x5.append(datetime.datetime.strptime(str(row[0]), format))
        y5.append(row[1])
with open('/home/yoan/NotSoEasyPref/Data/regularisation_sejour.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x6.append(datetime.datetime.strptime(str(row[0]), format))
        y6.append(row[1])


# On cree le graphique
p = figure(
    title="Disponibilités de créneaux au bureau du droit au séjour des étrangers de la Préfecture de la Seine-Maritime",
    x_axis_label="date et heure",
    x_axis_type ='datetime',
    y_axis_label="créneaux disponibles",
    sizing_mode ="stretch_both",
)

p.step(x1,y1, legend_label="Dépôt d'un premier titre de séjour", line_width=2, color='red')
p.step(x2,y2, legend_label="Renouvellement d'un titre de séjour", line_width=2, color='green')
p.step(x3,y3, legend_label="Retrait d'un titre de séjour", line_width=2, color='blue')
p.step(x4,y4, legend_label="Retrait d'un récépissé", line_width=2, color='sienna')
p.step(x5,y5, legend_label="Retrait d'un document de voyage", line_width=2, color='orange')
p.step(x6,y6, legend_label="Régularisation du séjour", line_width=2, color='white')


# On change l'aspect visuel de ...
## la legende
p.legend.title = "Motif de rendez-vous"
p.legend.click_policy = "hide"
p.legend.background_fill_color = "white"
p.legend.background_fill_alpha = 0.2
## du titre
p.title.text_font_size = "16px"
p.title.align = "center"
## du theme
output_file("bokeh.html")
curdoc().theme = 'night_sky'
## des axes
p.xaxis.axis_label = "date et heure"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"
p.yaxis.axis_label = "créneaux disponibles"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6
## de l'axe x pour la gestion des dates
p.xaxis[0].formatter = DatetimeTickFormatter(hours = ['%H:%M'], days = ['%A %d %B'])
## de l'arriere grille
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [4, 8]
p.xgrid.band_fill_color = "olive"
p.xgrid.band_fill_alpha = 0.1

# On ajoute des outils pour parfaire la consultation du graphique
## les défilements horizontaux pour contrôler les espacements entre les données temporelles
defilementHorizontal = WheelZoomTool(dimensions = 'width', description = "Contrôler à la molette l'abcisse")
defilementVertical = WheelZoomTool(dimensions = 'height', description = "Contrôler à la molette l'ordonnée")
p.add_tools(defilementHorizontal, defilementVertical)
p.toolbar.active_scroll = defilementHorizontal

## on affiche le graphique
show(p)

## on le déplace vers le dossier qui est mis en ligne
os.replace("/home/yoan/bokeh.html", "/home/yoan/NotSoEasyPref/Data/graphique.html")

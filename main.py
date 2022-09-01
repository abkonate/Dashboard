
from os.path import dirname, join

import numpy as np
import pandas as pd
from bokeh.models import CustomJS, ColumnDataSource, Select, Column
from bokeh.plotting import figure, show
from bokeh.models.widgets import Div
from bokeh.models.widgets import Paragraph
from bokeh.models.widgets import PreText
from bokeh.layouts import row
from bokeh.models import CheckboxGroup, CustomJS
from bokeh.io import curdoc
from bokeh.models import PreText
from bokeh.models.widgets import TextInput
import pandas_bokeh
import os



data_prediction = pd.read_csv(join(dirname(__file__), 'application_proba_prediction.csv'))

absolute_path = os.path.abspath(os.path.dirname('HomeCredit_columns_description.csv'))

HomeCredit_columns_description = pd.read_csv(absolute_path + '/HomeCredit_columns_description.csv' ,encoding='cp1252')


Var_Name = HomeCredit_columns_description[['Row','Description']]

Var_Name = Var_Name.drop_duplicates(subset=['Row'])


df_train = pd.read_csv(join(dirname(__file__),"application_train.csv"))

df = data_prediction.copy()

source = ColumnDataSource(df)

#print( source.data['label'])

df_index = list(map(str, df['SK_ID_CURR']))

Title = Div(text=""" <h1> Avec ce dashboard, on peut calculer la probabilité du risque de remboursement pour un client </h1>""" , width=200, height=400)

select = Select(title="Choisir l'id d'un client:", value='106861',
                options=df_index)


expl1 = Div(text=""" La probabilité sur risque de rembpursement est calculée sur la base de plusieurs variables.
                     On peut choisir une variable pour sa valeurs pour le client choisi, afficher sa distribution 
                     pour comparer le client par rapport aux autres.""" , width=200, height=300)



select2 = Select(title="Choisir une variable:", value='AMT_CREDIT' , options=list(Var_Name['Row'].values))

df_desc = Var_Name[Var_Name['Row'] == 'NAME_CONTRACT_TYPE' ]

#df_train_var = df_train[['TARGET', select2.value]]

#df_train_var = df_train_var.dropna()


#p_scatter = df_train_var.plot_bokeh.scatter(
#    figsize=(900, 600),
#    x="TARGET",
#    y= select2.value,
#    category="TARGET",
#    title="Variable choisie en fonction target",
#    #size="CNT_CHILDREN",
#    show_figure=False
#    )


description_of_variable = TextInput(value = str(df_desc['Description'].values) , title = "Description de la varibale choisie :")


Title2 = Div(text=""" <h1> La probabilité du risque de remboursement est estimée à  </h1>""" , width=800, height=100)


proba_remb = TextInput(value = str(0.5) , title = "")

df_aux = df [df['SK_ID_CURR'] == int(select.value)]

proba_remb.value = str(df_aux['label'].values)



def create_figure():
  df_train_var = df_train[['TARGET', select2.value]]
  df_train_var = df_train_var.dropna()
  xs = df_train_var['TARGET'].values
  ys = df_train_var[select2.value].values

  x_title = 'Target'
  y_title = select2.value

  dic_cat = {}

  if df_train_var[select2.value].dtype == object:
    kw = list(set(ys))
    nb_cat  = len(kw)
    for i in range(nb_cat):
      dic_cat[kw[i]] = i
    
    ys =[ dic_cat[a] for a in list(ys) ]

  p = figure(height=500, width=800, tools='pan,box_zoom,hover,reset')
  p.xaxis.axis_label = x_title
  p.yaxis.axis_label = y_title

  p.circle(x=xs, y=ys, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, size=10)

  return p


def update(attr, old, new):
    Col2.children[2] = create_figure()

def variable_choisie(attrname, old, new):
  p_scatter = df_train_var.plot_bokeh.scatter(
    figsize=(900, 600),
    x="TARGET",
    y= select2.value,
    category="TARGET",
    title="Variable choisie en fonction target",
    #size="CNT_CHILDREN",
    show_figure=False
    )
  
def client_choisi(attrname, old, new):
  df_aux = df [df['SK_ID_CURR'] == int(select.value)]
  proba_remb.value = str(df_aux['label'].values)
  #print(df_aux['label'].values)



select.on_change('value', client_choisi)

#select2.on_change('value', variable_choisie)

select2.on_change('value', update)


Col1 = Column(Title, select, select2, expl1, description_of_variable)

#Col2 = Column(Title2, proba_remb, p_scatter)

Col2 = Column(Title2, proba_remb, create_figure())

# add to document
#curdoc().add_root(row(Col1,Col2))
#curdoc().title = "Clustering"

#show(row(Col1,Col2))




#data_prediction = pd.read_csv('application_test_prediction.csv')

#df = data_prediction.copy()

#df_index = list(map(str, df['SK_ID_CURR']))





#select = Select(title="Custoimer ID:", value='106861',
#                options=df_index)



#div = Div(text=""" Le risque de remboursement du client """ + select.value +""" est de""", width=200, height=100)


#LABELS = ["Afficher la probabilité du risque de remboursement", 
#          "Afficher les informations du client", 
#          "Afficher les indicateurs de comparaisons avec les autres clients"]

#checkbox_group = CheckboxGroup(labels=LABELS, active=[1])


#df_aux = df [df['SK_ID_CURR'] == int('106861')]

#description = PreText(text="la probabilité du risque de rembouresement est estimée à" + str(df_aux['label'].values), width=500)

#div = Div(text=""" ii""", width=200, height=100)
#for col in df_aux.columns:
#  div.text = div.text + col +"      " + str(df_aux[col].values) + "     "  + '</br>'




#div = Div(text=str(df_aux.to_html()), width=200, height=100)



#def client_choisi(attrname, old, new):
#  df_aux = df [df['SK_ID_CURR'] == int(select.value)]
#  description.text = str(df_aux['label'])
#  div = Div(text=""" Le risque de remboursement du client """ + select.value +""" est de""", width=200, height=1000)
#  description_of_variable.value = "apres hanget"
  

#def information_client(attrname, old, new):
#  df_aux = df [df['SK_ID_CURR'] == int('106861')]
#  if 0 in checkbox_group.active:
#    div = Div(text="""""", width=200, height=100)
#    for col in df_aux.columns:
#      div.text = div.text + col +"      " + str(df_aux[col].values) + "     "  + '</br>'
#  if 1 in checkbox_group.active:
#    print('fonction à définir')
#  if 2 in checkbox_group.active:
#    print('fonction à définir')


#description_of_variable = TextInput(value = "Debut" , title = "Description :")


#select.on_change('value', client_choisi)

#div.on_change('text', client_choisi)

#checkbox_group.on_change('labels', information_client)

#controle = Column(select, checkbox_group, div,description_of_variable)

#show(row(controle, div))

# add to document
curdoc().add_root(row(Col1,Col2))
curdoc().title = "Dash"


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
import os
import gdown


if os.path.isfile('./Projet+Mise+en+prod+-+home-credit-default-risk.zip') == False:
  output="Projet+Mise+en+prod+-+home-credit-default-risk.zip"
  url = "https://drive.google.com/file/d/1WMSzXPeZzgZB9WvbEg9KT-nZom_jdhMN/view?usp=sharing"
  gdown.download(url=url, output=output, quiet=False, fuzzy=True)

if os.path.isfile('./application_proba_prediction.csv') == False:
  output2 ="application_proba_prediction.csv" 
  url2 = "https://drive.google.com/file/d/1-14BNXfPwiEP5pN1ornSj0Ct-jy2T19z/view?usp=sharing"
  gdown.download(url=url2, output=output2, quiet=False, fuzzy=True)

import shutil

if os.path.isfile('./Projet+Mise+en+prod+-+home-credit-default-risk.zip') == True:
  shutil.unpack_archive('Projet+Mise+en+prod+-+home-credit-default-risk.zip', './')

data_prediction = pd.read_csv("./application_proba_prediction.csv")
data_prediction = data_prediction.drop('Unnamed: 0', axis=1)

HomeCredit_columns_description = pd.read_csv('./HomeCredit_columns_description.csv',encoding='cp1252')
HomeCredit_columns_description = HomeCredit_columns_description.drop('Unnamed: 0', axis=1)

Var_Name = HomeCredit_columns_description[['Row','Description']]
Var_Name = Var_Name.drop_duplicates(subset=['Row'])


df_train = pd.read_csv("./application_train.csv")
df_test  = pd.read_csv("./application_test.csv")

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



select2 = Select(title="Choisir une variable:", value='AMT_REQ_CREDIT_BUREAU_YEAR' , options=list(Var_Name['Row'].values))

df_desc = Var_Name[Var_Name['Row'] == 'AMT_REQ_CREDIT_BUREAU_YEAR' ]


def create_figure():
  df_train_var = df_train[['TARGET', select2.value]]
  df_train_var = df_train_var.dropna()

  df_train_var_1 = df_train_var[ df_train_var['TARGET'] == 1 ]
  df_train_var_0 = df_train_var[ df_train_var['TARGET'] == 0 ]

  xs = df_train_var_1['TARGET'].values
  ys = df_train_var_1[select2.value].values

  x_title = 'Distribution'
  y_title = select2.value

  dic_cat = {}

  
  if df_train_var[select2.value].dtype == object:
    kw = list(set(df_train_var[select2.value].values))
    nb_cat  = len(kw)
    for i in range(nb_cat):
      dic_cat[kw[i]] = i
    
    ys =[ dic_cat[a] for a in list(ys) ]

    text_des = ""

    for keys,values in dic_cat.items():
      text_des +=  str(keys) +" " + str(values)+ " "

    print(text_des)

    x_title = text_des
    

  if df_train_var_1[select2.value].dtype == object:
    bins  = np.array(list(set(ys)))
  elif df_train_var_1[select2.value].dtype == np.int64:
    bins  = np.array(list(set(ys)))
  else:
    bins = np.linspace(ys.min(), ys.max(), 100)

  hist, edges = np.histogram(ys, density=True, bins=bins)

  #print(edges)

  p = figure(height=600, width=800, tools='pan,box_zoom,hover,reset')
  p.xaxis.axis_label = x_title
  p.yaxis.axis_label = y_title

  p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
         fill_color="skyblue", line_color="white",
         legend_label=f"label 1")
  
  # Probability density function
  #x = np.linspace(-5.0, 5.0, len(ys))
  #p.line(x, ys, line_width=2, line_color="navy",
  #legend_label="Probability Density Function")

  #p.circle(x=xs, y=ys, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, size=10)

  xs = df_train_var_0['TARGET'].values
  ys = df_train_var_0[select2.value].values

  #x_title = 'Target'
  #y_title = select2.value

  dic_cat = {}

  if df_train_var[select2.value].dtype == object:
    kw = list(set(df_train_var[select2.value].values))
    nb_cat  = len(kw)
    for i in range(nb_cat):
      dic_cat[kw[i]] = i
    
    ys =[ dic_cat[a] for a in list(ys) ]
    #print(dic_cat)

  #print(ys.min())
  #print(ys.max())
  #print(len(ys))
  #bins = np.linspace(ys.min(), ys.max(), 10)

  #print(bins)

  hist, edges = np.histogram(ys, density=True, bins=bins)

  #print(edges)

  #p = figure(height=600, width=800, tools='pan,box_zoom,hover,reset')
  #p.xaxis.axis_label = x_title
  #p.yaxis.axis_label = y_title

  p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
         fill_color="skyblue", line_color="red",
         legend_label=f"label 0")

  return p


def update(attr, old, new):
    Col2.children[2] = create_figure()


description_of_variable = TextInput(value = str(df_desc['Description'].values) , title = "Description de la varibale choisie :")

df_aux = df_test [df_test['SK_ID_CURR'] == int(select.value)]

info_of_customer = Div(text=(df_aux.T).to_html(index=True), width=550)
#info_of_customer = TextInput(value = str(df_aux) , title = "information client :")

Title2 = Div(text=""" <h1> La probabilité du risque de remboursement est estimée à  </h1>""" , width=800, height=100)

proba_remb = TextInput(value = str(0.5) , title = "")

  
def client_choisi(attrname, old, new):
  df_aux = df [df['SK_ID_CURR'] == int(select.value)]
  print(df_aux['label'].values)
  df_aux = df_test [df_test['SK_ID_CURR'] == int(select.value)]
  Col3.children[0] = Div(text=(df_aux.T).to_html(index=True), width=550)



select.on_change('value', client_choisi)

select2.on_change('value', update)


Col1 = Column(Title, select, select2, expl1, description_of_variable)

Col2 = Column(Title2, proba_remb, create_figure())

Col3 = Column(info_of_customer)

layout = row(Col1,Col2, Col3) 

# add to document
curdoc().add_root(layout)
curdoc().title = "Dashboard"

#layout = row(Col1,Col2, Col3) 

#show(layout)







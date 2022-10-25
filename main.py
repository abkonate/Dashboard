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
from bokeh.models import FactorRange
import os
import shutil
import shap
import lightgbm as lgb
from urllib.request import urlopen
import json

columns_acc =['FLOORSMAX_MODE',
              'FLOORSMAX_MEDI',
              'FLOORSMAX_AVG',
              'YEARS_BEGINEXPLUATATION_MODE',
              'YEARS_BEGINEXPLUATATION_MEDI',
              'YEARS_BEGINEXPLUATATION_AVG',
              'TOTALAREA_MODE',
              'EMERGENCYSTATE_MODE',
              'OCCUPATION_TYPE',
              'EXT_SOURCE_3',
              'AMT_REQ_CREDIT_BUREAU_MON',
              'AMT_REQ_CREDIT_BUREAU_QRT',
              'AMT_REQ_CREDIT_BUREAU_YEAR',
              'NAME_TYPE_SUITE',
              'OBS_30_CNT_SOCIAL_CIRCLE',
              'DEF_30_CNT_SOCIAL_CIRCLE',
              'OBS_60_CNT_SOCIAL_CIRCLE',
              'DEF_60_CNT_SOCIAL_CIRCLE',
              'EXT_SOURCE_2',
              'AMT_GOODS_PRICE',
              'AMT_ANNUITY',
              'CNT_FAM_MEMBERS',
              'DAYS_LAST_PHONE_CHANGE',
              'CNT_CHILDREN',
              'FLAG_DOCUMENT_8',
              'NAME_CONTRACT_TYPE',
              'CODE_GENDER',
              'FLAG_OWN_CAR',
              'FLAG_DOCUMENT_3',
              'FLAG_DOCUMENT_5',
              'FLAG_DOCUMENT_6',
              'FLAG_DOCUMENT_7',
              'FLAG_DOCUMENT_9',
              'FLAG_DOCUMENT_21',
              'FLAG_DOCUMENT_11',
              'FLAG_OWN_REALTY',
              'FLAG_DOCUMENT_13',
              'FLAG_DOCUMENT_14',
              'FLAG_DOCUMENT_15',
              'FLAG_DOCUMENT_16',
              'FLAG_DOCUMENT_17',
              'FLAG_DOCUMENT_18',
              'FLAG_DOCUMENT_19',
              'FLAG_DOCUMENT_20',
              'AMT_CREDIT',
              'AMT_INCOME_TOTAL',
              'FLAG_PHONE',
              'LIVE_CITY_NOT_WORK_CITY',
              'REG_CITY_NOT_WORK_CITY',
              'REG_CITY_NOT_LIVE_CITY',
              'LIVE_REGION_NOT_WORK_REGION',
              'REG_REGION_NOT_WORK_REGION',
              'REG_REGION_NOT_LIVE_REGION',
              'HOUR_APPR_PROCESS_START',
              'WEEKDAY_APPR_PROCESS_START',
              'REGION_RATING_CLIENT_W_CITY',
              'REGION_RATING_CLIENT',
              'FLAG_EMAIL',
              'FLAG_CONT_MOBILE',
              'ORGANIZATION_TYPE',
              'FLAG_WORK_PHONE',
              'FLAG_EMP_PHONE',
              'DAYS_ID_PUBLISH',
              'DAYS_REGISTRATION',
              'DAYS_EMPLOYED',
              'DAYS_BIRTH',
              'REGION_POPULATION_RELATIVE',
              'NAME_FAMILY_STATUS',
              'NAME_EDUCATION_TYPE',
              'NAME_INCOME_TYPE']

#data_prediction = pd.read_csv("/app/data/application_proba_prediction.csv")
#data_prediction = data_prediction.drop('Unnamed: 0', axis=1)

HomeCredit_columns_description = pd.read_csv('/app/data/HomeCredit_columns_description.csv',encoding='cp1252')
HomeCredit_columns_description = HomeCredit_columns_description.drop('Unnamed: 0', axis=1)

Var_Name = HomeCredit_columns_description[['Row','Description']]
Var_Name = Var_Name.drop_duplicates(subset=['Row'])


df_train = pd.read_csv("./data/application_train.csv")
df_test  = pd.read_csv("/app/data/application_test.csv")

feature_imp = pd.read_csv("/app/data/coefs_feature_importance.csv")

from pickle import load
explainer = load(open('/app/data/explainer.pkl', 'rb'))
normed_vec = load(open('/app/data/normed_vec.pkl', 'rb'))

#df_test['label'] = data_prediction['label'].values

#df = data_prediction.copy()

#source = ColumnDataSource(df)

#print( source.data['label'])

df_index = list(map(str, df_test['SK_ID_CURR']))

Title = Div(text=""" <h1> Avec ce dashboard, on peut calculer la probabilité du risque de remboursement pour un client </h1>""" , width=100, height=400)

select = Select(title="Choisir l'id d'un client:", value='106861', options=df_index)


expl1 = Div(text=""" La probabilité sur risque de remboursement est calculée sur la base de plusieurs variables.
                     On peut choisir une variable et  afficher sa distribution 
                     pour comparer le client par rapport aux autres.""" , width=100, height=300)



select2 = Select(title="Choisir une variable:", value='AMT_REQ_CREDIT_BUREAU_YEAR' , options=list(Var_Name['Row'].values))

df_desc = Var_Name[Var_Name['Row'] == 'AMT_REQ_CREDIT_BUREAU_YEAR' ]


feat_imp_data = feature_imp.head(10)

p_imp = figure(y_range=FactorRange(factors=feat_imp_data['Unnamed: 0']), plot_height=250, title="feature importance",toolbar_location=None, tools="")

p_imp.hbar(y=feat_imp_data['Unnamed: 0'], right=feat_imp_data['Coefficients'])



index_client = df_index.index(select.value)

shap_values = explainer(normed_vec[index_client:index_client+1,:])
  
sdf_train = pd.DataFrame({
  'feature': columns_acc,
  'shap_values': shap_values.values[:,:,1].flatten()   
})
  
sdf_train['shap_values_abv'] = sdf_train['shap_values'].abs()
  
data_sv = sdf_train.sort_values(by=['shap_values_abv'], ascending = False).head(10)


features =  data_sv['feature'].values 
shap_v = data_sv['shap_values'].values

color =[]

for el in shap_v:
  if el > 0:
    color.append("red")
  else:
    color.append("green")

p_shap = figure(y_range=FactorRange(factors=features), plot_height=250, title="shap values",toolbar_location=None, tools="")

  
p_shap.hbar(y=features, right=shap_v, color=color)


def create_figure():
  
  df_desc = Var_Name[Var_Name['Row'] == select2.value ]

  Col1.children[4] = Div(text = str(df_desc['Description'].values) , width=100)
  
  
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

  #p = figure(height=500, width=500, tools='pan,box_zoom,hover,reset')
  p = figure(tools='pan,box_zoom,hover,reset')
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
    Col2.children[4] = create_figure()


description_of_variable = TextInput(value = str(df_desc['Description'].values) , title = "Description de la varibale choisie :")

df_aux = df_test [df_test['SK_ID_CURR'] == int(select.value)]

#df_aux = df [df['SK_ID_CURR'] == int(select.value)]

info_of_customer = Div(text=(df_aux.T).to_html(index=True), width=550)

#info_of_customer = TextInput(value = str(df_aux) , title = "information client :")

Title2 = Div(text=""" <h1> La probabilité du risque de remboursement est estimée à  </h1>""" , width=400, height=100)

#proba_remb = TextInput(value = str(0.5) , title = "")

#df_aux0 = df_test [df_test['SK_ID_CURR'] == int(select.value)]

API_url = "https://warm-bastion-82817.herokuapp.com/credit/" + select.value

json_url = urlopen(API_url)

API_data = json.loads(json_url.read())

proba_remb = Div(text= str(API_data['la probabilte du risque']), width=550, style={'font-size': '300%', 'color': 'blue', 'text-align': 'center'})

  
def client_choisi(attrname, old, new):
  df_aux = df_test [df_test['SK_ID_CURR'] == int(select.value)]

  API_url = "https://warm-bastion-82817.herokuapp.com/credit/" + select.value

  json_url = urlopen(API_url)
  
  API_data = json.loads(json_url.read())

  Col2.children[1] = Div(text= str(API_data['la probabilte du risque']), width=550, style={'font-size': '300%', 'color': 'blue', 'text-align': 'center'})
  
  #Col2.children[1] = Div(text= str(df_aux['label'].values), width=550, style={'font-size': '300%', 'color': 'blue', 'text-align': 'center'})
  #df_aux0 = df_test [df_test['SK_ID_CURR'] == int(select.value)]
  
  Col3.children[0] = Div(text=(df_aux.T).to_html(index=True), width=550)
  index_client = df_index.index(select.value)

  shap_values = explainer(normed_vec[index_client:index_client+1,:])
  
  sdf_train = pd.DataFrame({
    'feature': columns_acc,
    'shap_values': shap_values.values[:,:,1].flatten()   
  })
  
  sdf_train['shap_values_abv'] = sdf_train['shap_values'].abs()
  
  data_sv = sdf_train.sort_values(by=['shap_values_abv'], ascending = False).head(10)

  
  features =  data_sv['feature'].values 
  shap_v = data_sv['shap_values'].values

  color =[]

  for el in shap_v:
    if el > 0:
      color.append("red")
    else:
      color.append("green")

  p_shap_u = figure(y_range=FactorRange(factors=features), plot_height=250, title="shap values",toolbar_location=None, tools="")

  
  p_shap_u.hbar(y=features, right=shap_v, color=color)

  Col2.children[2] = p_shap_u



select.on_change('value', client_choisi)

select2.on_change('value', update)


Col1 = Column(Title, select, select2, expl1, description_of_variable)

Col2 = Column(Title2, proba_remb, p_shap, p_imp, create_figure())

Col3 = Column(info_of_customer)

layout = row(Col1,Col2, Col3) 

# add to document
curdoc().add_root(layout)
curdoc().title = "Dashboard"

#layout = row(Col1,Col2, Col3) 

#show(layout)











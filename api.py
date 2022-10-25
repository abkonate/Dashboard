from typing import Union
#from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from typing_extensions import Literal
from enum import Enum, IntEnum

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pandas as pd
import numpy as np

app = FastAPI()


application_test = pd.read_csv('data/application_test.csv')



discrete_var = ['CNT_CHILDREN',
                'FLAG_DOCUMENT_8',
                'FLAG_DOCUMENT_3',
                'FLAG_DOCUMENT_5',
                'FLAG_DOCUMENT_6',
                'FLAG_DOCUMENT_7',
                'FLAG_DOCUMENT_9',
                'FLAG_DOCUMENT_21',
                'FLAG_DOCUMENT_11',
                'FLAG_DOCUMENT_13',
                'FLAG_DOCUMENT_14',
                'FLAG_DOCUMENT_15',
                'FLAG_DOCUMENT_16',
                'FLAG_DOCUMENT_17',
                'FLAG_DOCUMENT_18',
                'FLAG_DOCUMENT_19',
                'FLAG_DOCUMENT_20',
                'FLAG_PHONE',
                'LIVE_CITY_NOT_WORK_CITY',
                'REG_CITY_NOT_WORK_CITY',
                'REG_CITY_NOT_LIVE_CITY',
                'LIVE_REGION_NOT_WORK_REGION',
                'REG_REGION_NOT_WORK_REGION',
                'REG_REGION_NOT_LIVE_REGION',
                'HOUR_APPR_PROCESS_START',
                'REGION_RATING_CLIENT_W_CITY',
                'REGION_RATING_CLIENT',
                'FLAG_EMAIL',
                'FLAG_CONT_MOBILE',
                'FLAG_WORK_PHONE',
                'FLAG_EMP_PHONE',
                'DAYS_ID_PUBLISH',
                'DAYS_EMPLOYED',
                'DAYS_BIRTH']


var_objet = ['EMERGENCYSTATE_MODE',
             'OCCUPATION_TYPE',
             'NAME_TYPE_SUITE',
             'NAME_CONTRACT_TYPE',
             'CODE_GENDER',
             'FLAG_OWN_CAR',
             'FLAG_OWN_REALTY',
             'WEEKDAY_APPR_PROCESS_START',
             'ORGANIZATION_TYPE',
             'NAME_FAMILY_STATUS',
             'NAME_EDUCATION_TYPE',
             'NAME_INCOME_TYPE']

continuous_data = ['FLOORSMAX_MODE',
                   'FLOORSMAX_MEDI',
                   'FLOORSMAX_AVG',
                   'YEARS_BEGINEXPLUATATION_MODE',
                   'YEARS_BEGINEXPLUATATION_MEDI',
                   'YEARS_BEGINEXPLUATATION_AVG',
                   'TOTALAREA_MODE',
                   'EXT_SOURCE_3',
                   'AMT_REQ_CREDIT_BUREAU_MON',
                   'AMT_REQ_CREDIT_BUREAU_QRT',
                   'AMT_REQ_CREDIT_BUREAU_YEAR',
                   'OBS_30_CNT_SOCIAL_CIRCLE',
                   'DEF_30_CNT_SOCIAL_CIRCLE',
                   'OBS_60_CNT_SOCIAL_CIRCLE',
                   'DEF_60_CNT_SOCIAL_CIRCLE',
                   'EXT_SOURCE_2',
                   'AMT_GOODS_PRICE',
                   'AMT_ANNUITY',
                   'CNT_FAM_MEMBERS',
                   'DAYS_LAST_PHONE_CHANGE',
                   'AMT_CREDIT',
                   'AMT_INCOME_TOTAL',
                   'DAYS_REGISTRATION',
                   'REGION_POPULATION_RELATIVE']

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


from pickle import load
from sklearn.impute import SimpleImputer as imputer

discrete_variable_trans = load(open('data/scaler_discrete.pkl', 'rb'))

con_variable_trans = load(open('data/scaler_continu.pkl', 'rb'))

object_variable_trans = load(open('data/scaler_object.pkl', 'rb'))

cat_col_transformation = {}


cat_col_transformation['EMERGENCYSTATE_MODE'] =  load(open('data/EMERGENCYSTATE_MODE.pkl', 'rb'))
cat_col_transformation['OCCUPATION_TYPE'] = load(open('data/OCCUPATION_TYPE.pkl', 'rb'))
cat_col_transformation['NAME_TYPE_SUITE'] =  load(open('data/NAME_TYPE_SUITE.pkl', 'rb'))
cat_col_transformation['NAME_CONTRACT_TYPE']=  load(open('data/NAME_CONTRACT_TYPE.pkl', 'rb'))
cat_col_transformation['CODE_GENDER'] =  load(open('data/CODE_GENDER.pkl', 'rb'))
cat_col_transformation['FLAG_OWN_CAR']= load(open('data/FLAG_OWN_CAR.pkl', 'rb'))
cat_col_transformation['FLAG_OWN_REALTY'] =  load(open('data/FLAG_OWN_REALTY.pkl', 'rb'))
cat_col_transformation['WEEKDAY_APPR_PROCESS_START'] =  load(open('data/WEEKDAY_APPR_PROCESS_START.pkl', 'rb'))
cat_col_transformation['ORGANIZATION_TYPE']=  load(open('data/ORGANIZATION_TYPE.pkl', 'rb'))
cat_col_transformation['NAME_FAMILY_STATUS']  = load(open('data/NAME_FAMILY_STATUS.pkl', 'rb'))
cat_col_transformation['NAME_EDUCATION_TYPE'] =  load(open('data/NAME_EDUCATION_TYPE.pkl', 'rb'))
cat_col_transformation['NAME_INCOME_TYPE']= load(open('data/NAME_INCOME_TYPE.pkl', 'rb'))


from sklearn.preprocessing import StandardScaler, MinMaxScaler 

scaler = load(open('data/scaler_metric.pkl', 'rb'))

from lightgbm import LGBMClassifier as lgb
import joblib


model1 =  joblib.load('data/model1.pkl')
model2 =  joblib.load('data/model2.pkl')
model3 =  joblib.load('data/model3.pkl')
model4 =  joblib.load('data/model4.pkl') 


    
@app.get("/credit/{customer_id}")
def pred(customer_id: int):

    data = application_test[ application_test['SK_ID_CURR'] == customer_id ].drop(['SK_ID_CURR'], axis = 1) 
            
    data = data[columns_acc]
            
    data[var_objet] = object_variable_trans.transform(data[var_objet])

    data[continuous_data] = con_variable_trans.transform(data[continuous_data])


    data[discrete_var] = discrete_variable_trans.transform(data[discrete_var])

    for col in var_objet:
      data[col] = cat_col_transformation[col].transform(data[col])


    data = scaler.transform(data)
        
    
    #print(data[var_objet])


    proba_estimation = (model1.predict_proba(data) + model2.predict_proba(data) +model3.predict_proba(data) +model4.predict_proba(data))/4

    #print(proba_estimation[0][1])

    return {'la probabilte du risque':  proba_estimation[0][1]}




from typing import Union
#from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from typing_extensions import Literal
from enum import Enum, IntEnum

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class CountryEnum(str, Enum):
    India = "India"
    China = "China"
    Russia = "Russia"

class FLAG_MOBIL(IntEnum):
    Yes = 1
    No  = 0

class Bar(BaseModel):
  AMT_INCOME_TOTAL:float
  AMT_CREDIT:float
  AMT_ANNUITY: float
  AMT_GOODS_PRICE: float
  REGION_POPULATION_RELATIVE: float
  DAYS_REGISTRATION: float
  OWN_CAR_AGE : float
  CNT_FAM_MEMBERS: float
  EXT_SOURCE_1: float
  EXT_SOURCE_2: float
  EXT_SOURCE_3: float
  APARTMENTS_AVG: float
  BASEMENTAREA_AVG: float
  YEARS_BEGINEXPLUATATION_AVG: float
  YEARS_BUILD_AVG: float
  COMMONAREA_AVG: float
  ELEVATORS_AVG: float
  ENTRANCES_AVG: float
  FLOORSMAX_AVG: float
  FLOORSMIN_AVG: float
  LANDAREA_AVG: float
  LIVINGAPARTMENTS_AVG: float
  LIVINGAREA_AVG: float
  NONLIVINGAPARTMENTS_AVG: float
  NONLIVINGAREA_AVG: float
  APARTMENTS_MODE: float
  BASEMENTAREA_MODE: float
  YEARS_BEGINEXPLUATATION_MODE: float
  YEARS_BUILD_MODE: float
  COMMONAREA_MODE: float
  ELEVATORS_MODE: float
  ENTRANCES_MODE: float
  FLOORSMAX_MODE: float
  FLOORSMIN_MODE: float
  LANDAREA_MODE: float
  LIVINGAPARTMENTS_MODE: float
  LIVINGAREA_MODE: float
  NONLIVINGAPARTMENTS_MODE: float
  NONLIVINGAREA_MODE: float
  APARTMENTS_MEDI: float
  BASEMENTAREA_MEDI: float
  YEARS_BEGINEXPLUATATION_MEDI: float
  YEARS_BUILD_MEDI: float
  COMMONAREA_MEDI: float
  ELEVATORS_MEDI: float
  ENTRANCES_MEDI: float
  FLOORSMAX_MEDI: float
  FLOORSMIN_MEDI: float
  LANDAREA_MEDI: float
  LIVINGAPARTMENTS_MEDI: float
  LIVINGAREA_MEDI: float
  NONLIVINGAPARTMENTS_MEDI: float
  NONLIVINGAREA_MEDI: float
  TOTALAREA_MODE: float
  OBS_30_CNT_SOCIAL_CIRCLE: float
  DEF_30_CNT_SOCIAL_CIRCLE: float
  OBS_60_CNT_SOCIAL_CIRCLE: float
  DEF_60_CNT_SOCIAL_CIRCLE: float
  DAYS_LAST_PHONE_CHANGE: float
  AMT_REQ_CREDIT_BUREAU_HOUR: float
  AMT_REQ_CREDIT_BUREAU_DAY: float
  AMT_REQ_CREDIT_BUREAU_WEEK: float
  AMT_REQ_CREDIT_BUREAU_MON : float
  AMT_REQ_CREDIT_BUREAU_QRT: float
  AMT_REQ_CREDIT_BUREAU_YEAR: float
  CNT_CHILDREN: int
  DAYS_BIRTH : int
  DAYS_EMPLOYED: int
  DAYS_ID_PUBLISH: int

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    

class FLAG_EMP_PHONE(IntEnum):
    Yes = 1
    No  = 0

class FLAG_WORK_PHONE(IntEnum):
    Yes = 1
    No  = 0

class FLAG_CONT_MOBILE(IntEnum):
    Yes = 1
    No  = 0

class FLAG_PHONE(IntEnum):
    Yes = 1
    No  = 0
    
@app.get("/emps/by-country")
def empByCountryName(countryName: CountryEnum, phone:FLAG_MOBIL, bar: Bar, item:Item, flag_phoneE:FLAG_PHONE):
    return countryName

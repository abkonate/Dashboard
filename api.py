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

class FLAG_MOBIL(IntEnum):
    Yes = 1
    No  = 0

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

class FLAG_EMAIL(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_2(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_3(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_4(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_5(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_6(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_7(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_8(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_9(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_10(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_11(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_12(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_13(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_14(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_15(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_16(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_17(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_18(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_19(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_20(IntEnum):
    Yes = 1
    No  = 0

class FLAG_DOCUMENT_21(IntEnum):
    Yes = 1
    No  = 0

class NAME_CONTRACT_TYPE(str, Enum):
    Cashloans = "Cash loans"
    Revolvingloans = "Revolving loans"
    
class CODE_GENDER(str, Enum):
    Feminin = "F"
    Maxculin = "M"

class FLAG_OWN_CAR(str, Enum):
    YES = "Y"
    NO = "N"

class FLAG_OWN_REALTY(str, Enum):
    YES = "Y"
    NO = "N"

class NAME_TYPE_SUITE(str, Enum):
    Unaccompanied = "Unaccompanied"
    Family = "Family"
    Spouse = "Spouse"
    partner = "partner"
    Groupofpeople = "Group of people"
    Other_B = "Other_B"
    Children = "Children"
    Other_A = "Other_A"

class NAME_INCOME_TYPE(str, Enum):
    Working = "Working"
    Stateservant = "State servant"
    Pensioner  = "Pensioner"
    Commercialassociate = "Commercial associate"
    Businessman = "Businessman"
    Student = "Student"
    Unemployed = "Unemployed"

class NAME_EDUCATION_TYPE(str, Enum):
    Highereducation = "Higher education"
    Secondary_secondaryspecial = "Secondary / secondary special"
    Incompletehigher = "Incomplete higher"
    Lowersecondary = "Lower secondary"
    Academicdegree ="Academic degree"

class NAME_FAMILY_STATUS(str, Enum):
    Married = "Married"
    Single_notmarried = "Single / not married"
    Civilmarriage = "Civil marriage"
    Widow = "Widow"
    Separated = "Separated"

class NAME_HOUSING_TYPE(str, Enum):
    Houseapartment = "House / apartment"
    Withparents = "With parents"
    Rentedapartment ="Rented apartment"
    Municipalapartment = "Municipal apartment"
    Officeapartment = "Office apartment"
    Co_opapartment = "Co-op apartment"

class OCCUPATION_TYPE(str, Enum):
    LowskillLaborers = "Low-skill Laborers"
    Drivers = "Drivers"
    Salesstaff = "Sales staff"
    Highskilltechstaff = "High skill tech staff"
    Corestaff = "Core staff"
    Laborers = "Laborers"
    Managers = "Managers"
    Accountants = "Accountants"
    Medicinestaff = "Medicine staff"
    Securitystaff = "Security staff"
    Privateservicestaff ="Private service staff"
    Secretaries = "Secretaries"
    Cleaningstaff = "Cleaning staff"
    Cookingstaff = "Cooking staff"
    HRstaff = "HR staff"
    Waiters_barmenstaff = "Waiters/barmen staff"
    Realtyagents = "Realty agents"
    ITstaff = "IT staff"



class WEEKDAY_APPR_PROCESS_START(str, Enum):
    TUESDAY = 'TUESDAY'
    FRIDAY = 'FRIDAY'
    MONDAY = 'MONDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'


class ORGANIZATION_TYPE(str, Enum):
    Kindergarten = "Kindergarten"
    Selfemployed = 'Self-employed'
    Transporttype3 = "Transport: type 3"
    BusinessEntityType3 = "Business Entity Type 3"
    Government = "Government"
    Industrytype9 = "Industry: type 9"
    School = "School"
    Tradetype2 = "Trade: type 2"
    XNA = "XNA"
    Services ="Services"
    Bank = "Bank"
    Industrytype3 ="Industry: type 3"
    Other = "Other"
    Tradetype6 = "Trade: type 6"
    Industrytype12 = "Industry: type 12"
    Tradetype7  = 'Trade: type 7'
    Postal = 'Postal'
    Medicine = 'Medicine'
    Housing = "Housing"
    BusinessEntityType2 = "Business Entity Type 2"
    Construction = "Construction"
    Military = "Military"
    Industrytype4 = "Industry: type 4"
    Tradetype3 = "Trade: type 3"
    LegalServices = "Legal Services"
    Security = "Security"
    Industrytype11 = "Industry: type 11"
    University = "University"
    BusinessEntityType1 = "Business Entity Type 1"
    Agriculture = 'Agriculture'
    SecurityMinistries = 'Security Ministries'
    Transporttype2 = 'Transport: type 2'
    Industrytype7 = "Industry: type 7"
    Transporttype4 = "Transport: type 4"
    Telecom = "Telecom"
    Emergency = "Emergency"
    Police = "Police"
    Industrytype1 = "Industry: type 1"
    Electricity = "Electricity"
    Industrytype5 = "Industry: type 5"
    Hotel = "Hotel"
    Restaurant = "Restaurant"
    Advertising = 'Advertising'
    Mobile = "Mobile"
    Tradetype1 = "Trade: type 1"
    Industrytype8 = "Industry: type 8"
    Realtor = "Realtor"
    Cleaning = "Cleaning"
    Industrytype2 = 'Industry: type 2'
    Tradetype4 = 'Trade: type 4'
    Industrytype6 = "Industry: type 6"
    Culture = "Culture"
    Insurance = 'Insurance'
    Religion = "Religion"
    Industrytype13 = "Industry: type 13"
    Industrytype10 = "Industry: type 10"
    Tradetype5 = "Trade: type 5"



class FONDKAPREMONT_MODE(str, Enum):
    regoperaccount = "reg oper account"
    specified = "not specified"
    orgspecaccount = "org spec account"
    regoperspecaccount = "reg oper spec account"


class HOUSETYPE_MODE(str, Enum):
    blockofflats = "block of flats"
    specifichousing = "specific housing"
    terracedhouse = "terraced house"

class WALLSMATERIAL_MODE(str, Enum):
    Stonebrick = "Stone, brick"
    Panel = "Panel"
    Block = "Block"
    Wooden = "Wooden"
    Mixed = "Mixed"
    Monolithic = "Monolithic"
    Others = "Others"

class EMERGENCYSTATE_MODE(str, Enum):
    No = "No"
    Yes = "Yes"
    
@app.get("/emps/by-country")
def empByCountryName(countryName:Union[CountryEnum,None]= None, flag_mobil:Union[FLAG_MOBIL,None]= None, flag_EMP_PHONE:Union[FLAG_EMP_PHONE,None]= None,\
                     flag_CONT_MOBILE:Union[FLAG_CONT_MOBILE,None]= None, FLAG_WORK_PHONE:Union[FLAG_WORK_PHONE,None]= None,\
                     FLAG_PHONE:Union[FLAG_PHONE,None]= None, FLAG_EMAIL:Union[FLAG_EMAIL,None]= None,\
                     FLAG_DOCUMENT_2:Union[FLAG_DOCUMENT_2,None]= None, FLAG_DOCUMENT_3:Union[FLAG_DOCUMENT_3,None]= None,\
                     FLAG_DOCUMENT_4:Union[FLAG_DOCUMENT_4,None]= None, FLAG_DOCUMENT_5:Union[FLAG_DOCUMENT_5,None]= None,\
                     FLAG_DOCUMENT_6:Union[FLAG_DOCUMENT_6,None]= None, FLAG_DOCUMENT_7:Union[FLAG_DOCUMENT_7,None]= None,\
                     FLAG_DOCUMENT_8:Union[FLAG_DOCUMENT_8,None]= None,\
                     FLAG_DOCUMENT_9:Union[FLAG_DOCUMENT_9,None]= None, FLAG_DOCUMENT_10:Union[FLAG_DOCUMENT_10,None]= None,\
                     FLAG_DOCUMENT_11:Union[FLAG_DOCUMENT_11,None]= None,\
                     FLAG_DOCUMENT_12:Union[FLAG_DOCUMENT_12,None]= None, FLAG_DOCUMENT_13:Union[FLAG_DOCUMENT_13,None]= None,\
                     FLAG_DOCUMENT_14:Union[FLAG_DOCUMENT_14,None]= None,\
                     FLAG_DOCUMENT_15:Union[FLAG_DOCUMENT_15,None]= None, FLAG_DOCUMENT_16:Union[FLAG_DOCUMENT_16,None]= None,\
                     FLAG_DOCUMENT_17:Union[FLAG_DOCUMENT_17,None]= None,\
                     FLAG_DOCUMENT_18:Union[FLAG_DOCUMENT_18,None]= None, FLAG_DOCUMENT_19:Union[FLAG_DOCUMENT_19,None]= None,\
                     FLAG_DOCUMENT_20:Union[FLAG_DOCUMENT_20,None]= None,\
                     FLAG_DOCUMENT_21:Union[FLAG_DOCUMENT_21,None]= None, NAME_TYPE_SUITE:Union[NAME_TYPE_SUITE,None]= None,\
                     NAME_INCOME_TYPE:Union[NAME_INCOME_TYPE,None]= None,\
                     NAME_CONTRACT_TYPE:Union[NAME_CONTRACT_TYPE,None]= None, CODE_GENDER:Union[CODE_GENDER,None]= None,\
                     FLAG_OWN_CAR:Union[FLAG_OWN_CAR,None]= None, FLAG_OWN_REALTY:Union[FLAG_OWN_REALTY,None]= None,\
                     NAME_EDUCATION_TYPE:Union[NAME_EDUCATION_TYPE,None]= None, NAME_FAMILY_STATUS:Union[NAME_FAMILY_STATUS,None]= None,\
                     NAME_HOUSING_TYPE:Union[NAME_HOUSING_TYPE,None]= None,\
                     OCCUPATION_TYPE:Union[OCCUPATION_TYPE,None]= None,\
                     WEEKDAY_APPR_PROCESS_START:Union[WEEKDAY_APPR_PROCESS_START,None]= None, ORGANIZATION_TYPE:Union[ORGANIZATION_TYPE,None]= None,\
                     FONDKAPREMONT_MODE:Union[FONDKAPREMONT_MODE,None]= None,\
                     HOUSETYPE_MODE:Union[HOUSETYPE_MODE,None]= None, WALLSMATERIAL_MODE:Union[WALLSMATERIAL_MODE,None]= None,\
                     EMERGENCYSTATE_MODE:Union[EMERGENCYSTATE_MODE,None]= None,\
                     AMT_INCOME_TOTAL: Union[float, None] = None, AMT_CREDIT:Union[float, None] = None, AMT_ANNUITY: Union[float, None] = None,\
                     AMT_GOODS_PRICE: Union[float, None] = None, REGION_POPULATION_RELATIVE: Union[float, None] = None,\
                     DAYS_REGISTRATION: Union[float, None] = None,   OWN_CAR_AGE : Union[float, None] = None, CNT_FAM_MEMBERS: Union[float, None] = None,\
                     EXT_SOURCE_1: Union[float, None] = None, EXT_SOURCE_2: Union[float, None] = None,\
                     EXT_SOURCE_3: Union[float, None] = None, APARTMENTS_AVG: Union[float, None] = None, BASEMENTAREA_AVG: Union[float, None] = None,
                     YEARS_BEGINEXPLUATATION_AVG: Union[float, None] = None, YEARS_BUILD_AVG: Union[float, None] = None,\
                     COMMONAREA_AVG: Union[float, None] = None, ELEVATORS_AVG: Union[float, None] = None, ENTRANCES_AVG: Union[float, None] = None,\
                     FLOORSMAX_AVG: Union[float, None] = None, FLOORSMIN_AVG: Union[float, None] = None, LANDAREA_AVG: Union[float, None] = None,\
                     LIVINGAPARTMENTS_AVG: Union[float, None] = None, LIVINGAREA_AVG: Union[float, None] = None, NONLIVINGAPARTMENTS_AVG: Union[float, None] = None,\
                     NONLIVINGAREA_AVG: Union[float, None] = None, APARTMENTS_MODE: Union[float, None] = None,\
                     BASEMENTAREA_MODE: Union[float, None] = None, YEARS_BEGINEXPLUATATION_MODE: Union[float, None] = None,\
                     YEARS_BUILD_MODE: Union[float, None] = None, COMMONAREA_MODE: Union[float, None] = None, ELEVATORS_MODE: Union[float, None] = None,\
                     ENTRANCES_MODE: Union[float, None] = None, FLOORSMAX_MODE: Union[float, None] = None, FLOORSMIN_MODE: Union[float, None] = None,\
                     LANDAREA_MODE: Union[float, None] = None, LIVINGAPARTMENTS_MODE: Union[float, None] = None, LIVINGAREA_MODE: Union[float, None] = None,\
                     NONLIVINGAPARTMENTS_MODE: Union[float, None] = None, NONLIVINGAREA_MODE: Union[float, None] = None,\
                     APARTMENTS_MEDI: Union[float, None] = None, BASEMENTAREA_MEDI: Union[float, None] = None,\
                     YEARS_BEGINEXPLUATATION_MEDI: Union[float, None] = None, YEARS_BUILD_MEDI: Union[float, None] = None,\
                     COMMONAREA_MEDI: Union[float, None] = None, ELEVATORS_MEDI: Union[float, None] = None, ENTRANCES_MEDI: Union[float, None] = None,\
                     FLOORSMAX_MEDI: Union[float, None] = None, FLOORSMIN_MEDI: Union[float, None] = None, LANDAREA_MEDI: Union[float, None] = None,\
                     LIVINGAPARTMENTS_MEDI: Union[float, None] = None, LIVINGAREA_MEDI: Union[float, None] = None,\
                     NONLIVINGAPARTMENTS_MEDI: Union[float, None] = None, NONLIVINGAREA_MEDI: Union[float, None] = None,\
                     TOTALAREA_MODE: Union[float, None] = None, OBS_30_CNT_SOCIAL_CIRCLE: Union[float, None] = None,\
                     DEF_30_CNT_SOCIAL_CIRCLE: Union[float, None] = None, OBS_60_CNT_SOCIAL_CIRCLE: Union[float, None] = None,\
                     DEF_60_CNT_SOCIAL_CIRCLE: Union[float, None] = None,DAYS_LAST_PHONE_CHANGE: Union[float, None] = None,\
                     AMT_REQ_CREDIT_BUREAU_HOUR: Union[float, None] = None, AMT_REQ_CREDIT_BUREAU_DAY: Union[float, None] = None,\
                     AMT_REQ_CREDIT_BUREAU_WEEK: Union[float, None] = None, AMT_REQ_CREDIT_BUREAU_MON : Union[float, None] = None,\
                     AMT_REQ_CREDIT_BUREAU_QRT: Union[float, None] = None, AMT_REQ_CREDIT_BUREAU_YEAR: Union[float, None] = None,\
                     CNT_CHILDREN: Union[int, None] = None, DAYS_BIRTH : Union[int, None] = None,\
                     DAYS_EMPLOYED: Union[int, None] = None, DAYS_ID_PUBLISH: Union[int, None] = None 
                     ):
    return {"countryName":countryName, "FLAG_MOBIL":flag_mobil, "FLAG_WORK_PHONE":FLAG_WORK_PHONE, "FLAG_PHONE":FLAG_PHONE, "FLAG_EMAIL":FLAG_EMAIL,\
                     "FLAG_DOCUMENT_2":FLAG_DOCUMENT_2, "FLAG_DOCUMENT_3":FLAG_DOCUMENT_3,\
                     "FLAG_DOCUMENT_4":FLAG_DOCUMENT_4, "FLAG_DOCUMENT_5":FLAG_DOCUMENT_5,\
                     "FLAG_DOCUMENT_6":FLAG_DOCUMENT_6, "FLAG_DOCUMENT_7":FLAG_DOCUMENT_7, "FLAG_DOCUMENT_8":FLAG_DOCUMENT_8,\
                     "FLAG_DOCUMENT_9":FLAG_DOCUMENT_9, "FLAG_DOCUMENT_10":FLAG_DOCUMENT_10, "FLAG_DOCUMENT_11":FLAG_DOCUMENT_11,\
                     "FLAG_DOCUMENT_12":FLAG_DOCUMENT_12, "FLAG_DOCUMENT_13":FLAG_DOCUMENT_13, "FLAG_DOCUMENT_14":FLAG_DOCUMENT_14,\
                     "FLAG_DOCUMENT_15":FLAG_DOCUMENT_15, "FLAG_DOCUMENT_16":FLAG_DOCUMENT_16, "FLAG_DOCUMENT_17":FLAG_DOCUMENT_17,\
                     "FLAG_DOCUMENT_18":FLAG_DOCUMENT_18, "FLAG_DOCUMENT_19":FLAG_DOCUMENT_19, "FLAG_DOCUMENT_20":FLAG_DOCUMENT_20,\
                     "FLAG_DOCUMENT_21":FLAG_DOCUMENT_21, "NAME_TYPE_SUITE":NAME_TYPE_SUITE, "NAME_INCOME_TYPE":NAME_INCOME_TYPE,\
                     "NAME_CONTRACT_TYPE":NAME_CONTRACT_TYPE, "CODE_GENDER":CODE_GENDER, "FLAG_OWN_CAR":FLAG_OWN_CAR, "FLAG_OWN_REALTY":FLAG_OWN_REALTY,\
                     "NAME_EDUCATION_TYPE":NAME_EDUCATION_TYPE,"NAME_FAMILY_STATUS":NAME_FAMILY_STATUS, "NAME_HOUSING_TYPE":NAME_HOUSING_TYPE,\
                     "OCCUPATION_TYPE":OCCUPATION_TYPE,\
                     "WEEKDAY_APPR_PROCESS_START":WEEKDAY_APPR_PROCESS_START, "ORGANIZATION_TYPE":ORGANIZATION_TYPE, "FONDKAPREMONT_MODE":FONDKAPREMONT_MODE,\
                     "HOUSETYPE_MODE":HOUSETYPE_MODE, "WALLSMATERIAL_MODE":WALLSMATERIAL_MODE, "EMERGENCYSTATE_MODE":EMERGENCYSTATE_MODE}

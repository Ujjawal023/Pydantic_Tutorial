from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated


#create pydantic model and defined schema
class Patient(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    married: bool
    allergies: Optional[List[str]] = None #if patient not define allergies then show None
    contact_details: Dict[str, str]

#create field Validator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should be in between 0 and 100')

#Function
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

#Dict
patient_info = {'name':'nitish', 'age':'30', 'email':'abc@hdfc.com', 'weight': 75.2, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'phone': '7894562123'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
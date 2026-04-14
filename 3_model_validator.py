from pydantic import BaseModel, model_validator
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

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

#Function
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

#Dict
patient_info = {'name':'nitish', 'age':70, 'email':'abc@gmail.com', 'weight': 75.2, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'phone': '7894562123', 'emergency': '51894891684'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
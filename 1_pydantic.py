from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated


#create pydantic model and defined schema
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Optional[List[str]] = None #if patient not define allergies then show None
    contact_details: Dict[str, str]

#Function
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

#Dict
patient_info = {'name': 'nitish', 'age': '30', 'weight': 75.2, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone': '7894562123'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
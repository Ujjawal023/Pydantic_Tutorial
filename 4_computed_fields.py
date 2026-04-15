from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated


#create pydantic model and defined schema
class Patient(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    height: float
    married: bool
    allergies: Optional[List[str]] = None #if patient not define allergies then show None
    contact_details: Dict[str, str]

 
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


#Function
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('BMI', patient.calculate_bmi)
    print('Inserted')

#Dict
patient_info = {'name':'nitish', 'age':65, 'email':'abc@gmail.com', 'weight': 75.2, 'height':1.72, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'phone': '7894562123'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
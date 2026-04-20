from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

addresss_dict = {
    'city': 'gurgaon',
    'state': 'haryana',
    'pin': '122001'
}

address1 = Address(**addresss_dict)

patient_dict = {
    'name': 'Nitish',
    'gender': 'male',
    'age': 34,
    'address': address1
}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  #pydantic model object convert into Dict

temp1 = patient1.model_dump(include=['name'])
temp1 = patient1.model_dump(exclude=['gender'])

temp2 = patient1.model_dump_json()  #pydantic model object convert into JSON but python has received in str


print(temp)
print(type(temp))  

print(temp2)
print(type(temp2))

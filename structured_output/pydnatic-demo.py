from pydantic import BaseModel

class student(BaseModel):
    name:str 
    age:int


new_student={'name':'John Doe', 'age':30}
student1=student(name='John Doe', age=30)

print(new_student)
print(student1)
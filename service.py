from model import PersonModel

class PersonService:

    def __init__(self):
        self.personArray = []

    def addPerson(self):
        pm = PersonModel()
        print("Enter the name : ")
        pm.name = input()

        print("Enter the age : ")
        age = int(input())
        if self.validatePersonage(age) == True:
            pm.age = age
        else:
            print("Invalid age! ")

        print("Enter the work : ")
        pm.work = input()
        self.personArray.append(pm)

    def validatePersonage(self, age):
        if age >= 1 and age <= 100:
            return True
        else:
            return False
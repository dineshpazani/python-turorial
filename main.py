
from service import PersonService

def main():
    print("Program starting!")

    po = PersonService()
    print("Enter no of the persons : ")
    no = int(input())
    for i in range(0, no):
        po.addPerson()

    for p in po.personArray:
        print(p.name, ": ", p.age, ":", p.work)


if __name__ == "__main__":
    main()

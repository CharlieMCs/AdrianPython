from PeopleA import People

class Student(People):
    def __init__(self, paramName: str, paramSurname: str, paramRole: str):
        super().__init__(paramName, paramSurname, paramRole)
        
    def takingNotes(self):
        print("The student has taken his notebook, they are ready study")

    def presentationTime(self):
        print("the student is getting ready for the upcoming presentation")
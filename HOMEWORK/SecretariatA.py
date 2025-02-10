from PeopleA import People

class Secretariat(People):
    def __init__(self, paramName: str, paramSurname: str, paramRole: str):
        super().__init__(paramName, paramSurname, paramRole)

    def organizeSchedule(self):
        print("The Secretariat has started organizing the Professors Scehedules for the rest of the week")
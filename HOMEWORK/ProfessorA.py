from PeopleA import People

class Professor(People):
    def __init__(self, paramName: str, paramSurname: str, paramRole: str):
        super().__init__(paramName, paramSurname, paramRole)

    def startClass(self):
        print("The Professor is ready to start the first class of the day")

    def gradingTasks(self):
        print("The Professor is qualifying the students tasks")
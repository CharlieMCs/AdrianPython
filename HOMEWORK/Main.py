from StudentA import Student
from ProfessorA import Professor
from SecretariatA import Secretariat
from PeopleA import People

Professor = Professor("Jhon", "Sylvester", "Professor")
print(Professor)
Professor.startClass()

Student = Student("Charles", "Darwin", "Student")
print(Student)
Student.takingNotes()

Secretariat = Secretariat("Hannah", "Sylvester", "Secretariat")
print(Secretariat)
Secretariat.shiftOn()
Secretariat.organizeSchedule()
Secretariat.shiftOff()
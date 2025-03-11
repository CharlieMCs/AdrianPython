class Persona:
    def __init__(self, name, surname, ide, pic, email, password, age):
        self.__name = name
        self.__surname = surname
        self.__ide = ide
        self.__pic = pic
        self.__email = email
        self.__password = password
        self.__age = age

#Getters
    def getName(self):
        return self.__name
    
    def getSurname(self):
        return self.__surname
    
    def getIde(self):
        return self.__ide
    
    def getPic(self):
        return self.__pic
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def getAge(self):
        return self.__age
    
#Settersn methods
    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname

    def setIde(self, ide):
        self.__ide = ide

    def setPic(self, pic):
        self.__pic = pic

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        if len(password) >= 8:
            self.__password = password
        else:
            print("The password must have at least 8 characters")

    def setAge(self, age):
        if age >= 18:
            self.__age = age
        else:
            print("You need to have 18 years to sign up")

#str
    def __str__(self):
        return f"Nombre: {self.__name}, Edad: {self.__age}, Correo: {self.__email}"

#Log in static method
    @staticmethod
    def log_in(email, password, users):
        user = email(email, password, users)
        if user:
            return ("Login successful", user)
        else:
            return ("Login failed", None)
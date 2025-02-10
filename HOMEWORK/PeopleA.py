class People:
    def __init__(self, paramName: str, paramSurname: str, paramRole: str):
        self.paramName = paramName
        self.paramSurname = paramSurname
        self.paramRole = paramRole

    def shiftOn (self):
        print(f"The {self.paramRole}, has started their shift")

    def lunchTime (self):
        print(f"The {self.paramRole}, is now taking lunch")

    def shiftOff (self):
        print(f"The {self.paramRole}, has finished their shift")

    def __str__(self):
        return f"""
        The person {self.paramName} is the {self.paramRole} of the HighSchool
        """
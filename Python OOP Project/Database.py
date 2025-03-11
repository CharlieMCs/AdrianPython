from Persona import Persona

users = [
    Persona("Leon", "Charles", "001", "foto1.png", "leon@gmail.com", "123", 25),
    Persona("Maria", "Gomez", "002", "foto2.png", "maria@gmail.com", "456", 30),
    Persona("Carlos", "Ramirez", "003", "foto3.png", "carlos@gmail.com", "password789", 28)
]

# Guardar en el archivo Database.txt
def saveUsers():
    with open("Database.txt", "w") as archivo:
        for user in users:
            line = f"{user.getName()},{user.getSurname()},{user.getIde()},{user.getPic()},{user.getEmail()},{user.getPassword()},{user.getAge()}\n"
            archivo.write(line)

def read_database():
    users = []
    try:
        with open("Database.txt", "r") as archivo:
            for line in archivo:
                name, surname, ide, pic, email, password, age = line.strip().split(',')
                user = Persona(name, surname, ide, pic, email, password, int(age))
                users.append(user)
    except FileNotFoundError:
        print("Database file not found.")
    return users
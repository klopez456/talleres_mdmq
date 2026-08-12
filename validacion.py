#Funcion para validar cédula sea 10 digitos numericos
def validar_cedula(cedula):
    if len(cedula) == 10 and cedula.isdigit():
        return True
    else:
        return False

#Función para validar nombre y apellido que sean solo letras y espacios 
def validar_nombre(nombre):
    if nombre.replace(" ", "").isalpha():
        return True
    else:
        return False
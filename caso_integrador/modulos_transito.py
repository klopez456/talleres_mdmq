import re

# Valida que una placa vehicular tenga el formato correcto.
# Debe contener 3 letras, un guion y 3 o 4 números (Ej: PBA-1234 o ABC-123).
# Recibe str y devuelve bool.
# Devuelve False si es None, si está vacía o si tiene caracteres especiales no permitidos.
def validar_placa(placa: str) -> bool:
    if not isinstance(placa, str):
        return False
    
    patron = r'^[A-Z]{3}-\d{3,4}$'
    if re.match(patron, placa):
        return True
    return False


# Asigna el mes correspondiente para la revisión técnica según el último dígito de la placa.
# Basado en el esquema de calendarización estándar:
# 1 -> Febrero, 2 -> Marzo, ..., 9 -> Octubre, 0 -> Noviembre.
# Lanza ValueError si la placa no es válida.
def asignar_mes_revision(placa: str) -> str:
    if not validar_placa(placa):
        raise ValueError("Placa invalida, no se puede asignar mes.")
    
    ultimo_digito = placa[-1]
    
    meses_calendarizacion = {
        '1': 'Febrero', '2': 'Marzo', '3': 'Abril', 
        '4': 'Mayo', '5': 'Junio', '6': 'Julio', 
        '7': 'Agosto', '8': 'Septiembre', '9': 'Octubre', 
        '0': 'Noviembre'
    }
    
    return meses_calendarizacion.get(ultimo_digito, "Desconocido")


# Calcula el valor de la multa por no presentarse en el mes de calendarización.
# Recibe el número del mes asignado (1 a 12) y el número del mes en que asiste (1 a 12).
# Si el mes de asistencia es mayor al asignado, devuelve 50.0. Caso contrario, 0.0.
# Lanza ValueError si los meses están fuera del rango 1-12.
def calcular_multa(mes_asignado: int, mes_asistencia: int) -> float:
    if not (1 <= mes_asignado <= 12) or not (1 <= mes_asistencia <= 12):
        raise ValueError("Los meses deben estar en el rango de 1 a 12.")
    
    if mes_asistencia > mes_asignado:
        return 50.0
    
    return 0.0


# Evalúa los resultados de las pruebas físicas del vehículo en el centro de revisión.
# Recibe la placa y el estado (True = pasa, False = falla) de gases, frenos y luces.
# Si pasa todas, devuelve aprobado True. Si falla alguna, devuelve False y la lista de fallos.
def estado_revision(placa: str, gases: bool, frenos: bool, luces: bool) -> dict:
    fallos = []
    
    if not gases:
        fallos.append("Emision de gases")
    if not frenos:
        fallos.append("Sistema de frenos")
    if not luces:
        fallos.append("Sistema de luces")
        
    if len(fallos) == 0:
        return {
            "placa": placa,
            "aprobado": True,
            "detalles": "Revision exitosa"
        }
    else:
        return {
            "placa": placa,
            "aprobado": False,
            "fallos_detectados": fallos
        }
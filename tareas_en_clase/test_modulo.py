import pytest    
from tramites import calcular_promedio, clasificar_tiempo, resumen_diario, validar_cedula, validar_fecha

# Generar una prueba unitaria para el módulo de trámites.
# Se debe probar la función validar_cedula con varios casos de prueba.
# en base a la siguiente tabla de equivalencia:
#| ID | Función | Tipo | Entrada | Resultado esperado |
#| CC-01 | `validar_cedula` | Normal | `"0923456789"` | Devuelve `True`. Tiene exactamente 10 dígitos. |
#| CC-02 | `validar_cedula` | Límite | `"123456789"` | Devuelve `False`. Tiene 9 dígitos, uno menos del mínimo requerido. |
#| CC-03 | `validar_cedula` | Error | `None` | Devuelve `False` sin lanzar excepción. |

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios normales (cédulas válidas de 10 dígitos).
@pytest.mark.parametrize("cedula", [
    "0923456789",
    "1234567890",
    "9876543210"
])
def test_validar_cedula_normal(cedula):
    assert validar_cedula(cedula) is True


# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios límite (cédulas con 9 dígitos, 11 dígitos o vacías).
@pytest.mark.parametrize("cedula", [
    "123456789",  # 9 dígitos
    "12345678901",  # 11 dígitos
    ""  # cadena vacía
])
def test_validar_cedula_limite(cedula):
    assert validar_cedula(cedula) is False

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios de error (valores nulos, booleanos o tipos de datos incorrectos).
@pytest.mark.parametrize("cedula", [
    None,
    True,
    False
])
def test_validar_cedula_error(cedula):
    assert validar_cedula(cedula) is False


# Generar una prueba unitaria para el módulo de trámites.
# Se debe probar la función validar_fecha con varios casos de prueba.
# en base a la siguiente tabla de equivalencia:
#| ID | Función | Tipo | Entrada | Resultado esperado |
#| CF-01 | `validar_fecha` | Normal | `"05/08/2026"` | Devuelve `True`. La fecha tiene formato válido y existe. |
#| CF-02 | `validar_fecha` | Límite | `"29/02/2024"` | Devuelve `True`. Es el último día válido de febrero en un año bisiesto. |
#| CF-03 | `validar_fecha` | Error | `"31/02/2026"` | Devuelve `False`. La fecha no existe. |

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios normales (fechas válidas en formato DD/MM/YYYY que devuelvan True).
@pytest.mark.parametrize("fecha", [
    "05/08/2026",   
    "04/08/2026",   
    "03/08/2026"   
])
def test_validar_fecha_normal(fecha):
    assert validar_fecha(fecha) is True

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios límite (fechas de años bisiestos o fines de mes que devuelvan True).
@pytest.mark.parametrize("fecha", [
    "29/02/2024",  # Último día válido de febrero en un año bisiesto
    "31/01/2026",  # Último día de enero
    "30/04/2026"   # Último día de abril
])
def test_validar_fecha_limite(fecha):
    assert validar_fecha(fecha) is True

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios de error (fechas inexistentes o mal formateadas que devuelvan False).
@pytest.mark.parametrize("fecha", [
    "31/02/2026",  # Fecha inexistente
    "31/04/2026",  # Fecha inexistente
    "31/06/2026"   # Fecha inexistente
])
def test_validar_fecha_error(fecha):
    assert validar_fecha(fecha) is False


# Generar una prueba unitaria para el módulo de trámites.
# Se debe probar la función clasificar_tiempo con varios casos de prueba.
# en base a la siguiente tabla de equivalencia:
#| ID | Función | Tipo | Entrada | Resultado esperado |
#| CT-01 | `clasificar_tiempo` | Normal | `20` | Devuelve `"Normal"`. Está entre 11 y 30 minutos. |
#| CT-02 | `clasificar_tiempo` | Límite | `10` | Devuelve `"Ágil"`. Es el límite superior de la categoría ágil. |
#| CT-03 | `clasificar_tiempo` | Error | `-1` | Lanza `ValueError` con el mensaje `"El tiempo no puede ser negativo"`. |

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios normales (tiempos intermedios y sus resultados esperados en texto).
@pytest.mark.parametrize("tiempo, esperado", [
    (20, "Normal"),
    (15, "Normal"),
    (30, "Normal")
])
def test_clasificar_tiempo_normal(tiempo, esperado):
    assert clasificar_tiempo(tiempo) == esperado

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios límite (tiempos de frontera para la categoría Ágil).
@pytest.mark.parametrize("tiempo, esperado", [
    (10, "Ágil"),
    (0, "Ágil"),
    (5, "Ágil")
])
def test_clasificar_tiempo_limite(tiempo, esperado):
    assert clasificar_tiempo(tiempo) == esperado

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios de error (valores negativos que deben lanzar ValueError).
@pytest.mark.parametrize("tiempo, mensaje", [
    (-1, "El tiempo no puede ser negativo"),
    (-10, "El tiempo no puede ser negativo"),
    (-100, "El tiempo no puede ser negativo")
])
def test_clasificar_tiempo_error(tiempo, mensaje):
    with pytest.raises(ValueError) as excinfo:
        clasificar_tiempo(tiempo)
    assert str(excinfo.value) == mensaje

# Generar una prueba unitaria para el módulo de trámites.
# Se debe probar la función calcular_promedio con varios casos de prueba.
# en base a la siguiente tabla de equivalencia:
#| ID | Función | Tipo | Entrada | Resultado esperado |
#| CP-01 | `calcular_promedio` | Normal | `[10, 20, 31]` | Devuelve `20.33`, redondeado a dos decimales. |
#| CP-02 | `calcular_promedio` | Límite | `[]` | Devuelve `0.0` sin lanzar excepción. |
#| CP-03 | `calcular_promedio` | Error | `[10, "20"]` | Lanza `TypeError` porque no se pueden sumar enteros y cadenas. |

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios normales (listas de números y el promedio esperado).
@pytest.mark.parametrize("lista_tiempos, esperado", [
    ([10, 20, 31], 20.33),
    ([0, 0, 0], 0.0),
    ([5, 15, 25], 15.0)
])
def test_calcular_promedio_normal(lista_tiempos, esperado):
    assert calcular_promedio(lista_tiempos) == esperado

# Crear datos de prueba con completions inline usando @pytest.mark.parametrize.
# Generar 3 escenarios límite (listas vacías o con un solo número).
@pytest.mark.parametrize("lista_tiempos, esperado", [
    ([], 0.0),
    ([10], 10.0),
    ([5], 5.0)
])
def test_calcular_promedio_limite(lista_tiempos, esperado):
    assert calcular_promedio(lista_tiempos) == esperado


@pytest.mark.parametrize("lista_tiempos, mensaje", [
    ([10, "20"], "unsupported operand type(s) for +: 'int' and 'str'"),
    ([5, None], "unsupported operand type(s) for +: 'int' and 'NoneType'"),
    ([1, [2]], "unsupported operand type(s) for +: 'int' and 'list'")
])
def test_calcular_promedio_error(lista_tiempos, mensaje):
    with pytest.raises(TypeError) as excinfo:
        calcular_promedio(lista_tiempos)
    assert str(excinfo.value) == mensaje

# Generar una prueba unitaria para el módulo de trámites.
# Se debe probar la función resumen_diario con varios casos de prueba.
# en base a la siguiente tabla de equivalencia:
#| ID | Función | Tipo | Entrada | Resultado esperado |
#| RD-01 | `resumen_diario` | Normal | `[{"cedula": "0923456789", "fecha": "05/08/2026", "minutos": 10}, {"cedula": "0912345678", "fecha": "06/08/2026", "minutos": 31}]` | Devuelve `{"total": 2, "descartados": 0, "promedio": 20.5, "conteo_categoria": {"Ágil": 1, "Normal": 0, "Demorada": 1}}`. |
#| RD-02 | `resumen_diario` | Límite | `[]` | Devuelve `{"total": 0, "descartados": 0, "promedio": 0.0, "conteo_categoria": {"Ágil": 0, "Normal": 0, "Demorada": 0}}`. |
#| RD-03 | `resumen_diario` | Error | `[{"cedula": "0923456789", "fecha": "05/08/2026", "minutos": -1}]` | Descarta el registro y devuelve `total = 0`, `descartados = 1`, `promedio = 0.0`; no lanza excepción. |
def test_resumen_diario_normal():
    registros = [
        {"cedula": "0923456789", "fecha": "05/08/2026", "minutos": 10},
        {"cedula": "0912345678", "fecha": "06/08/2026", "minutos": 31}
    ]
    resultado = resumen_diario(registros)
    assert resultado == {
        "total": 2,
        "descartados": 0,
        "promedio": 20.5,
        "conteo_categoria": {"Ágil": 1, "Normal": 0, "Demorada": 1}
    }

def test_resumen_diario_limite():
    registros = []
    resultado = resumen_diario(registros)
    assert resultado == {
        "total": 0,
        "descartados": 0,
        "promedio": 0.0,
        "conteo_categoria": {"Ágil": 0, "Normal": 0, "Demorada": 0}
    }

def test_resumen_diario_error():
    registros = [
        {"cedula": "0923456789", "fecha": "05/08/2026", "minutos": -1}
    ]
    resultado = resumen_diario(registros)
    assert resultado == {
        "total": 0,
        "descartados": 1,
        "promedio": 0.0,
        "conteo_categoria": {"Ágil": 0, "Normal": 0, "Demorada": 0}
    }

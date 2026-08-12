import pytest
from modulos_transito import validar_placa, asignar_mes_revision, calcular_multa, estado_revision

# ==========================================
# Pruebas para validar_placa
# ==========================================

# Generar escenarios normales (placas con formato correcto de 3 letras mayúsculas, guion y 3 o 4 números)
@pytest.mark.parametrize("placa", [
    "PBA-1234",
    "ABC-123",
    "XYZ-9999"
])
def test_validar_placa_normal(placa):
    assert validar_placa(placa) is True

# Generar escenarios límite (placas con números muy bajos o el máximo de caracteres)
@pytest.mark.parametrize("placa", [
    "AAA-000",
    "ZZZ-0000"
])
def test_validar_placa_limite(placa):
    assert validar_placa(placa) is True

# Generar escenarios de error (minúsculas, sin guion, formato incorrecto, o tipos de dato inválidos)
@pytest.mark.parametrize("placa", [
    "pba-1234",   # Minúsculas
    "PB-1234",    # Solo 2 letras
    "PBA-12",     # Solo 2 números
    "PBA1234",    # Sin guion
    1234567,      # Número entero en lugar de string
    None          # Valor nulo
])
def test_validar_placa_error(placa):
    assert validar_placa(placa) is False


# ==========================================
# Pruebas para asignar_mes_revision
# ==========================================

# Generar escenarios normales (asigna correctamente el mes según el último dígito)
@pytest.mark.parametrize("placa, mes_esperado", [
    ("PBA-1231", "Febrero"),
    ("ABC-1235", "Junio"),
    ("XYZ-9999", "Octubre")
])
def test_asignar_mes_revision_normal(placa, mes_esperado):
    assert asignar_mes_revision(placa) == mes_esperado

# Generar escenarios límite (dígito 0 que corresponde a Noviembre, el último mes)
@pytest.mark.parametrize("placa, mes_esperado", [
    ("AAA-0000", "Noviembre")
])
def test_asignar_mes_revision_limite(placa, mes_esperado):
    assert asignar_mes_revision(placa) == mes_esperado

# Generar escenarios de error (placa invalida lanza ValueError)
@pytest.mark.parametrize("placa, mensaje", [
    ("PBA-12", "Placa invalida, no se puede asignar mes."),
    (None, "Placa invalida, no se puede asignar mes.")
])
def test_asignar_mes_revision_error(placa, mensaje):
    try:
        asignar_mes_revision(placa)
        assert False, "Se esperaba un ValueError"
    except ValueError as e:
        assert str(e) == mensaje


# ==========================================
# Pruebas para calcular_multa
# ==========================================

# Generar escenarios normales (asiste a tiempo = 0.0, asiste tarde = 50.0)
@pytest.mark.parametrize("mes_asignado, mes_asistencia, multa_esperada", [
    (2, 2, 0.0),   # A tiempo (Febrero)
    (5, 4, 0.0),   # Asiste un mes antes (Abril)
    (2, 3, 50.0)   # Asiste un mes tarde (Marzo)
])
def test_calcular_multa_normal(mes_asignado, mes_asistencia, multa_esperada):
    assert calcular_multa(mes_asignado, mes_asistencia) == multa_esperada

# Generar escenarios límite (inicios y fines de año)
@pytest.mark.parametrize("mes_asignado, mes_asistencia, multa_esperada", [
    (12, 12, 0.0), # Límite superior a tiempo
    (1, 12, 50.0)  # Debería ir en Enero, va en Diciembre
])
def test_calcular_multa_limite(mes_asignado, mes_asistencia, multa_esperada):
    assert calcular_multa(mes_asignado, mes_asistencia) == multa_esperada

# Generar escenarios de error (meses fuera del rango 1-12)
@pytest.mark.parametrize("mes_asignado, mes_asistencia", [
    (13, 2),
    (2, 0),
    (-1, 5)
])
def test_calcular_multa_error(mes_asignado, mes_asistencia):
    try:
        calcular_multa(mes_asignado, mes_asistencia)
        assert False, "Se esperaba un ValueError"
    except ValueError as e:
        assert str(e) == "Los meses deben estar en el rango de 1 a 12."


# ==========================================
# Pruebas para estado_revision
# ==========================================

# Generar escenarios normales (vehículo aprueba todo)
@pytest.mark.parametrize("placa, gases, frenos, luces", [
    ("PBA-1234", True, True, True)
])
def test_estado_revision_aprobado(placa, gases, frenos, luces):
    resultado = estado_revision(placa, gases, frenos, luces)
    assert resultado["aprobado"] is True
    assert resultado["detalles"] == "Revision exitosa"

# Generar escenarios de falla parcial (falla una sola prueba)
@pytest.mark.parametrize("placa, gases, frenos, luces, fallo_esperado", [
    ("PBA-1234", False, True, True, "Emision de gases"),
    ("ABC-123", True, False, True, "Sistema de frenos"),
    ("XYZ-9999", True, True, False, "Sistema de luces")
])
def test_estado_revision_falla_parcial(placa, gases, frenos, luces, fallo_esperado):
    resultado = estado_revision(placa, gases, frenos, luces)
    assert resultado["aprobado"] is False
    assert fallo_esperado in resultado["fallos_detectados"]
    assert len(resultado["fallos_detectados"]) == 1

# Generar escenarios de límite (falla absolutamente todas las pruebas)
@pytest.mark.parametrize("placa, gases, frenos, luces", [
    ("ZZZ-0000", False, False, False)
])
def test_estado_revision_falla_total(placa, gases, frenos, luces):
    resultado = estado_revision(placa, gases, frenos, luces)
    assert resultado["aprobado"] is False
    assert len(resultado["fallos_detectados"]) == 3
    assert "Emision de gases" in resultado["fallos_detectados"]
    assert "Sistema de frenos" in resultado["fallos_detectados"]
    assert "Sistema de luces" in resultado["fallos_detectados"]
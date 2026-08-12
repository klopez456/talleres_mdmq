**Resumen**
- **Descripción**: Este directorio contiene el módulo `modulos_transito.py` con funciones para validar placas, asignar el mes de revisión técnica, calcular multas y evaluar el estado de revisión del vehículo. Las pruebas están en `test_modulos_transito.py` y cubren casos normales, límites y de error para cada función.

**Archivos**
- **Código**: [modulos_transito.py](caso_integrador/modulos_transito.py)
- **Pruebas**: [test_modulos_transito.py](caso_integrador/test_modulos_transito.py)

**Funciones en `modulos_transito.py`**

- **`validar_placa(placa: str) -> bool`**:
  - **Entrada**: `placa` (string esperado en formato `AAA-123` o `AAA-1234`).
  - **Salida**: `True` si cumple el patrón, `False` en otro caso.
  - **Qué hace**: Verifica que `placa` sea `str` y que coincida con la expresión regular `^[A-Z]{3}-\d{3,4}$` (tres letras mayúsculas, guion, 3 o 4 dígitos).
  - **Casos especiales**: Devuelve `False` para `None`, para enteros u otros tipos no-`str`, para minúsculas o formatos sin guion.

- **`asignar_mes_revision(placa: str) -> str`**:
  - **Entrada**: `placa` válida.
  - **Salida**: nombre del mes asignado (`'Febrero'`, `'Marzo'`, ..., `'Noviembre'`).
  - **Qué hace**: Si la placa es válida, toma el último carácter (dígito) y lo mapea al mes de calendarización según el esquema documentado (1 -> Febrero, ..., 0 -> Noviembre). Si la placa no es válida, lanza `ValueError` con mensaje `"Placa invalida, no se puede asignar mes."`.
  - **Casos especiales**: Si por alguna razón el último carácter no existe o no está en el mapeo, la función devuelve `'Desconocido'` (pero el diseño actual evita ese caso validando la placa primero).

- **`calcular_multa(mes_asignado: int, mes_asistencia: int) -> float`**:
  - **Entrada**: dos enteros entre 1 y 12.
  - **Salida**: `50.0` si `mes_asistencia > mes_asignado`, en caso contrario `0.0`.
  - **Qué hace**: Valida que ambos meses estén en el rango 1..12; si no, lanza `ValueError("Los meses deben estar en el rango de 1 a 12.")`.
  - **Casos especiales**: No contempla diferencias por más de un año (se compara numéricamente las etiquetas de mes tal como vienen en las pruebas).

- **`estado_revision(placa: str, gases: bool, frenos: bool, luces: bool) -> dict`**:
  - **Entrada**: `placa` (string) y tres booleanos que indican si cada prueba pasó.
  - **Salida**: si no hay fallos devuelve `{"placa": placa, "aprobado": True, "detalles": "Revision exitosa"}`; si hay fallos devuelve `{"placa": placa, "aprobado": False, "fallos_detectados": [...lista de fallos...]}`.
  - **Qué hace**: Construye una lista `fallos` añadiendo cadenas descriptivas por cada prueba que falle.

**Descripción de las pruebas en `test_modulos_transito.py`**

- Estructura general:
  - Para cada función hay tres grupos de pruebas: **normales**, **límites** y **errores** (exceptions o inputs inválidos).
  - Se usa `pytest.mark.parametrize` para cubrir varios ejemplos por prueba, y `pytest.raises` para validar excepciones esperadas.

- Cobertura por función:
  - `validar_placa`:
    - **Normales**: placas como `PBA-1234`, `ABC-123`, `XYZ-9999`.
    - **Límites**: `AAA-000` (números bajos) y `ZZZ-0000` (tres letras y 4 dígitos máximo).
    - **Errores**: minúsculas, formatos con menos letras o números, sin guion, tipos no-`str` (`int`, `None`).
  - `asignar_mes_revision`:
    - **Normales**: placas con último dígito mapeado (p. ej. `PBA-1231` => `Febrero`).
    - **Límites**: tarjeta con `0` como último dígito (`AAA-0000` => `Noviembre`).
    - **Errores**: placas inválidas que deben lanzar `ValueError`.
  - `calcular_multa`:
    - **Normales**: casos a tiempo (`0.0`) y tarde (`50.0`).
    - **Límites**: meses en los extremos del año (1 y 12).
    - **Errores**: meses fuera del rango 1..12 deberían lanzar `ValueError`.
  - `estado_revision`:
    - **Normales**: todas las pruebas pasan, la respuesta contiene `aprobado: True` y `detalles`.
    - **Fallas parciales**: cada prueba (gases/frenos/luces) evaluada individualmente produce un fallo único en `fallos_detectados`.
    - **Falla total**: todos los chequeos en `False` generan las tres entradas en `fallos_detectados`.

**Cómo ejecutar las pruebas**
- Abrir terminal en la carpeta raíz del proyecto o en `caso_integrador` y ejecutar:

```
cd "c:\Users\kalopez\Desktop\CURSOS MUNICIPIO\talleres_mdmq\caso_integrador"
pytest -q
```

**Sugerencias y mejoras**
- Para `validar_placa`: considerar aceptar minúsculas transformándolas a mayúsculas internamente o documentar que solo se aceptan mayúsculas.
- Para `asignar_mes_revision`: en lugar de devolver `'Desconocido'` podría lanzarse excepción si el dígito no es válido.
- Para `calcular_multa`: revisar política inter-anual (si la calendarización cruza años, la comparación numérica simple puede ser insuficiente).
- Para `estado_revision`: incluir la validación de `placa` para mantener consistencia y devolver un error si la placa es inválida.

---

*README generado automáticamente por asistente — contiene un resumen de la lógica y de las pruebas actuales.*

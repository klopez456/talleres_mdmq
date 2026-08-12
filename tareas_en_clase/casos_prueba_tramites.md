# Tabla de casos de prueba para `tramites.py`

Cada función tiene al menos un caso normal, uno de límite y uno de error. Los resultados indicados corresponden al comportamiento actual de la implementación.

| ID | Función | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| CC-01 | `validar_cedula` | Normal | `"0923456789"` | Devuelve `True`. Tiene exactamente 10 dígitos. |
| CC-02 | `validar_cedula` | Límite | `"123456789"` | Devuelve `False`. Tiene 9 dígitos, uno menos del mínimo requerido. |
| CC-03 | `validar_cedula` | Error | `None` | Devuelve `False` sin lanzar excepción. |
| CF-01 | `validar_fecha` | Normal | `"05/08/2026"` | Devuelve `True`. La fecha tiene formato válido y existe. |
| CF-02 | `validar_fecha` | Límite | `"29/02/2024"` | Devuelve `True`. Es el último día válido de febrero en un año bisiesto. |
| CF-03 | `validar_fecha` | Error | `"31/02/2026"` | Devuelve `False`. La fecha no existe. |
| CT-01 | `clasificar_tiempo` | Normal | `20` | Devuelve `"Normal"`. Está entre 11 y 30 minutos. |
| CT-02 | `clasificar_tiempo` | Límite | `10` | Devuelve `"Ágil"`. Es el límite superior de la categoría ágil. |
| CT-03 | `clasificar_tiempo` | Error | `-1` | Lanza `ValueError` con el mensaje `"El tiempo no puede ser negativo"`. |
| CP-01 | `calcular_promedio` | Normal | `[10, 20, 31]` | Devuelve `20.33`, redondeado a dos decimales. |
| CP-02 | `calcular_promedio` | Límite | `[]` | Devuelve `0.0` sin lanzar excepción. |
| CP-03 | `calcular_promedio` | Error | `[10, "20"]` | Lanza `TypeError` porque no se pueden sumar enteros y cadenas. |
| RD-01 | `resumen_diario` | Normal | `[{"cedula": "0923456789", "fecha": "05/08/2026", "minutos": 10}, {"cedula": "0912345678", "fecha": "06/08/2026", "minutos": 31}]` | Devuelve `{"total": 2, "descartados": 0, "promedio": 20.5, "conteo_categoria": {"Ágil": 1, "Normal": 0, "Demorada": 1}}`. |
| RD-02 | `resumen_diario` | Límite | `[]` | Devuelve `{"total": 0, "descartados": 0, "promedio": 0.0, "conteo_categoria": {"Ágil": 0, "Normal": 0, "Demorada": 0}}`. |
| RD-03 | `resumen_diario` | Error | `[{"cedula": "0923456789", "fecha": "05/08/2026", "minutos": -1}]` | Descarta el registro y devuelve `total = 0`, `descartados = 1`, `promedio = 0.0`; no lanza excepción. |

## Observaciones

- En `validar_cedula`, también son casos de error una cadena vacía, una cadena con letras o una entrada con una longitud distinta de 10.
- En `validar_fecha`, son casos de error el formato incorrecto, los meses fuera de 1 a 12, los días fuera del rango del mes y los valores no numéricos.
- En `resumen_diario`, los registros con cédula, fecha o minutos negativos inválidos se descartan. Sin embargo, un elemento que no sea un diccionario o un valor de `minutos` no numérico puede lanzar `AttributeError` o `TypeError`, respectivamente, porque la función no los captura.
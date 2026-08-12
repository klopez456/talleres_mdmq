# Talleres MDMQ

Este repositorio contiene ejercicios y prácticas realizadas durante el curso de GitHub Copilot para Desarrollo y Aseguramiento de la Calidad - GAD DMQ. El propósito principal es explorar el uso de herramientas de IA para apoyar la programación, la automatización de tareas y la validación de lógica en proyectos pequeños.

## Descripción general

El proyecto está compuesto por ejemplos sencillos de Python que muestran conceptos básicos de programación y validación de entrada de datos. El enfoque principal es practicar buenas prácticas de desarrollo y entender cómo una inteligencia artificial puede asistir en la creación, explicación y revisión de código.

## Estructura del repositorio

- `validacion.py`: archivo con funciones de validación para datos de entrada.

## Archivo principal de validación

El archivo `validacion.py` está desarrollado en Python, un lenguaje de programación interpretado, fácil de leer y ampliamente utilizado para automatización, scripts y desarrollo de aplicaciones.

### Tecnologías y detalles técnicos

- Lenguaje: Python 3
- Extensión del archivo: `.py`
- Tipo de archivo: script ejecutable
- Dependencias: no requiere bibliotecas externas
- Sintaxis: usa funciones nativas de Python y validaciones sobre cadenas de texto

### Funciones incluidas

#### `validar_cedula(cedula)`
Esta función verifica si una cédula cumple con la estructura esperada de Ecuador: debe tener exactamente 10 caracteres y estar compuesta únicamente por dígitos numéricos.

Lógica:
- `len(cedula) == 10`: valida la cantidad de caracteres.
- `cedula.isdigit()`: confirma que todos los caracteres sean números.
- Si ambas condiciones se cumplen, devuelve `True`; de lo contrario, devuelve `False`.

#### `validar_nombre(nombre)`
Esta función valida que un nombre o apellido esté compuesto únicamente por letras y espacios, permitiendo nombres con más de una palabra.

Lógica:
- `nombre.replace(" ", "")`: elimina los espacios para evaluar solo los caracteres del nombre.
- `.isalpha()`: comprueba que lo restante esté formado únicamente por letras.
- Si el resultado es válido, devuelve `True`; si contiene números u otros caracteres, devuelve `False`.

## Objetivo del repositorio

El repositorio tiene un enfoque didáctico y práctico, con el objetivo de:

- Aprender a escribir scripts en Python.
- Validar entradas del usuario.
- Comprender el uso de funciones y condiciones.
- Utilizar GitHub Copilot como apoyo durante el desarrollo.

## Ejemplo de uso

```python
from validacion import validar_cedula, validar_nombre

print(validar_cedula("0923456789"))
print(validar_nombre("Ana Maria"))
```

## Conclusión

Este repositorio es una colección de ejercicios básicos que muestran cómo implementar validaciones y pequeños programas con Python, reforzando la comprensión de programación lógica y el uso de herramientas de asistencia en el desarrollo de software.

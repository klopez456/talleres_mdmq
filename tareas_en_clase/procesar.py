# Script que recorre la carpeta ./datos, lee cada archivo CSV
# con columnas cedula, fecha y minutos, valida cada fila con
# las funciones de tramites.py y escribe resumen.csv con el
# total de filas válidas, las descartadas y el promedio de
# minutos. Usa solo la librería estándar (csv, pathlib).
# No debe detenerse si una fila tiene datos inválidos.
import csv
from pathlib import Path
from tramites import validar_cedula, validar_fecha, clasificar_tiempo
def procesar_carpeta(carpeta: str = "datos") -> dict:
    base_dir = Path(__file__).resolve().parent.parent
    carpeta_path = Path(carpeta)

    if not carpeta_path.is_absolute():
        candidatos = [base_dir / carpeta_path, base_dir / carpeta_path.name]
        carpeta_path = next((ruta.resolve() for ruta in candidatos if ruta.exists()), (base_dir / carpeta_path).resolve())
    else:
        carpeta_path = carpeta_path.resolve()

    carpeta_path.mkdir(parents=True, exist_ok=True)

    total_validas = 0
    total_descartadas = 0
    tiempos_validos = []

    for archivo_csv in sorted(carpeta_path.glob("*.csv")):
        with archivo_csv.open("r", encoding="utf-8", newline="") as fh:
            lector = csv.DictReader(fh)
            for fila in lector:
                cedula = fila.get("cedula", "")
                fecha = fila.get("fecha", "")
                minutos_texto = fila.get("minutos", "")

                try:
                    minutos = int(minutos_texto)
                except (TypeError, ValueError):
                    total_descartadas += 1
                    continue

                if (
                    not validar_cedula(cedula)
                    or not validar_fecha(fecha)
                    or minutos < 0
                ):
                    total_descartadas += 1
                    continue

                clasificar_tiempo(minutos)
                total_validas += 1
                tiempos_validos.append(minutos)

    promedio = round(sum(tiempos_validos) / len(tiempos_validos), 2) if tiempos_validos else 0.0

    resumen_path = carpeta_path / "resumen.csv"
    with resumen_path.open("w", encoding="utf-8", newline="") as fh:
        escritor = csv.writer(fh)
        escritor.writerow(["total_validas", "descartadas", "promedio_minutos"])
        escritor.writerow([total_validas, total_descartadas, promedio])

    return {
        "total_validas": total_validas,
        "descartadas": total_descartadas,
        "promedio_minutos": promedio,
        "archivo_resumen": str(resumen_path),
    }

# Bloque para ejecutarlo directamente
if __name__ == "__main__":
    resultado = procesar_carpeta()
    print(f"Proceso finalizado. Resultados: {resultado}")

# Semana 02 — Configuracion del entorno de trabajo

Scripts de la sesion practica de la Semana 2 del curso Analisis de Algoritmos.

## Archivos

- `refactor_pep8.py`: version PEP 8 del calculador de promedio con type hints, docstring y entrada `main()`.
- `clasificador_anios.py`: ejercicio integrador que determina cuales anios de una lista son bisiestos.

## Comandos para reproducir el entorno virtual

Desde la raiz del repositorio (`curso-analisis-algoritmos/`):

```powershell
# 1. Crear el entorno virtual (una sola vez)
python -m venv venv

# 2. Activar el entorno (el prefijo "(venv)" aparece en la terminal)
.\venv\Scripts\Activate.ps1

# 3. Instalar las dependencias del curso
pip install -r requirements.txt

# 4. Ejecutar el clasificador
python .\ejercicios-clase\semana-02\clasificador_anios.py

# 5. Desactivar el entorno cuando se termine
deactivate
```

La carpeta `venv/` y `requirements.antes.txt` / `requirements.despues.txt` (usados para verificar
la reproducibilidad) estan excluidas en `.gitignore` y no se suben al repositorio.

# Proyecto Python - EXAMEN PRIMER MOMENTO

## Integrantes
- Carlos Andres Bolivar Berrio (carlboli)
- Joan Sebastian Caballero (Jscbllero)

## Descripcion
Aplicacion en Python para cargar y validar datos de compras desde un archivo CSV, generar estadisticas y producir un reporte en formato JSON.  
Incluye practicas de Git/GitHub como manejo de ramas, issues, releases y resolucio de conflictos.
## Estrategia de Branching y Reglas

Este repositorio utiliza una estrategia basada en **Git Flow simplificado**:

- La rama principal es **`main`**, donde siempre se encuentra el código en estado **estable y listo para producción**.
- La rama de desarrollo es **`dev`**, donde se integran las nuevas funcionalidades antes de pasar a `main`.
- Para cada nueva característica o corrección se crean ramas con el prefijo **`feature/`** a partir de `dev`.  
  Ejemplo: `feature/login`, `feature/api-conexion`.

### Flujo de trabajo
1. Crear una rama desde `dev` con el prefijo `feature/`.
2. Desarrollar la funcionalidad o corrección en la rama `feature/*`.
3. Hacer **Pull Request (PR)** hacia `dev`.
4. El PR debe ser aprobado al menos por **1 revisor** antes de poder hacer merge.
5. Una vez validado en `dev`, se crea un PR hacia `main`.
6. `main` se actualiza únicamente mediante PR, nunca con commits directos.

### Reglas de protección
- La rama **`main`** y la rama **`dev`** están protegidas:
  - ✅ Requieren Pull Request antes de hacer merge.  
  - ✅ Requieren al menos **1 aprobación** de revisor.  
  - ✅ Se recomienda habilitar *Require status checks* (tests) antes de merge.  
  - 🚫 No se permiten commits directos.

De esta manera aseguramos un flujo controlado, con revisiones obligatorias y evitando errores en la rama principal.


## Instrucciones de ejecucion
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TuUsuarioGitHub/EXAMEN_PYTHON.git
   cd EXAMEN_PYTHON

# Gestor de flujo de caja

Este proyecto es una solución en Python diseñada para ayudar a emprendedores y profesionales a gestionar su flujo de caja de manera eficiente. Integra conceptos de ingeniería de sistemas y finanzas, permitiendo el registro, análisis, simulación y proyección de transacciones financieras para apoyar en la toma de decisiones estratégicas.

## Funciones principales

### 1. Cargar archivo CSV
Permite cargar un archivo CSV con transacciones financieras. El archivo debe incluir las siguientes columnas:
- **fecha**: Fecha de la transacción (formato `YYYY-MM-DD`).
- **tipo**: Tipo de transacción, que puede ser `ingreso` o `gasto`.
- **categoria**: Categoría de la transacción (por ejemplo, ventas, marketing, suministros).
- **monto**: Monto de la transacción, expresado en pesos colombianos (**COP**).
- **descripcion**: Breve descripción o detalle de la transacción.

Si el archivo no existe, puedes crear uno manualmente con la siguiente estructura:

```csv
fecha,tipo,categoria,monto,descripcion
2025-01-01,ingreso,ventas,5000.00,Ingreso por ventas
2025-01-15,gasto,marketing,800.00,Campaña publicitaria
2025-01-20,gasto,suministros,400.00,Compra de insumos
```

### 2. Generar reporte mensual
Genera un reporte financiero mensual con las siguientes métricas clave:
- **Mes y año** de la transacción.
- **Ingresos totales (COP)**.
- **Gastos totales (COP)**.
- **Flujo neto (COP)**.
- **Flujo acumulado (COP)** (acumulación histórica de flujo neto).
- **Indicadores financieros** como:
  - **Burn rate (ratio)**: Promedio de gastos mensuales.
  - **Liquidez (ratio)**: Relación entre ingresos y gastos por mes.
  - **Rentabilidad (%)**: Relación entre flujo neto e ingresos.
  - **Días efectivo (días)**: Tiempo estimado que el balance acumulado puede sostener el negocio.

### 3. Visualización y gráficos
Proporciona gráficos interactivos que ayudan a analizar la dinámica del flujo de caja:
- **Gráfico de barras apiladas**: Ingresos y gastos mensuales.
- **Distribución de gastos por categoría**.
- **Distribución de ingresos por categoría**.
  
### 4. Ver balance actual
Calcula el balance financiero actual sumando todos los ingresos y restando todos los gastos registrados.

### 5. Simular transacción
Evalúa el impacto de una transacción hipotética en el balance actual sin modificar los datos originales. Permite al usuario:
- Seleccionar el tipo de transacción (`ingreso` o `gasto`).
- Ingresar el monto de la transacción.
- Visualizar el balance actual, el balance simulado y la diferencia resultante.

### 6. Detección de patrones de gasto
Analiza las transacciones para identificar categorías con altos niveles de gasto en comparación con el total y sugiere dónde optimizar.

### 7. Proyección del flujo de caja
Utiliza módulo de inteligencia artificial (**IA**) para predecir la evolución futura del flujo de caja a partir de regresiones, modelando datos históricos con un enfoque de **regresión lineal**. Permite estimar:
- **Ingresos estimados** (próximos 4 meses).
- **Gastos estimados** (próximos 4 meses).

Ejemplo de resultado:
```csv
Mes futuro,Ingreso estimado (COP),Gasto estimado (COP)
Mes 1,5200.00,1600.00
Mes 2,5400.00,1700.00
Mes 3,5600.00,1800.00
Mes 4,5800.00,1900.00
```

---

## Instalación

1. Asegúrate de que tengas **Python 3.x** instalado.
2. Instala las siguientes librerías necesarias ejecutando el comando:
   ```bash
   pip install pandas matplotlib numpy scikit-learn
   ```
3. Descarga o clona este repositorio en tu sistema:
   ```bash
   git clone https://github.com/usuario/gestor-flujo-caja.git
   cd gestor-flujo-caja
   ```

---

## Uso
Clona el repositorio en tu espacio de trabajo, luego:

1. **Inicia la aplicación**:
   Esto abrirá una interfaz gráfica de usuario (GUI).

2. **Carga un archivo CSV**:
   - Haz clic en el botón **"📂 Cargar archivo CSV"**.
   - Selecciona un archivo CSV con tus transacciones financieras.
   - Si el archivo no contiene columnas válidas o tiene datos inconsistentes, la carga fallará.

3. **Funciones disponibles en la GUI**:
   - **Generar reportes**: Haz clic en **"📊 Generar reporte"** para ver un resumen mensual interactivo.
   - **Visualizar gráficos**: Haz clic en **"📈 Generar gráficos"** para ver gráficos financieros.
   - **Proyección de flujo de caja**: Haz clic en **"🔮 Proyección"** para predecir ingresos y gastos a futuro.
   - **Simular transacciones**: Haz clic en **"🧮 Simular transacción"** para evaluar el impacto de una transacción hipotética.

4. **Actualiza los datos cuando sea necesario**:
   Si deseas añadir nuevas transacciones, edita manualmente tu archivo CSV y cárgalo nuevamente.

---

## Formato del archivo CSV

El programa trabaja exclusivamente con archivos CSV en el siguiente formato:

| **Columna**   | **Descripción**                                                                            |
|---------------|--------------------------------------------------------------------------------------------|
| `fecha`       | Fecha de la transacción (formato: `YYYY-MM-DD`).                                           |
| `tipo`        | Tipo de transacción (`ingreso` o `gasto`).                                                 |
| `categoria`   | Categoría asociada (ventas, marketing, suministros, etc.).                                 |
| `monto`       | Cantidad de dinero involucrada en la transacción (en **COP**).                             |
| `descripcion` | Detalle adicional de la transacción (opcional).                                            |

Ejemplo de archivo:
```csv
fecha,tipo,categoria,monto,descripcion
2025-01-05,ingreso,ventas,3000,Venta producto A
2025-01-10,gasto,marketing,500,Campaña de publicidad
2025-01-15,ingreso,consultoría,1500,Servicios de consultoría
2025-01-20,gasto,suministros,200,Compra de materiales
```

---

## Ejemplo de flujo de trabajo

1. **Inicio**: Abres la aplicación y cargas el archivo CSV con tus transacciones.
2. **Balance actual**: Automáticamente se calcula el balance financiero basado en los datos cargados.
3. **Reporte detallado**: Generas un reporte financiero mensual desde la interfaz.
4. **Simulación de transacciones**: Calculas el impacto de un ingreso o gasto hipotético.
5. **Proyección del flujo de caja**: Predices los movimientos financieros de los próximos meses.
6. **Gráficos interactivos**: Analizas visualmente los ingresos y gastos por periodos y categorías.

---

## Notas importantes

1. **Formato de fechas**: Todas las fechas deben estar en el formato `YYYY-MM-DD`.
2. **Validación de datos**: 
   - El tipo de transacción debe ser `ingreso` o `gasto`.
   - Todas las columnas obligatorias deben estar presentes y con valores válidos.
3. **Errores comunes**:
   - Si un archivo CSV tiene valores no numéricos, columnas incompletas o categorías desconocidas, la carga fallará.
4. **Moneda**: Todos los montos deben estar expresados en **COP** (Pesos Colombianos).

---

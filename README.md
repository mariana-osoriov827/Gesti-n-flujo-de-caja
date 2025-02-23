# Gestor de flujo de caja

Este proyecto es una solución en Python diseñada para ayudar a emprendedores y profesionales a gestionar su flujo de caja de forma eficiente. Integra conceptos de ingeniería de sistemas y finanzas, permitiendo el registro, análisis y simulación de transacciones para apoyar la toma de decisiones financieras en startups.

## Funciones

### Cargar CSV
Permite cargar un archivo CSV con transacciones financieras. Si el archivo no existe, se crea automáticamente con la estructura necesaria.

### Generar reporte
Genera un reporte mensual con la siguiente información:
- **Mes y año**
- **Ingresos totales (COP)**
- **Gastos totales (COP)**
- **Flujo neto (COP)**
- **Rentabilidad (%)**
- **Categorías de ingresos y gastos**

### Ver balance actual
Calcula el balance actual sumando los ingresos y restando los gastos registrados hasta la fecha.

### Simular transacción
Permite evaluar el impacto de una transacción hipotética en el balance sin modificar los datos originales.

### Indicadores financieros
Proporciona métricas clave para evaluar la salud financiera del negocio:
- **Burn rate**: Promedio de gastos mensuales.
- **Runway**: Meses estimados que el negocio puede sostenerse con el balance actual.
- **Tasa de crecimiento de ingresos (%)**: Variación de ingresos en el tiempo.
- **Punto de equilibrio**: Momento en que los ingresos cubren los costos fijos.
- **Tendencia del flujo de caja**: Proyección del flujo de caja basada en patrones históricos.

### Visualizaciones
Genera gráficos de barras para visualizar:
- **Flujo de caja mensual**
- **Distribución de gastos por categoría**
- **Distribución de ingresos por categoría**

### Detección de patrones de gasto
Analiza las transacciones para identificar categorías con altos niveles de gasto y sugiere posibles ajustes para optimizar recursos.

### Proyección de flujo de caja
Utiliza técnicas de inteligencia artificial para predecir la evolución futura del flujo de caja en función de patrones de gasto e ingreso previos.

## Requisitos
- Python 3.x
- Librerías: pandas, matplotlib, numpy, sklearn

## Uso

Para usar el programa, debes clonarlo en tu máquina. Luego, al ejecutarlo, debes seguir los siguientes pasos:

### 1. **Cargar el archivo CSV**
   - Al iniciar el programa (`python main.py`), se abrirá una interfaz gráfica interactiva. En ella, haz clic en el botón **"Cargar archivo CSV"** para seleccionar el archivo que contiene tus transacciones financieras.
   - Si no tienes un archivo existente, el programa creará automáticamente uno con la estructura inicial:
     ```csv
     fecha,tipo,categoria,monto,descripcion
     2025-01-01,ingreso,ventas,5000.00,Ingreso por ventas
     2025-01-15,gasto,marketing,800.00,Campaña publicitaria
     2025-01-20,gasto,suministros,400.00,Compra de insumos
     ```
     - **fecha**: Fecha de la transacción en formato `YYYY-MM-DD`.
     - **tipo**: Puede ser `ingreso` o `gasto`.
     - **categoria**: Tipo de transacción (por ejemplo, ventas, marketing, suministros).
     - **monto**: Monto de la transacción, expresado en **COP** (Pesos Colombianos).
     - **descripcion**: Detalle opcional de la transacción.

### 2. **Generar un reporte financiero mensual**
   - Una vez cargadas las transacciones, haz clic en el botón **"Generar reporte"**. Esto mostrará un resumen financiero mensual con las siguientes columnas:
     - **Mes y Año**: Periodo de la transacción.
     - **Ingresos totales (COP)**.
     - **Gastos totales (COP)**.
     - **Flujo neto (COP)**.
     - **Flujo acumulado (COP)**.
     - Indicadores como **Burn Rate**, **Liquidez**, y **Rentabilidad (%)**.
     - 
### 3. **Visualización de datos**
   - Haz clic en **"Generar gráficos"** para visualizar tus transacciones financieras con gráficos detallados:
     - **Gráfico de barras apiladas**: Muestra los ingresos y gastos totales por mes.
     - **Distribución de gastos** por categoría.
     - **Distribución de ingresos** por categoría.
   - Los gráficos permiten identificar patrones y tendencias, facilitando la toma de decisiones.

### 4. **Proyección del flujo de caja**
   - Haz clic en el botón **"Proyección"** para predecir el comportamiento del flujo de caja en los próximos 4 meses. Las predicciones utilizan inteligencia artificial (modelo de regresión lineal) basada en los datos históricos.
   - Verás un reporte como el siguiente:
     ```csv
     Mes futuro,Ingreso estimado (COP),Gasto estimado (COP)
     Mes 1,5200.00,1600.00
     Mes 2,5400.00,1700.00
     Mes 3,5600.00,1800.00
     Mes 4,5800.00,1900.00
     ```
     - **Ingreso estimado (COP)**: Proyección mensual de ingresos.
     - **Gasto estimado (COP)**: Proyección mensual de gastos.

### 5. **Registrar nuevas transacciones**
   - Edita manualmente tu archivo CSV con nuevas transacciones y vuelve a cargarlo en la aplicación para actualizar los datos.
   - Alternativamente, utiliza la funcionalidad de simulación de transacciones para calcular el impacto de una transacción hipotética en el balance actual sin alterar los datos originales.
     
---

## Archivos CSV

El programa trabaja con archivos CSV que deben seguir el formato proporcionado. Aquí tienes un ejemplo de archivo que puedes usar como base:

```csv
fecha,tipo,categoria,monto,descripcion
2025-01-05,ingreso,ventas,3000,venta producto a
2025-01-10,gasto,marketing,500,campaña publicidad
2025-01-15,ingreso,servicios,1500,consultoría
2025-01-20,gasto,suministros,200,compra materiales
...
```

---

### Ejemplo de flujo de trabajo

1. **Inicio**: Abres la aplicación y cargas el archivo CSV con tus transacciones.
2. **Balance actual**: Automáticamente se calcula el balance financiero basado en los datos cargados.
3. **Reporte detallado**: Generas un reporte financiero mensual.
4. **Visualización con gráficos**: Generas gráficos que detallan ingresos, gastos y distribuciones.
5. **Proyección del flujo de caja**: Generas predicciones financieras.

---

### Notas importantes:
- **Formato de fechas**: Asegúrate de que las fechas estén en el formato `YYYY-MM-DD`.
- **Valores de moneda**: Todos los valores monetarios deben estar en **COP (Pesos Colombianos)**.
- **Errores comunes**:
  - Si el archivo CSV tiene valores faltantes o categorías inconsistentes, la carga fallará. Limpia y verifica tus datos antes de importarlos.

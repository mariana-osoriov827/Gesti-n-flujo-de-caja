# Gestor de flujo de caja

Este proyecto es una solución en Python diseñada para ayudar a emprendedores y profesionales a gestionar su flujo de caja de forma eficiente. Integra conceptos de ingeniería de sistemas y finanzas, permitiendo el registro, análisis y simulación de transacciones para apoyar la toma de decisiones financieras en startups.

## Características
- Registro de transacciones: Permite agregar ingresos y gastos mediante la carga de un archivo CSV.
- Reporte mensual: Agrupa las transacciones por mes y muestra ingresos, gastos y flujo neto.
- Balance actual: Calcula el balance actual (ingresos menos gastos).
- Simulación de transacciones: Evalúa el impacto de una transacción hipotética sin modificar los datos reales.
- Indicadores financieros:
  - Burn rate: Promedio de gastos mensuales.
  - Runway: Estimación en meses de la duración del balance actual, basado en el burn rate.
  - Tasa de crecimiento de ingresos: Porcentaje de crecimiento de los ingresos a lo largo del tiempo.
  - Punto de equilibrio: Cálculo del punto de equilibrio según costos fijos y margen de contribución.
  - Tendencia del flujo de caja: Estimación de la tendencia futura del flujo neto.
- Visualizaciones: Gráficos de barras para analizar el flujo de caja mensual y la distribución de gastos e ingresos por categoría.

## Requisitos
- Python 3.x
- Librerías: pandas, matplotlib, numpy
  
## Uso

Clona este repositorio y navega hasta la carpeta del proyecto. Ejecuta el script principal (por ejemplo, `python main.py`). Al iniciar, se te solicitará el nombre del archivo csv a cargar (con extensión `.csv`). Si el archivo no existe, se creará uno nuevo con la estructura necesaria. El programa registra transacciones, genera reportes, gráficos e indicadores financieros que te ayudarán a analizar el estado y la tendencia de tu flujo de caja.

## Archivos csv

El proyecto utiliza archivos csv con la siguiente estructura:

```csv
fecha,tipo,categoria,monto,descripcion
2025-01-05,ingreso,ventas,3000,venta producto a
2025-01-10,gasto,marketing,500,campaña publicidad
2025-01-15,ingreso,servicios,1500,consultoría
2025-01-20,gasto,suministros,200,compra materiales
...

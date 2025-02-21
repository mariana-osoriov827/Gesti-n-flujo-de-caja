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

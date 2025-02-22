# Gestor de flujo de caja

Este proyecto es una solución en Python diseñada para ayudar a emprendedores y profesionales a gestionar su flujo de caja de forma eficiente. Integra conceptos de ingeniería de sistemas y finanzas, permitiendo el registro, análisis y simulación de transacciones para apoyar la toma de decisiones financieras en startups.

## Características

### Cargar CSV
Permite cargar un archivo CSV con transacciones financieras. Si el archivo no existe, se crea automáticamente con la estructura necesaria.

### Generar reporte
Genera un reporte mensual con la siguiente información:
- **Mes y año**
- **Ingresos totales (moneda local)**
- **Gastos totales (moneda local)**
- **Flujo neto (moneda local)**
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

### Exportación de reportes
Permite exportar los reportes financieros a un archivo CSV para análisis externo o archivo histórico.

### Detección de patrones de gasto
Analiza las transacciones para identificar categorías con altos niveles de gasto y sugiere posibles ajustes para optimizar recursos.

### Proyección de flujo de caja
Utiliza técnicas de inteligencia artificial para predecir la evolución futura del flujo de caja en función de patrones de gasto e ingreso previos.

## Requisitos
- Python 3.x
- Librerías: pandas, matplotlib, numpy
  
## Uso

Clona este repositorio y navega hasta la carpeta del proyecto. Ejecuta el script principal (por ejemplo, `python main.py`). Al iniciar, se te solicitará el nombre del archivo CSV a cargar (con extensión `.csv`). Si el archivo no existe, se creará uno nuevo con la estructura necesaria. El programa registra transacciones, genera reportes, gráficos e indicadores financieros que te ayudarán a analizar el estado y la tendencia de tu flujo de caja.

## Archivos CSV

El proyecto utiliza archivos CSV con la siguiente estructura:

```csv
fecha,tipo,categoria,monto,descripcion
2025-01-05,ingreso,ventas,3000,venta producto a
2025-01-10,gasto,marketing,500,campaña publicidad
2025-01-15,ingreso,servicios,1500,consultoría
2025-01-20,gasto,suministros,200,compra materiales
...

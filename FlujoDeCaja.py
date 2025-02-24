import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.linear_model import LinearRegression
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GestorFlujoCaja:
    def __init__(self):
        self.transacciones = pd.DataFrame()

    def cargar_csv(self):
        archivo_csv = filedialog.askopenfilename(
            title="Seleccione un archivo CSV", filetypes=[("CSV Files", "*.csv")]
        )
        if not archivo_csv:
            messagebox.showerror("Error", "No se seleccionó ningún archivo CSV.")
            return False

        try:
            self.transacciones = pd.read_csv(archivo_csv, parse_dates=["fecha"])
            self.transacciones["monto"] = pd.to_numeric(
                self.transacciones["monto"], errors="coerce"
            ).fillna(0)
            self.transacciones["tipo"] = self.transacciones["tipo"].str.strip().str.lower()
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo CSV: {e}")
            return False

    def balance_actual(self):
        ingresos = self.transacciones[self.transacciones["tipo"] == "ingreso"]["monto"].sum()
        gastos = self.transacciones[self.transacciones["tipo"] == "gasto"]["monto"].sum()
        return ingresos - gastos

    def generar_reporte(self):
        if self.transacciones.empty:
            messagebox.showinfo("Información", "No hay datos para generar un reporte.")
            return None

        self.transacciones["mes_año"] = self.transacciones["fecha"].dt.strftime('%B %Y')
        rep = self.transacciones.groupby(["mes_año", "tipo"])["monto"].sum().unstack().fillna(0)
        rep["Mes y año"] = rep.index  # Agregar la columna con Mes y Año directamente
        rep["flujo_neto"] = rep.get("ingreso", 0) - rep.get("gasto", 0)
        rep["flujo_acumulado"] = rep["flujo_neto"].cumsum()

        rep["burn_rate"] = rep.get("gasto", 0) / rep.get("ingreso", 1).replace(0, 1)
        rep["liquidez"] = rep.get("ingreso", 0) / rep.get("gasto", 1).replace(0, 1)
        rep["rentabilidad"] = (rep["flujo_neto"] / rep.get("ingreso", 1).replace(0, 1)) * 100
        rep["dias_efectivo"] = rep["flujo_acumulado"] / (rep.get("gasto", 1).replace(0, 1) / 30)

        # Renombrar columnas con unidades
        rep = rep.rename(columns={
            "ingreso": "Ingreso (COP)",
            "gasto": "Gasto (COP)",
            "flujo_neto": "Flujo neto (COP)",
            "flujo_acumulado": "Flujo acumulado (COP)",
            "burn_rate": "Burn rate (Ratio)",
            "liquidez": "Liquidez (Ratio)",
            "rentabilidad": "Rentabilidad (%)",
            "dias_efectivo": "Días efectivo (días)"
        })
        columnas = ["Mes y Año"] + [col for col in rep.columns if col != "Mes y Año"]
        rep = rep[columnas]

        return rep.round(2)

    def mostrar_reporte(self, root):
        reporte = self.generar_reporte()
        if reporte is not None:
            top = tk.Toplevel(root)
            top.title("Reporte Financiero")
            frame = ttk.Frame(top)
            frame.pack(fill=tk.BOTH, expand=True)

            # Crear Treeview
            tree = ttk.Treeview(frame, columns=list(reporte.columns), show='headings', height=20)
            for col in reporte.columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="center")
            for _, row in reporte.iterrows():
                tree.insert("", "end", values=row.tolist())
            tree.pack(fill=tk.BOTH, expand=True)

    def generar_graficos(self, root):
        if self.transacciones.empty:
            messagebox.showinfo("Información", "No hay datos para generar gráficos.")
            return

        # Crear gráfico del flujo de caja (ingresos vs gastos)
        fig, ax = plt.subplots(figsize=(10, 5))
        self.transacciones["mes_año"] = self.transacciones["fecha"].dt.to_period("M")
        datos_agrupados = self.transacciones.groupby(["mes_año", "tipo"])["monto"].sum().unstack().fillna(0)

        datos_agrupados.plot(kind="bar", stacked=True, ax=ax)
        ax.set_title("Flujo de Caja por Mes (COP)")
        ax.set_ylabel("Monto (COP)")
        ax.set_xlabel("Meses")
        ax.legend(["Ingresos", "Gastos"], loc="upper left")
        ax.tick_params(axis="x", rotation=45)

        # Mostrar gráfico en la ventana
        for widget in root.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

    def proyectar_flujo_caja(self):
        if self.transacciones.empty:
            messagebox.showinfo("Información", "No hay datos suficientes para hacer proyecciones.")
            return None

        # Preparar los datos para el modelo
        self.transacciones["mes_num"] = self.transacciones["fecha"].dt.to_period("M").astype("category").cat.codes
        ingresos = self.transacciones[self.transacciones["tipo"] == "ingreso"].groupby("mes_num")["monto"].sum()
        gastos = self.transacciones[self.transacciones["tipo"] == "gasto"].groupby("mes_num")["monto"].sum()

        datos = pd.DataFrame({"ingresos": ingresos, "gastos": gastos}).fillna(0)

        X = np.arange(len(datos)).reshape(-1, 1)  # Los índices de los meses
        y_ingresos = datos["ingresos"].values.reshape(-1, 1)
        y_gastos = datos["gastos"].values.reshape(-1, 1)

        # Entrenar los modelos (ingresos y gastos)
        modelo_ingresos = LinearRegression().fit(X, y_ingresos)
        modelo_gastos = LinearRegression().fit(X, y_gastos)

        # Proyectar ingresos y gastos para los próximos 4 meses
        futuros = np.arange(len(datos), len(datos) + 4).reshape(-1, 1)
        pred_ingresos = modelo_ingresos.predict(futuros).flatten()
        pred_gastos = modelo_gastos.predict(futuros).flatten()

        # Crear DataFrame con las predicciones
        proyeccion = pd.DataFrame({
            "Mes futuro": [f"Mes {i + 1}" for i in range(len(futuros))],
            "Ingreso estimado (COP)": pred_ingresos,
            "Gasto estimado (COP)": pred_gastos
        }).round(2)

        return proyeccion

    def simular_transaccion(self, monto, tipo):
        if tipo not in ["ingreso", "gasto"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'gasto'.")

        balance_actual = self.balance_actual()

        if tipo == "ingreso":
            balance_simulado = balance_actual + monto
        elif tipo == "gasto":
            balance_simulado = balance_actual - monto

        # Retornar los resultados de la simulación
        return {
            "balance_actual": balance_actual,
            "balance_simulado": balance_simulado,
            "tipo_transaccion": tipo,
            "monto_transaccion": monto,
            "diferencia": balance_simulado - balance_actual
        }


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de flujo de caja")
        self.gestor = GestorFlujoCaja()
        self.root.geometry("800x600")
        self.root.configure(bg="#2E2E2E")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TLabel", font=("Arial", 12), background="#2E2E2E", foreground="white")

        frame = ttk.Frame(root)
        frame.pack(expand=True)

        self.boton_cargar = ttk.Button(frame, text="📂 Cargar archivo CSV", command=self.cargar_csv)
        self.boton_cargar.pack(pady=5, fill=tk.X)

        self.boton_reporte = ttk.Button(frame, text="📊 Generar reporte", command=self.generar_reporte)
        self.boton_reporte.pack(pady=5, fill=tk.X)

        self.boton_graficos = ttk.Button(frame, text="📈 Generar gráficos", command=self.generar_graficos)
        self.boton_graficos.pack(pady=5, fill=tk.X)

        self.boton_proyeccion = ttk.Button(frame, text="🔮 Proyección", command=self.generar_proyeccion)
        self.boton_proyeccion.pack(pady=5, fill=tk.X)

        self.boton_simulacion = ttk.Button(frame, text="🧮 Simular transacción", command=self.simular_transaccion)
        self.boton_simulacion.pack(pady=5, fill=tk.X)

        self.label_balance = ttk.Label(frame, text="Balance actual: $0")
        self.label_balance.pack(pady=10)

    def cargar_csv(self):
        if self.gestor.cargar_csv():
            balance = self.gestor.balance_actual()
            self.label_balance.config(text=f"Balance actual: ${balance:,.2f} COP")
            messagebox.showinfo("Éxito", "Datos cargados correctamente. Balance actualizado.")

    def generar_reporte(self):
        self.gestor.mostrar_reporte(self.root)

    def generar_graficos(self):
        self.gestor.generar_graficos(self.root)

    def generar_proyeccion(self):
        proyeccion = self.gestor.proyectar_flujo_caja()
        if proyeccion is not None:
            top = tk.Toplevel(self.root)
            top.title("Proyección IA")
            frame = ttk.Frame(top)
            frame.pack(fill=tk.BOTH, expand=True)

            columnas = list(proyeccion.columns)
            tree = ttk.Treeview(frame, columns=columnas, show='headings')
            for col in columnas:
                tree.heading(col, text=col)
                tree.column(col, anchor="center")
            for _, row in proyeccion.iterrows():
                tree.insert("", "end", values=row.tolist())
            tree.pack(fill=tk.BOTH, expand=True)

    def simular_transaccion(self):
        def realizar_simulacion():
            try:
                monto = float(entry_monto.get())
                tipo = combo_tipo.get().lower()
                resultados = self.gestor.simular_transaccion(monto, tipo)

                messagebox.showinfo(
                    "Resultados de la Simulación",
                    f"Balance actual: ${resultados['balance_actual']:,.2f} COP\n"
                    f"Tipo de transacción: {resultados['tipo_transaccion']}\n"
                    f"Monto de la transacción: ${resultados['monto_transaccion']:,.2f} COP\n"
                    f"Balance simulado: ${resultados['balance_simulado']:,.2f} COP\n"
                    f"Diferencia: ${resultados['diferencia']:,.2f} COP"
                )
            except ValueError as ve:
                messagebox.showerror("Error", f"Entrada no válida: {ve}")
            except Exception as e:
                messagebox.showerror("Error", f"{e}")

        ventana_simulacion = tk.Toplevel(self.root)
        ventana_simulacion.title("Simular transacción")
        ventana_simulacion.geometry("400x300")

        frame_simulacion = ttk.Frame(ventana_simulacion)
        frame_simulacion.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        ttk.Label(frame_simulacion, text="Tipo de Transacción:").pack(anchor="w")
        combo_tipo = ttk.Combobox(frame_simulacion, values=["Ingreso", "Gasto"], state="readonly")
        combo_tipo.current(0)
        combo_tipo.pack(fill=tk.X, pady=5)

        ttk.Label(frame_simulacion, text="Monto (COP):").pack(anchor="w")
        entry_monto = ttk.Entry(frame_simulacion)
        entry_monto.pack(fill=tk.X, pady=5)

        boton_realizar = ttk.Button(frame_simulacion, text="Simular", command=realizar_simulacion)
        boton_realizar.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

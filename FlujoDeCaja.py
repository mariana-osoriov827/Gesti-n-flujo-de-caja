import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression


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
        rep["Mes y Año"] = rep.index  # Agregar la columna con Mes y Año directamente
        rep["flujo_neto"] = rep.get("ingreso", 0) - rep.get("gasto", 0)
        rep["flujo_acumulado"] = rep["flujo_neto"].cumsum()

        rep["burn_rate"] = rep.get("gasto", 0) / rep.get("ingreso", 1).replace(0, 1)
        rep["liquidez"] = rep.get("ingreso", 0) / rep.get("gasto", 1).replace(0, 1)
        rep["rentabilidad"] = (rep["flujo_neto"] / rep.get("ingreso", 1).replace(0, 1)) * 100
        rep["dias_efectivo"] = rep["flujo_acumulado"] / (rep.get("gasto", 1).replace(0, 1) / 30)

        # Renombrar columnas con unidades y asegurarse de que "Mes y Año" sea la primera columna
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

        self.transacciones["mes_num"] = self.transacciones["fecha"].dt.to_period("M").astype("category").cat.codes
        ingresos = self.transacciones[self.transacciones["tipo"] == "ingreso"].groupby("mes_num")["monto"].sum()
        gastos = self.transacciones[self.transacciones["tipo"] == "gasto"].groupby("mes_num")["monto"].sum()

        datos = pd.DataFrame({"ingresos": ingresos, "gastos": gastos}).fillna(0)

        X = np.arange(len(datos)).reshape(-1, 1)
        y_ingresos = datos["ingresos"].values.reshape(-1, 1)
        y_gastos = datos["gastos"].values.reshape(-1, 1)

        modelo_ingresos = LinearRegression().fit(X, y_ingresos)
        modelo_gastos = LinearRegression().fit(X, y_gastos)

        futuros = np.arange(len(datos), len(datos) + 4).reshape(-1, 1)
        pred_ingresos = modelo_ingresos.predict(futuros).flatten()
        pred_gastos = modelo_gastos.predict(futuros).flatten()

        proyeccion = pd.DataFrame({
            "Mes futuro": [f"Mes {i + 1}" for i in range(len(futuros))],
            "Ingreso estimado (COP)": pred_ingresos,
            "Gasto estimado (COP)": pred_gastos
        }).round(2)

        return proyeccion

    def generar_alerta(self):
        if self.transacciones.empty:
            messagebox.showinfo("Información", "No hay datos para generar alertas.")
            return

        gastos = self.transacciones[self.transacciones["tipo"] == "gasto"]
        if gastos.empty:
            messagebox.showinfo("Información", "No se registraron gastos.")
            return

        # Agrupar gastos por categoría o tipo
        resumen = gastos.groupby("categoria")["monto"].sum()

        gasto_total = resumen.sum()
        categorias_alerta = resumen[resumen > 0.2 * gasto_total]  # Categorías con más del 20% del total

        if categorias_alerta.empty:
            messagebox.showinfo("Alerta", "No se encontraron gastos significativos.")
        else:
            alertas = "\n".join([f"{cat}: ${monto:,.2f}" for cat, monto in categorias_alerta.items()])
            messagebox.showinfo("Alertas de Gasto",
                                f"Se detectaron gastos elevados en las siguientes categorías:\n\n{alertas}")


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

        self.boton_alerta = ttk.Button(frame, text="⚠️ Generar alerta", command=self.generar_alerta)
        self.boton_alerta.pack(pady=5, fill=tk.X)

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

    def generar_alerta(self):
        self.gestor.generar_alerta()


if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

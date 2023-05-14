import sys
from PyQt5.QtWidgets import QApplication, QDialog
from GraficasDialog import GraficasDialog
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class GraficasApplication(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = GraficasDialog()
        self.ui.setupUi(self)
        
        self.ui.guardar_dato.clicked.connect(self.registrar)
        self.ui.guardar_titulo.clicked.connect(self.registrar2)
        self.ui.genera_grafica.clicked.connect(self.graficas)
        
        self.show()
        
    def registrar(self):
        dato = []
        elemento = []
        for i in range(6):           
            dato.append(self.ui.le_datos.text())
            elemento.append(self.ui.le_elemento.text())
        
        print(dato)

    def registrar2(self):
        titulo = self.ui.le_titulo.text()
        eje_x = self.ui.le_x.text()
        eje_y = self.ui.le_y.text()
        
    def graficas(self):
        titulo = "Ventas de marcas"
        eje_x = "Marcas"
        eje_y = "Ventas"
        venta = {"Samsung" :988, "Nokia": 54, "Motorola":325, "LG":820, "iPhone": 220, "Huawei":630}
        ventas= {"Compañias":["Samsung", "Nokia", "Motorola", "LG", "iPhone", "Huawei"], "Ventas":[988, 54, 325, 820, 220, 630]}
        df = pd.DataFrame.from_dict(ventas)
        a = venta.keys()
        b = venta.values()
        
        if self.ui.m_barras.isChecked():
            #barrasmat
            plt.bar(a, b,color = "blue")
            plt.title(titulo)
            plt.ylabel(eje_y)
            plt.xlabel(eje_x)
            plt.show()
            
        elif self.ui.m_pie.isChecked():
            #piemat
            fig1, ax1 = plt.subplots()
            ax1.pie(b, labels=a, autopct='%1.1f%%',shadow=True, startangle=90)
            ax1.axis('equal')
            plt.title(titulo)
            plt.legend()
            plt.show()
            
        elif self.ui.m_linea.isChecked():
            #lineamat
            plt.plot(a, b, label = "b", linewidth = 4, color = "blue")
            #Definicion de titulo y nombres de los ejes
            plt.title(titulo)
            plt.ylabel(eje_y)
            plt.xlabel(eje_x)
            #Mostrar leyenda, cuadricula y figura
            plt.legend()
            plt.grid()
            plt.show()
            
        elif self.ui.s_barras.isChecked():
            #barraseaborn
            #Definicion de nombres de los ejes
            plt.bar(a, b,color = "blue")
            #Mostrar figura
            plt.show()
            
        elif self.ui.s_linea.isChecked(): 
            #lineaseaborn
            plt.plot(a, b, label = "b", linewidth = 4, color = "blue")
            #Definicion de titulo y nombres de los ejes
            plt.title(titulo)
            plt.ylabel(eje_y)
            plt.xlabel(eje_x)
            #Mostrar leyenda, cuadricula y figura
            plt.legend()
            plt.grid()
            plt.show()
        
        
try:
    with sqlite3.connect("BaseDeDatosGraficasDemo.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS __ ()")
        
        mi_cursor.execute("INSERT INTO __ VALUES()")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error{sys.exc_info()[0]}")
    
    
if __name__ == "__main__":
    app =  QApplication(sys.argv)
    ventana = GraficasApplication()
    ventana.show()
    sys.exit(app.exec_())
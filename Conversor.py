#App para convertir pies a metros usando tkinter.
#Leslie Rodriguez Garcia
#23/02/2023

from tkinter import*
from tkinter import ttk

class Conversor: 
    #Tipo constructor de la clase
    def __init__(self, raiz): 
        raiz.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a ").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)

        #Hacer la operacion presionando "enter"
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        piesUsuario = float(self.pies.get()) #Siempre devuelve una cadena y convierte una cadena a flotante
        print("Pies ingresados : ", piesUsuario)
        metros = piesUsuario * 0.3048
        print("Metros : ", metros)
        self.metros.set(metros)
        


if __name__=="__main__":
    print("Este es el arcivo principal.")
    print("Nada mas se mostrara esto si es el principal")         




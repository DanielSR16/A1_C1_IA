import tkinter as tk
class Formulario():
    def __init__(self):
        self.posicionX_1 = 0
        self.posicionX_2 = 0
        self.posicionY_1 = 0
        self.posicionY_2 = 0
        self.resolucion = 0
        self.tamaño_poblacion_inicial = 0
        self.tamaño_poblacion_maxima = 0
        self.probabilidad_mutacion_genetica = 0
        self.probabilidad_mutacion_individual = 0
        self.generaciones = 0

    def verificacionLlaves(self,cadena):
        self.posicionX_1 = cadena
    def vista(self):
    
        root= tk.Tk()
        canvas1 = tk.Canvas(root, width = 550, height = 600)
        canvas1.pack()

        label1 = tk.Label(root, text='Algoritmo Genetico')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(275, 25, window=label1)

        label2 = tk.Label(root, text='Ingresar Valores para X [,]')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(150, 100, window=label2)

        label3 = tk.Label(root, text='X1')
        label3.config(font=('helvetica', 10))
        canvas1.create_window(90, 140, window=label3)

        entry1 = tk.Entry (root) 
        canvas1.create_window(90, 180, window=entry1)

        label4 = tk.Label(root, text='X2')
        label4.config(font=('helvetica', 10))
        canvas1.create_window(220, 140, window=label4)

        entry3 = tk.Entry (root) 
        canvas1.create_window(220, 180, window=entry3)

        #Y
        label5 = tk.Label(root, text='Ingresar Valores para Y [,]')
        label5.config(font=('helvetica', 10))
        canvas1.create_window(425, 100, window=label5)

        label6 = tk.Label(root, text='Y1')
        label6.config(font=('helvetica', 10))
        canvas1.create_window(350, 140, window=label6)

        entry4 = tk.Entry (root) 
        canvas1.create_window(350, 180, window=entry4)

        label7 = tk.Label(root, text='Y2')
        label7.config(font=('helvetica', 10))
        canvas1.create_window(460, 140, window=label7)

        entry5 = tk.Entry (root) 
        canvas1.create_window(480, 180, window=entry5)

        label8 = tk.Label(root, text='Resolucion')
        label8.config(font=('helvetica', 10))
        canvas1.create_window(275, 230, window=label8)

        entry6 = tk.Entry (root) 
        canvas1.create_window(275, 260, window=entry6)
        
        
        label9 = tk.Label(root, text='Cantidad de poblacion inicial')
        label9.config(font=('helvetica', 10))
        canvas1.create_window(150, 290, window=label9)

        entry7 = tk.Entry (root) 
        canvas1.create_window(150, 320, window=entry7)

            
        label9 = tk.Label(root, text='Cantidad de poblacion Maxima')
        label9.config(font=('helvetica', 10))
        canvas1.create_window(400, 290, window=label9)

        entry8 = tk.Entry (root) 
        canvas1.create_window(400, 320, window=entry8)
        
        label10 = tk.Label(root, text='Probabilidad de Mutacion Genetica')
        label10.config(font=('helvetica', 10))
        canvas1.create_window(275, 350, window=label10)

        entry9 = tk.Entry (root) 
        canvas1.create_window(275, 370, window=entry9)
        
        label11 = tk.Label(root, text='Probabilidad de Mutacion Individual')
        label11.config(font=('helvetica', 10))
        canvas1.create_window(275, 400, window=label11)

        entry10 = tk.Entry (root) 
        canvas1.create_window(275, 420, window=entry10)

        label12 = tk.Label(root, text='Generaciones')
        label12.config(font=('helvetica', 10))
        canvas1.create_window(275, 460, window=label12)

        entry11 = tk.Entry (root) 
        canvas1.create_window(275, 480, window=entry11)
        
        


        def getSquareRoot():  
            self.posicionX_1 = entry1.get()
            self.posicionX_2 = entry3.get()
            self.posicionY_1 = entry4.get()
            self.posicionY_2 = entry5.get()
            self.resolucion = entry6.get()
            self.tamaño_poblacion_inicial = entry7.get()
            self.tamaño_poblacion_maxima = entry8.get()
            self.probabilidad_mutacion_genetica = entry9.get()
            self.probabilidad_mutacion_individual = entry10.get()
            self.generaciones = entry11.get()
            root.destroy()
        button1 = tk.Button(text='EJECUTAR', command=getSquareRoot,bg='brown', fg='white')
        canvas1.create_window(275, 525, window=button1)

        root.mainloop()

    
        

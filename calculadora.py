import tkinter

ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("+600+200")
ventana.resizable(width=10, height=10)
#Funciones de las operaciones matematicas
def suma():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) + int(numero[1])
            label_result["text"] = f"El resultado de la suma es {numero[2]}" 
def resta():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) - int(numero[1])
            label_result["text"] = f"El resultado de la resta es {numero[2]}" 
def multi():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) * int(numero[1])
            label_result["text"] = f"El resultado de la multiplicacion es {numero[2]}" 
def div():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) / int(numero[1])
            label_result["text"] = f"El resultado de la division es {numero[2]}"      
def expo():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) ** int(numero[1])
            label_result["text"] = f"El resultado del exponente es {numero[2]}"      
def modulo():
    label_result
    label_result.grid(row=7, column=0, columnspan=2)
    numero = [0,0,0]
    numero[0] = n1.get()
    if numero[0] == "":
        label_result["text"] = "Los valores no pueden estar vacios!"
    else:
        numero[1] = n2.get()
        if numero[1] == "":
            label_result["text"] = "Los valores no pueden estar vacios!"
        else:
            numero[2] = int(numero[0]) % int(numero[1])
            label_result["text"] = f"El resultado del modulo es {numero[2]}"      

#Labels o texto de la calculadora
label_calculadora = tkinter.Label(ventana, text="Calculadora", font="courier 15")
label_n1 = tkinter.Label(ventana, text="Ingrese el primer valor",font="courier 10") 
label_n2 = tkinter.Label(ventana, text="Ingrese el segundo valor", font="courier 10")
label_result = tkinter.Label(ventana, font="courier 10", pady=10)


#Entradas o textbox
n1 = tkinter.Entry(ventana)
n2 = tkinter.Entry(ventana)


#Botones de las operaciones
btn_sum = tkinter.Button(ventana, text="Suma", width=20, command=suma)
btn_rest = tkinter.Button(ventana, text="Resta", width=20, command=resta)
btn_mltp = tkinter.Button(ventana, text="Multiplicacion", width=20, command=multi)
btn_div = tkinter.Button(ventana, text="Division", width=20, command=div)
btn_expo = tkinter.Button(ventana, text="Exponente", width=20, command=expo)
btn_modulo = tkinter.Button(ventana, text="Modulo", width=20, command=modulo)

#Grid Metodo para manejar los espacios de la ventana como una matriz
label_calculadora.grid(row=0, column=0, columnspan=2, pady=10)
label_n1.grid(row=1, column=0, pady=5)
label_n2.grid(row=2, column=0, pady=5)
n1.grid(row=1, column=1, pady=5, padx=5)
n2.grid(row=2, column=1, pady=5, padx=5)
btn_sum.grid(row=3, column=0, pady=10)
btn_rest.grid(row=3, column=1, padx=10)
btn_mltp.grid(row=4, column=1)
btn_div.grid(row=4, column=0, pady=10)
btn_expo.grid(row=5, column=0, pady=10)
btn_modulo.grid(row=5, column=1, pady=10)


ventana.mainloop()
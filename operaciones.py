import tkinter as tk
from tkinter import simpledialog, messagebox
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3



titulo="Diagrama de venn"
# Función para mostrar diagrama de Venn para dos o más conjuntos
def mostrar_diagrama_venn(*args):
    
    plt.figure(figsize=(8, 6))
    if(args.__len__()==1):
        conjunto1=', '.join(str(n) for n in diferencia_conjuntos(args[0]))
        venn=venn2((args[0],set()), ('Conjunto A',''))
        venn.get_label_by_id('10').set_text(conjunto1)
        venn.get_label_by_id('01').set_text('')
    
    if(args.__len__()==2):
        
        conjunto1=', '.join(str(n) for n in diferencia_conjuntos(args[0], args[1]))
        conjunto2=', '.join(str(n) for n in diferencia_conjuntos(args[1], args[0]))
        
        interseccion=', '.join(str(n) for n in interseccion_conjuntos(args[0], args[1]))
        
        venn=venn2(args, ('Conjunto A', 'Conjunto B'))
        venn.get_label_by_id('10').set_text(conjunto1)
        venn.get_label_by_id('01').set_text(conjunto2)
        
        
        if (bool(interseccion)):
            venn.get_label_by_id('11').set_text(interseccion)

    if(args.__len__()==3): 
       
        conjunto1=', '.join(str(n) for n in diferencia_conjuntos(args[0], args[2],args[1]))
        conjunto2=', '.join(str(n) for n in diferencia_conjuntos(args[1], args[0],args[2]))
        conjunto3=', '.join(str(n) for n in diferencia_conjuntos(args[2], args[1],args[0]))
        
        interseccion12=', '.join(str(n) for n in diferencia_conjuntos(interseccion_conjuntos(args[0], args[1]),
                                                interseccion_conjuntos(args[0], args[1],args[2])))
        interseccion13=', '.join(str(n) for n in diferencia_conjuntos(interseccion_conjuntos(args[0], args[2]),
                                                interseccion_conjuntos(args[0], args[1],args[2])))
        interseccion23=', '.join(str(n) for n in diferencia_conjuntos(interseccion_conjuntos(args[1], args[2]),
                                                interseccion_conjuntos(args[0], args[1],args[2])))
        interseccion=', '.join(str(n) for n in interseccion_conjuntos(args[0], args[1],args[2]))
        
        venn=venn3(args, ('Conjunto A', 'Conjunto B', 'Conjunto C'))
        venn.hide_zeroes()
        venn.get_label_by_id('100').set_text(conjunto1)
        venn.get_label_by_id('010').set_text(conjunto2)
        venn.get_label_by_id('001').set_text(conjunto3)
        if (bool(interseccion12) ):
            venn.get_label_by_id('110').set_text(interseccion12)
        if (bool(interseccion13)):
            venn.get_label_by_id('101').set_text(interseccion13)
        if (bool(interseccion23)):
            venn.get_label_by_id('011').set_text(interseccion23)
        if (bool(interseccion)):
            venn.get_label_by_id('111').set_text(interseccion)
        
  
    plt.title(titulo)
    plt.show()


# Función para calcular la unión de varios conjuntos
def union_conjuntos(*args):
    union = set()
    for arg in args:
        for elemento in arg:
            if elemento not in union:
                union.add(elemento)
    return union

# Función para calcular la intersección de varios conjuntos
def interseccion_conjuntos(*args):
    interseccion = set(args[0])
    for arg in args:
            interseccionIntemedia=set()
            for elemento in interseccion:
                if elemento in arg:
                   interseccionIntemedia.add(elemento)
                   continue
            interseccion=set(interseccionIntemedia)
    return interseccion

# Función para calcular la diferencia entre varios conjuntos
def diferencia_conjuntos(*args):
    diferencia = set()
    for arg in args:
        if arg!=args[0]:
            diferenciaIntermedia=set()
            for elemento in diferencia:
                if elemento not in arg:
                    diferenciaIntermedia.add(elemento)
                    continue
            diferencia=set(diferenciaIntermedia)
        else:
            diferencia=set(args[0])
    return diferencia

# Función para calcular el complemento de un conjunto en otro conjunto universal
def complemento_conjunto_universal(conjunto_universal, conjunto):
    complemento = set()
    for elemento in conjunto_universal:
        if elemento not in conjunto:
            complemento.add(elemento)
    return complemento

# Función para calcular la combinación de dos conjuntos
def combinacion_conjuntos(*args):
    combinacion = set()
    combinacion=union_conjuntos(union_conjuntos(*args), interseccion_conjuntos(*args))
    return combinacion

# Función para calcular la cardinalidad de un conjunto
def cardinalidad_conjunto(conjunto):
    cardinalidad = len(conjunto)
    return cardinalidad

# Función para verificar si un conjunto es subconjunto de otro
def es_subconjunto(conjunto_a, conjunto_b):
    return all(elemento in conjunto_b for elemento in conjunto_a)

# Función para verificar si dos conjuntos son disjuntos
def son_disjuntos(conjunto_a, conjunto_b):
    return interseccion_conjuntos(conjunto_a, conjunto_b) == set()

def menu():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Mostrar el menú en una ventana emergente
    opcion = simpledialog.askinteger("Menú de Conjuntos", 
                                     "Seleccione una opción:\n"
                                     "1. Operaciones entre conjuntos\n"
                                     "2. Cardinalidad de un conjunto\n"
                                     "3. Subconjunto\n"
                                     "4. Conjuntos disjuntos\n"
                                     "5. Salir\n\n"
                                     "Ingrese el número de la opción deseada:")

    if opcion == 1:
        operaciones_conjuntos()
        menu()
    elif opcion == 2:
        conjunto = ingresar_conjunto("Ingrese los elementos del conjunto separados por espacios:")
        messagebox.showinfo("Cardinalidad de un conjunto", f"La cardinalidad del conjunto es: {len(conjunto)}")
        menu()
    elif opcion == 3:
        conjunto_a = ingresar_conjunto("Ingrese los elementos del primer conjunto separados por espacios:")
        conjunto_b = ingresar_conjunto("Ingrese los elementos del segundo conjunto separados por espacios:")
        if es_subconjunto(conjunto_a, conjunto_b):
            messagebox.showinfo("Subconjunto", "El primer conjunto es subconjunto del segundo conjunto.")
        else:
            messagebox.showinfo("Subconjunto", "El primer conjunto NO es subconjunto del segundo conjunto.")
        menu()
    elif opcion == 4:
        conjunto_a = ingresar_conjunto("Ingrese los elementos del primer conjunto separados por espacios:")
        conjunto_b = ingresar_conjunto("Ingrese los elementos del segundo conjunto separados por espacios:")
        if son_disjuntos(conjunto_a, conjunto_b):
            messagebox.showinfo("Conjuntos disjuntos", "Los conjuntos son disjuntos.")
        else:
            messagebox.showinfo("Conjuntos disjuntos", "Los conjuntos NO son disjuntos.")
        menu()
    elif opcion == 5:
        messagebox.showinfo("Salir", "¡Hasta luego!")
    else:
        messagebox.showerror("Error", "Opción no válida. Intente de nuevo.")
    

# Función para realizar operaciones entre conjuntos
def operaciones_conjuntos():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Pedir al usuario que ingrese la cantidad de conjuntos
    cantidad = simpledialog.askinteger("Operaciones entre conjuntos", 
                                       "Ingrese la cantidad de conjuntos que desea utilizar:")
    
    # Pedir al usuario que ingrese los elementos de cada conjunto
    conjuntos = []
    for i in range(cantidad):
        conjunto = simpledialog.askstring("Operaciones entre conjuntos", 
                                          f"Ingrese los elementos del conjunto {i+1} separados por espacios:")
        conjuntos.append(set(conjunto.split()))

    # Mostrar las operaciones en una ventana emergente
    opcion = simpledialog.askinteger("Operaciones entre conjuntos", 
                                     "Seleccione la operación que desea realizar:\n"
                                     "1. Unión de conjuntos\n"
                                     "2. Intersección de conjuntos\n"
                                     "3. Diferencia entre conjuntos\n"
                                     "4. Complemento de un conjunto en otro conjunto universal\n"
                                     "5. Combinación de dos conjuntos\n\n"
                                     "Ingrese el número de la opción deseada:")
    
    if opcion == 1:
        resultado = union_conjuntos(*conjuntos)
    elif opcion == 2:
        resultado = interseccion_conjuntos(*conjuntos)
    elif opcion == 3:
        resultado = diferencia_conjuntos(*conjuntos)
    elif opcion == 4:
        conjunto_universal = ingresar_conjunto("Ingrese los elementos del conjunto universal separados por espacios:")
        conjunto = ingresar_conjunto("Ingrese los elementos del conjunto para calcular su complemento:")
        resultado = complemento_conjunto_universal(conjunto_universal, conjunto)
    elif opcion == 5:
        resultado = combinacion_conjuntos(*conjuntos)
    else:
        messagebox.showerror("Error", "Opción no válida. Intente de nuevo.")
        return

    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado}")

     # Mostrar el diagrama de Venn para la operación realizada
    mostrar_diagrama_venn(*conjuntos)
    mostrar_diagrama_venn(resultado)

# Función para ingresar un conjunto desde la entrada del usuario
def ingresar_conjunto(mensaje):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    conjunto = simpledialog.askstring("Ingreso de conjunto", mensaje)
    return set(conjunto.split())

# Ejecutar el menú
menu()


# Ejemplo de uso
# conjunto_a = {1, 2, 3, 4, 5}
# conjunto_b = {2 ,4, 5, 6, 7, 8}
# conjunto_c = {1, 2, 4,8, 9}
#conjunto_d = {9,10}

#print(interseccion_conjuntos(   conjunto_a,conjunto_b,conjunto_c))

#print(union_conjuntos(   conjunto_a,conjunto_b,conjunto_c,conjunto_d))

#print(diferencia_conjuntos(   conjunto_c,conjunto_a,conjunto_b))

#print(son_disjuntos(   conjunto_a,conjunto_b))

#mostrar_diagrama_venn(conjunto_d)
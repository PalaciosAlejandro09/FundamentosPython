def nuevoTema(tema):
    print("\n========", tema, "=======\n")
#Esto es un comentario

if __name__ == "__main__":
    nuevoTema("Operadores Aritmeticos")
    print("Operacion de division entera (10 //3 )" , 10/3)
    print("operador de potencias (5 * 5): ", 5 * 5 )
    print("Operador de cambios de signo(-5): ", -5)

    nuevoTema("=====Operadores logicos====")
    print("Operador and (true and false): ", True and False)
    #Actividad: Mostrar las tablas de verdad de los operadores Logicos.

    print("Operador and : ", True and False)
    print("Operador and : ", True and True)
    print("Operador and : ", False and True)
    print("Operador and : ", False and False)

    print("Operador or : ", True and False)
    print("Operador or : ", True and True)
    print("Operador or : ", False and True)
    print("Operador or : ", False and False)

    print("Operador not : ", not False)
    print("Operador not : ", not True)

    print("***Operadores de comparacion**")
    print("2==3", 2==3)
    print("Menor que<: 2 < 3", 2 < 3 )
    print("Mayor que >: 3 > 2", 3 > 2)
    print("Menor o igual que 2 <= 2", 2 <= 2)
    print("Mayor o igual que 3>=2", 3 >= 2 )

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 34.2
    variable3 = "Pepe"
    dos_palabras = "Hola"
    dosPalabras = "Hello"

    print(variable1, _variable2, variable3 , dos_palabras, dosPalabras)

    a, b, c = 98, 3.1416, "Bienvenido"
    print(a, b, c)

    nuevoTema("Enteros")
    w = 196
    x = 46526246246146
    y = -896
    z = 0b0011011 #numero en binario
    h = 0xffa #entero en hexadecimal 

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("flotantes")
    x = 1297.5
    print(x,type(x))
    y = 0.052829
    print(y,type(y))

    nuevoTema("numeros complejos")
    x = 46j
    y = 12+45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("listas")
    a = [10, 20.5, "python list"]
    print(a)
    a = ["listas2", 45, 16.2]
    print(a)

    nuevoTema("tuplas")
    t= (25,"tuplas", 5.6)
    print(t)
    print(t[1])

    nuevoTema("conjuntos")
    c= (50, 20, 10, 4, 8, 50 )
    print(c)

    nuevoTema("Diccionario")
    d = {1:"valor1", "2":45}
    print(d,type(d))

    nuevoTema("Cadenas")
    cadena1 = "Cadena entre comillas dobles"
    print(cadena1)
    cadena2 = "cadena entre comillas sencillas"
    print(cadena2)
    cadena3 = ''' cadena de 
    varias
    lineas'''
    print(cadena3)
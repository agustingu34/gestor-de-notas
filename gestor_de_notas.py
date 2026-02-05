notas=[]
while True:
    print("\n1 - Agregar")
    print("2 -Ver notas")
    print("3 - Promedio")
    print("4 - Borrar ultima nota")
    print("5 - Salir")
    usuario=int(input("Elija una opcion: "))
    if usuario==5:
        print("fin del programa.")
        break
    elif usuario==1:
        a=int(input("agregar notas: "))
        notas.append(a)
        print("Agregado: ",notas)
    elif usuario==2:
        print(notas)
    elif usuario==3:
        if len(notas)==0:
            print("No hay notas cargadas.")
        else:
            promedio=sum(notas)/len(notas)
            print(f"El promedio es: {promedio}")
    elif usuario==4:
        if notas:
            notas.pop()
            print("Se elimino la ultima nota agregada")
        elif len(notas)==0:
            print("no hay notas.")
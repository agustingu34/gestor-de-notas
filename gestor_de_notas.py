notas=[]
try:
    with open("notas.txt", "r") as f:
        for linea in f:              
            notas.append(int(linea.strip()))
except:
    pass
while True:
    print("\n1 - Agregar")
    print("2 -Ver notas")
    print("3 - Promedio")
    print("4 - Borrar ultima nota")
    print("5 - Guardar al Salir")
    usuario=int(input("Elija una opcion: "))
    if usuario==5:
        with open("notas.txt","w") as f:
            for nota in notas:
                f.write(str(nota)+ "\n")
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
            print("Se elimino la ultim anota agregada")
        elif len(notas)==0:
            print("no hay notas.")

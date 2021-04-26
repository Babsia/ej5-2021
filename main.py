from Menu import Menu
if __name__=='__main__':
    bandera = False
    m=Menu()
    while not bandera:
        print("")
        print("a listado de porcentaje por alumnos")
        print("b modificar la cantidad maxima de inasitencias")
        print("c salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='c'
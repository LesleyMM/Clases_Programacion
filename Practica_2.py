if __name__ == '__main__':
    print(' Opciones a elegir: \n 1.- Mover archivos. \n 2.- Borrar archivos. \n 3.- Renombrar archivos. \n 4.- Crear archivo. \n Cualquier numero para cerrar. ')

    Mover_archivos = 1 
    Borrar_archivos = 2
    Renombrar_archivos = 3
    Crear_archivo = 4
    
    Opcion = float(input(' Que opcion necesitas: '))

    if Mover_archivos == Opcion:
        print(' Se movieron los archivos: ')
    
    elif Borrar_archivos == Opcion:
        archivo = input(' Nombre del archivo: ')
        print(' Se borro el archivo ' + archivo )

    elif Renombrar_archivos == Opcion:
        archivo = input(' Nombre del archivo a renombrar: ')
        archivo_2 = input(' Nuevo nombre: ')
        print(' Se cambio el nombre a ' + archivo_2)

    elif Crear_archivo == Opcion:
        archivo = input(' Nombre del archivo: ')
        print(' Se creo archivo ' + archivo)

    else: 
        print(' Adios. ')
        




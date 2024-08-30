from os import system
from mascotas import Mascota

def main():
    try:
        while True:
            print('\n*************** MENU MASCOTAS ********************\n')

            print('\t1 -Registrar nueva mascota')
            print('\t2 -Buscar una mascota por el ID')
            print('\t3 -Buscar una mascota por el nombre')
            print('\t4 -Mostar todas las mascotas')
            print('\t5 -Actualizar mascota')
            print('\t6 -Eliminar una mascota')
            print('\t7 -Salir del sistema')

            print('\n*************** MENU MASCOTAS ********************')
            while True:
                try:
                    opcion = int(input('\n\tSeleccione una opción: '))
                    break
                except ValueError:
                    print('Opción no válida')

            if opcion == 7:
                print('Gracias por usar nuestra app..')
                break
            
            elif opcion == 1:
                system('cls')
                mascota1 = Mascota()
                mascota1.registrar_mascota()
            
            elif opcion == 2:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de mascota a buscar: '))
                mascota1.buscar_mascota(codigo_mascota)
                
            elif opcion == 3:
                system('cls')
                mascota1 = Mascota()
                nombre_mascota = input('Nombre de la mascota a buscar: ')
                mascota1.buscar_mascota_nombre(nombre_mascota)
                
            elif opcion == 4:
                system('cls')
                mascota1 = Mascota()
                mascota1.obtener_mascotas()
                
                
            elif opcion == 5:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de la mascota a actualizar: '))
                mascota1.actualizar_mascota(codigo_mascota)
            

            elif opcion == 6:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de mascota que desea eliminar: '))
                mascota1.eliminar_mascota(codigo_mascota)
                
              
            else:
                system('cls')
                print('Opción no válida. Intente de nuevo')
    
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continue')
    except Exception as error:
        print(f'Ha ocurrido error no codificado {error}')
    finally:
        print('Intente de nuevo')

if __name__ == "__main__":
    main()

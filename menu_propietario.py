from os import system
from propietarios import Propietarios

def main():
    try:
        while True:
            print('\n*************** MENU PROPIETARIOS ********************\n')

            print('\t1 -Registrar propietario')
            print('\t2 -Consultar el propietario por el ID')
            print('\t3 -Consultar el propietario por el nombre')
            print('\t4 -Actualizar propietario')
            print('\t5 -Eliminar propietario')
            print('\t6 -Salir del sistema')

            print('\n*************** MENU MASCOTAS ********************')
            while True:
                try:
                    opcion = int(input('\n\tSeleccione una opción: '))
                    break
                except ValueError:
                    print('Opción no válida')

            if opcion == 6:
                print('Gracias por usar nuestra app..')
                break
            
            elif opcion == 1:
                system('cls')
                print('1. Registrar Propietario')
                propietarios = Propietarios()
                propietarios.registrar_propietario()
            
            elif opcion == 2:
                system('cls')
                propietarios = Propietarios()
                propietario = int(input('Ingrese el Id del propietario: '))
                propietarios.buscar_propietarioid(propietario)
                
            elif opcion == 3:
                system('cls')
                propietarios = Propietarios()
                propietario = input('Nombre del propietario: ')
                propietarios.buscar_propietarionombre(propietario)
                
            elif opcion == 4:
                system('cls')
                propietarios = Propietarios()
                propietario = int(input('Id de usuario para actualizar: '))
                propietarios.actualizar_propietario(propietario)

            elif opcion == 5:
                system('cls')
                propietarios = Propietarios()
                propietario = input('Ingrese el código del propietario: ')
                propietarios.eliminar_propietarioid(propietarios)
     
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

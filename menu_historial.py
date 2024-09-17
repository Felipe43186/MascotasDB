from os import system
from historial_medico import Historial_medico

def main():
    try:
        while True:
            print('\n*************** MENU HISTORIAL MEDICOS ********************\n')
            print('\t1 - Registrar historial medico')
            print('\t2 - Consultar historial medico por el codigo')
            print('\t3 - Actualizar historial medico')
            print('\t4 - Eliminar historial medico')
            print('\t5 - Salir del sistema')

            print('\n*************** MENU HISTORIAL MEDICO ********************')
            opcion = int(input('\n\tSeleccione una opción: '))
            if opcion == 5:
                print('Gracias por usar nuestra app..')
                break


            elif opcion == 1:
                system('cls')
                historial_medico = Historial_medico()
                historial_medico.registrar_historial()


            elif opcion == 2:
                system('cls')
                historial_medico = Historial_medico()
                codigo_historial = input('Ingrese el código del historial médico: ')
                historial_medico.buscar_historialid(codigo_historial)


            elif opcion == 3:
                system('cls')
                historial_medico = Historial_medico()
                codigo_historial = input('Ingrese el código del historial médico: ')
                historial_medicos.actualizar_historial(codigo_historial)

            
            elif opcion == 4:
                system('cls')
                historial_medicos = Historial_medico()
                codigo_historial = input('Ingrese el código del historial médico: ')
                historial_medicos.eliminar_historial(codigo_historial)

    
    except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
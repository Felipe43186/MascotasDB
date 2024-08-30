from os import system
from administradores import Administradores


@staticmethod
def menu_administradores():
    try:
         while True:
             print('\n----------------------------Menu Administradores----------------------------')
             print('\t1. Agregar Administrador')
             print('\t2. Consultar Administrador Por ID')
             print('\t3. Consultar Administrador Por Nombre')
             print('\t4. Consultar Todos Los Administradores')
             print('\t5. Actualizar Administrador Por ID')
             print('\t6. Eliminar Administrador Por ID')
             print('\t7. Volver al Menu Principal')
             
             print('\n----------------------------Menu Administradores----------------------------')
             while True:
                 try:
                     opcion = int(input('\t\nIngrese una opción: '))
                     break
                 
                 except ValueError:
                     print('Opcion invalida. Intente nuevamente.')
                     
             if opcion == 7:
                 print('Gracias por usar nuestro programa ')
            
             elif opcion == 1:
                 system('cls')
                 administrador1 = Administradores()
                 administrador1.InsertarAdministrador()
            
             elif opcion == 2:
                 system ('cls')
                 adminsitrador1 = Administradores()
                 codigo_administrador = int(input('Codigo de administrador a buscar: '))
                 administrador1.buscar_administradorid(codigo_administrador)
                 
             elif opcion == 3:
                 system('cls')
                 administrador1 = Administradores()
                 nombre_administrador = input('Nombre de administrador a buscar: ')
                 administrador1.buscar_adminitradornombre()
            
             elif opcion == 4:
                 system('cls')
                 administrador1 = Administradores()
                 administrador1.consultar_todos_admin()
                 
             elif opcion == 5:
                 administrador1 = Administradores()
                 codigo_administrador = int(input('Codigo de administrador a actualizar: '))
                 administrador1.actualizar_admin(codigo_administrador)
             
             elif opcion == 6:
                 administrador1 = Administradores()
                 codigo_administrador = int(input('Codigo de administrador a eliminar: '))
                 administrador1.eliminar_administradoid()
                 
             else: 
                 system('cls')
                 print('Opcion no válida. Intente de nuevo')
                     
    except KeyboardInterrupt:
        print('Caracter no valido')
    
    except Exception as error:
        print('Ha ocurrido error no codificado {error} ')
        
    finally:
        print('Intente de nuevo')

if __name__ == "__main__":
    menu_administradores()
    
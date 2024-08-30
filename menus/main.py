from conexion10 import BaseDatos
class menu:
    @staticmethod

    
    def menu_principal():
        
        print('----------------------------Menu Principal----------------------------')
        print('1. Propietarios')
        print('2. Veterinarios')
        print('3. Administradores')
        print('4. Mascotas')
        print('5. Historiales Medicos')
        print('6. Productos')
        print('7. Citas Medicas')
        print('8. Servicios')
        print('9. Salir')
        
        opcion = input('Por favor seleccione una opcion:')
       
        if opcion == 1:
            menu.menu_propietarios()
        
        elif opcion == 2:
            menu.menu_veterinarios()
            
        elif opcion == 3:
            menu.menu_administradores()
        
        elif opcion == 4:
            menu.menu_mascotas()
        
        elif opcion == 5:
            menu.menu_historiales_medicos()
        
        elif opcion == 6:
            menu.menu_productos()
            
        elif opcion == 7:
            menu.menu_citas_medicas()
            
        elif opcion == 8:
            menu.menu_servicios()
            
        elif opcion == 9:
            print('Saliendo del programa...')
            BaseDatos.desconectar()
        
    
    @staticmethod
    def menu_propietarios():
        
        print('----------------------------Menu Propietarios----------------------------')
        print('1. Agregar Propietario')
        print('2. Consultar Propietario Por ID')
        print('3. Consultar Propietario Por Nombre')
        print('4. Consultar Todos Los Propietarios')
        print('5. Actualizar Propietario Por ID')
        print('6. Eliminar Propietario Por ID')
        print('7. Volver al Menu Principal')
        
        
    @staticmethod
    def menu_veterinarios():
        
        print('----------------------------Menu Veterinarios----------------------------')
        print('1. Agregar Veterinario')
        print('2. Consultar Veterinario Por Nombre')
        print('3. Consultar Veterinario Por ID')
        print('4. Consultar Los Veterinarios')
        print('5. Actualizar Veterinario Por ID')
        print('6. Eliminar Veterinario Por ID')
        print('7. Volver al Menu Principal')
        
    @staticmethod
    def menu_administradores():
        
        print('----------------------------Menu Administradores----------------------------')
        print('1. Agregar Administrador')
        print('2. Consultar Administrador Por ID')
        print('3. Consultar Administrador Por Nombre')
        print('4. Consultar Todos Los Administradores')
        print('5. Actualizar Administrador Por ID')
        print('6. Eliminar Administrador Por ID')
        print('7. Volver al Menu Principal')
        
    @staticmethod
    def menu_mascotas():
        
        print('----------------------------Menu Mascotas----------------------------')
        print('1. Agregar Mascota')
        print('2. Consultar Mascota ')
        print('3. Consultar Mascota Por Nombre')
        print('4. Consultar Todas Las Mascotas')
        print('5. Actualizar Mascota Por ID')
        print('6. Eliminar Mascota Por ID')
        print('7. Volver al Menu Principal')
        
    @staticmethod
    def menu_historial_medico():
        
        print('----------------------------Menu Historial Medico----------------------------')
        print('1. Agregar Historial Medico')
        print('2. Consultar Historial Medico Por ID')
        print('3. Consultar Historial Medico Por Mascota')
        print('4. Consultar Todos Los Historiales Medicos')
        print('4. Actualizar Historial Medico Por Mascota')
        print('5. Eliminar Historial Medico ')
        print('6. Volver al Menu Principal')
        
    @staticmethod
    def menu_productos():
        
        print('----------------------------Menu Productos----------------------------')
        print('1. Agregar Producto')
        print('2. Consultar Producto Por Codigo')
        print('3. Consultar Producto Por Nombre')
        print('4. Consultar Todos Los Productos')
        print('5. Eliminar Producto')
        print('6. Volver al Menu Principal')
        
    @staticmethod
    def menu_citas_medicas():
        
        print('----------------------------Menu Citas Medicas----------------------------')
        print('1. Agregar Cita Medica')
        print('2. Consultar Cita Medica Por Fecha')
        print('3. Consultar Cita Medica Por Mascota')
        print('4. Consultar Todas Las Citas Medicas')
        print('5. Actualizar Cita Medica Por Mascota')
        print('6. Eliminar Historial Cita Medica Por Codigo')
        print('7. Volver al Menu Principal')
        
    @staticmethod
    def menu_servicios():   
        
        print('----------------------------Menu Servicios----------------------------')
        print('1. Agregar Servicio')
        print('2. Consultar Servicio Por Codigo')
        print('3. Consultar Servicio Por Nombre')
        print('4. Consultar Todos Los Servicios')
        print('5. Eliminar Servicio Por ID')
        print('6. Volver al Menu Principal')
        

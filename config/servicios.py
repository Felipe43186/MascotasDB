from conexion10 import BaseDatos

class Servicios:
    
    def __init__(self, 
                 codigo_servicio: int,
                 nombre: str, 
                 descripcion: str, 
                 precio:float):
        
        self.__codigo_servicio = codigo_servicio
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        
        
    def get_codigo_servicio(self):
        return self.__codigo_servicio
    
    
    def set_codigo_servicio(self,codigo_servicio):
        self.__codigo_servicio = codigo_servicio
        
        
    def get_nombre(self):
        return self.__nombre
    
    
    def set_nombre(self):
        self.__nombre = input('Ingrese el nombre del servicio: ')
        
        
    def get_descripcion(self):
        return self.__descripcion
    
    
    def set_descipcion(self):
        self.__descripcion = input('Ingrese la descripción del servicio: ')
        
        
    def get_precio(self):
        return self.__precio
    
    
    def set_precio(self):
        while True:
            try:
                precio = float(input('Ingrese el precio del servicio: '))
                if precio > 0:
                    self.__precio = precio
                    break
                else:
                    print('El precio debe ser mayor a 0.')
            except ValueError:
                print('Ingresar un número válido.')
        
        
    def capturar_datos(self):
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()


    def registrar_servicio(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('InsertarServicio', [
                    self.__codigo,
                    self.__nombre,
                    self.__descripcion,
                    self.__precio,
                ])
                conexion.commit()
                print('Servicio registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
                
    def buscar_servicio_por_codigo(self, codigo_servicio):
        if codigo_servicio is None:
            self.set_codigo()
            codigo_servicio = self.__codigo
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicioPorCodigo', [codigo_servicio])
                print('Búsqueda de servicio completada.')
                for result in cursor_servicio.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:')
                        print('-------------------------------------------------------------------------')
                        print("\033[;36m" +
                            f"| {'Codigo':<15}: {fila[0]:<20} | {'Nombre':<15}: {fila[1]:<30}\n" +
                            f"| {'Descripción':<15}: {fila[2]:<50}\n" +
                            f"| {'Precio':<15}: {fila[3]:<20}\n" +
                            '\033[0;m')
                        print('-------------------------------------------------------------------------')                        
                        fila = result.fetchone()  
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    
    def buscar_servicio_nombre(self, nombre_servicio):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicioPorNombre', [nombre_servicio])  
                print('Búsqueda del servicio completada.')
                servicio_encontrado = False
                for result in cursor_servicio.stored_results():
                    filas = result.fetchone()
                    if filas:
                        servicio_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('-------------------------------------------------------------------------')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20}\n" +
                                '\033[0;m')
                            print('-------------------------------------------------------------------------')
                if not servicio_encontrado:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    
    def mostrar_servicios(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicios') 
                print('Listado de todas los servicios completados.')
                cita_encontrada = False
                for result in cursor_servicio.stored_results():
                    filas = result.fetchall()
                    if filas:
                        cita_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('*****************************************************************************')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20}\n" +
                                '\033[0;m')
                            print('*****************************************************************************')
                if not cita_encontrada:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    
    def actualizar_servicio(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('ActualizarServicio', [
                    self.__codigo,
                    self.__nombre,
                    self.__descripcion,
                    self.__precio,
                ])
                conexion.commit()
                print('Servicio actualizado correctamente...')
            except Exception as e:
                print(f'Error al actualizar el servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    def eliminar_servicio(self, codigo_servicio):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('EliminarServicio', [codigo_servicio])
                conexion.commit()
                print('Servicio borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
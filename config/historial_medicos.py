from datetime import datetime
from conexion10 import BaseDatos

class HistorialMedicos:
    def __init__(self, codigo_historial: int, fecha_entrada: datetime, descripcion: str, tratamiento: str, codigo_mascota: int):
        self.__codigo_historial = codigo_historial
        self.__fecha_entrada = fecha_entrada
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
        self.__codigo_mascota = codigo_mascota

    
    def get_codigo_historial(self):
        return self.__codigo_historial
    

    def set_codigo_historial(self):
        while True:
            try:
                codigo_historial = int(input('Ingerese el codigo de la mascota-> '))
                if (1 <= codigo_historial <= 1000000000):
                    self.__codigo_historial = codigo_historial
                else:
                    print('El número debe estar entre 3 y 100000000')
            except ValueError:
                    print('El código debe ser un número.')
            except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
            
    
    def get_fecha_entrada(self):
        return self.__fecha_entrada
    

    def set_fecha_entrada(self):
        while True:
            try:
                fecha_entrada = int(input('Digite la fecha de hoy: '))
                fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
                print(f'Fecha ingresada: {fecha_entrada.date()}')
                return fecha_entrada.date() 
            except ValueError:
                print('Invalido. Por favor use el formato YYYY-MM-DD')


    def get_descripcion(self):
        return self.__descripcion
    

    def set_descripcion(self):
        while True:
            descripcion = input('Ingrese la descripcion del historial: ')
            if len(descripcion) >= 10 and len(descripcion) <= 255:
                self.__descripcion = descripcion
                break
            else:
                print('La descripcion debe tener entre 10 y 255 caracteres.')


    def get_tratamiento(self):
        return self.__tratamiento
    

    def set_tratamiento(self):
        while True:
            tratamiento = input('Ingrese el tratamiento de la mascota: ')
            if len(tratamiento) >= 10 and len(tratamiento) <= 255:
                self.__tratamiento = tratamiento
                break
            else:
                print('El tratamiento debe tener entre 10 y 255 caracteres.')


    def get_codigo_mascota(self):
        return self.__codigo_mascota


    def set_codigo_mascota(self, codigo_mascota):
        while True:
            try:
                codigo_mascota = int(input('Ingrese el ID de mascota: ')) 
                if 1 <= codigo_mascota <= 1000000000:
                    self.__codigo_historial = codigo_mascota
                    break 
                else:
                    print("El ID debe estar entre 1 y 1,000,000,000.")
            except ValueError:
                print("ID debe ser un número entero.")



    def capturar_datos(self):
        self.set_codigo_historial()
        self.set_fecha_entrada()
        self.set_descripcion()
        self.set_tratamiento()
        self.set_codigo_mascota()


    def registrar_histirial_medico(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('InsertarHistorialMedico', [
                    self.__codigo_historial,
                    self.__fecha_entrada,
                    self.__descripcion,
                    self.__tratamiento,
                    self.__codigo_mascota
                ])
                print('Historial médico registrado correctamente.')
            except Exception as e:
                print(f'Error al registrar historial médico: {e}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()
    

    def buscar_historial_codigo(self,codigo_historial):
        if conexion:
            conexion = BaseDatos.conectar()
            try:
                cursor_historial = conexion.cursor()      
                cursor_historial.callproc('BuscarHistorialPorCodigo', [codigo_historial])
                print('Búsqueda de historial completado.')
                for result in cursor_historial.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('=============================================================================================================================================================================================================================================')
                        print("\033[;36m" +
                            f"| Codigo:{fila[0]} | Fecha:{fila[1]} | Descripcion:{fila[2]} | Tratamiento:{fila[3]} | Codigo_mascota:{fila[4]}" +
                            '\033[0;m')
                        print('=============================================================================================================================================================================================================================================')
                        return fila         
            except Exception as e:
                print(f'Error al buscar historial: {e}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()


    def actualizar_historial(self,codigo_historial = None):
        if conexion:
            conexion = BaseDatos.conectar()
            try:
                cursor_historial = conexion.cursor()
                self.buscar_historial(codigo_historial)
                cursor_historial.callproc('ActualizarHistorial', [self.codigo_historial, self.fecha_entrada, self.descripcion, self.tratamiento, self.codigo_mascota])
                print('Actualización de historial completado.')
                for result in cursor_historial.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('=============================================================================================================================================================================================================================================')
                        print("\033[;36m" +
                            f"| Codigo:{fila[0]} | Fecha:{fila[1]} | Descripcion:{fila[2]} | Tratamiento:{fila[3]} | Codigo_mascota:{fila[4]}" +
                            '\033[0;m')
                        print('=============================================================================================================================================================================================================================================')
                conexion.commit()
            except Exception as e:
                print(f'Error al actualizar historial: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()
         

    def eliminar_historial(self,eliminar_historial):
         if conexion:
            conexion = BaseDatos.conectar()
            cursor_historial = conexion.cursor()
            self.eliminar_historial(eliminar_historial)
            cursor_historial.callproc('EliminarHistorial', [self.eliminar_historial,self.codigo_mascota])
            print('Historial Eliminado')
            conexion.commit()
            if conexion:
                cursor_historial.close()
                BaseDatos.desconectar()
            



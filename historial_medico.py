from conexion1 import BaseDatos
import datetime 
from mascota import Mascota 
class Historial_medico(Mascota):
    def __init__(
            self,
            codigo: int = None,
            codigo_mascota: int = None,
            fecha: datetime.datetime = None,
            descripcion: str = None,
            tratamiento: str = None,
            **kwargs
            ):
            super().__init__**kwargs 
            self.__codigo = codigo
            self.__codigo_mascota = codigo_mascota
            self.__fecha = fecha
            self.__descripcion = descripcion
            self.__tratamiento = tratamiento
    # GET y SET

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self):
            while True:
                try:
                    codigo_producto = int(input('Escriba el código del producto =>'))
                    if (1 <= codigo_producto <= 1000000000):
                        self.__codigo = codigo_producto
                        break
                    else:
                        print('El número debe estar entre 3 y 100000000')
                except ValueError:
                    print('El código debe ser un número.')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
 
    def get_codigo_mascota(self):
        return self.__codigo_mascota

    def set_codigo_mascota(self):
        while True:
            try:
                codigo_mascota = int(input('Codigo del producto =>'))
                if len(codigo_mascota)>1100000:
                    self.__codigo_mascota = codigo_mascota
                    break
                else:
                    print('Codigo incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_fecha(self):
        return self.__fecha
  
    def set_fecha(self):
        while True:
            try:
                fecha_entrada = (input('Digite la fecha: '))
                fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
                print(f'Fecha => {fecha_entrada.date()}')
                return fecha_entrada.date() 
            except ValueError:
                print('Invalido. Por favor use el formato YYYY-MM-DD')


    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self):
        while True:
            try:
                descripcion= str(input('ingrese la descripcion =>'))
                # Verificar que solo contenga letras y espacios y que la longitud esté entre 3 y 30 caracteres
                if 3 <= len(descripcion) <= 5000000:
                    self.__descripcion = descripcion
                    break
                else:
                    print('Descrripcion incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
  
    def get_tratamiento(self):
        return self.__tratamiento

    def set_tratamiento(self):
        while True:
            try:
                tratamiento = str(input('Ingrese el tratamiento =>'))
                if 0 <= tratamiento <= 10000000:
                    self.__tratamiento = tratamiento
                    break
                else:
                    print('cantidad no válida')
            except ValueError:
                print('cantidad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                

    def capturar_datos(self):
           super().capturar_datos
           self.set_codigo()
           self.set_codigo_mascota()
           self.set_fecha()
           self.set_descripcion()
           self.set_tratamiento()
        
    def registrar_historial(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_historial = conexion.cursor()
            cursor_historial.callproc('InsertarHistorial', [
                self.get_codigo(),
                self.get_codigo_mascota(),
                self.get_fecha(),
                self.get_descripcion(),
                self.get_descripcion(),
                self.get_tratamiento()
            ])
            conexion.commit()
        print('Historial registrado correctamente...')
        if conexion:
            BaseDatos.desconectar()

    def buscar_historialid(self, codigo_historial=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                historial_encontrada = False
                cursor_historial = conexion.cursor()
                print(f'Buscando producto {codigo_historial}...')
                cursor_historial.callproc('ConsultarHistorialId', [codigo_historial])
                for busqueda in cursor_historial.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        historial_encontrada = True
                        print(historial_encontrada)
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return historial_encontrada
                    else:
                        print('Producto no encontrado. Intente de nuevo.')
                        print(historial_encontrada)
                        return historial_encontrada
            except Exception as e:
                print(f'Error al buscar el historial: {e}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()

    def actualizar_historial(self, codigo_historial):
        conexion = BaseDatos.conectar()
        historial_encontrada = self.buscar_historialid(codigo_historial)
        if historial_encontrada:
            try:
                print('Escriba los nuevos datos del historial=> ')
                self.set_fecha()
                self.set_descripcion()
                self.set_tratamiento()
                
                nueva_fecha = self.get_fecha()
                nueva_descripcion = self.get_descripcion()
                nueva_tratamiento = self.get_tratamiento()
                
                print(f'Código => {codigo_historial}')
                print(f'Nueva fecha=> {nueva_fecha}')
                print(f'Nueva descripción> {nueva_descripcion}')
                print(f'Nuevo tratamiento=> {nueva_tratamiento}')
                

                cursor_historial = conexion.cursor()
                cursor_historial.callproc('ActualizarHistorial', [
                    codigo_historial,
                    nueva_fecha,
                    nueva_descripcion,
                    nueva_tratamiento                         
                ])
                conexion.commit()
                cursor_historial.close()
                print('Historial actualizada')
            except Exception as error:
                print(f'Error al actualizar el historial: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('error no encontrada. Intente otra vez')

    def eliminar_historial(self, codigo_historial):
        conexion = BaseDatos.conectar()
        historial_encontrada = self.buscar_historialid(codigo_historial)
        if historial_encontrada:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('EliminarHistorial', [codigo_historial])
                conexion.commit()
                cursor_historial.close()
                print('historial eliminado')
            except Exception as error:
                print(f'Error al eliminar el historial: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
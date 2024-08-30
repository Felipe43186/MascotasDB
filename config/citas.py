from conexion10 import BaseDatos
import datetime

class Citas:
    
    def __init__(self,
                 codigo_cita: int = None,
                 fecha: str = None,
                 hora: datetime.datetime = None,
                 codigo_servicio: int = None,
                 id_usuario: int = None,
                 codigo_mascota: int = None,
                 estado: str = None
                 ):
        
        self.__codigo_cita = codigo_cita
        self.__fecha = fecha
        self.__hora = hora    
        self.__codigo_servicio  = codigo_servicio
        self.__id_usuario = id_usuario
        self.__codigo_mascota = codigo_mascota
        self.__estado = estado
       
        
    def get_codigo_cita(self):
        return self.__codigo_cita
    
    
    def set_codigo_cita(self):
        while True:
                codigo_cita = int(input('Ingrese el código de la cita: '))
                if codigo_cita >= 3 and codigo_cita <= 9999999:
                    self.__codigo_cita = codigo_cita
                    break
                else:
                    print('El código de la cita debe estar entre 3 y 9999999.')
                    
                    
    def get_fecha(self):
        return self.__fecha
    
    
    def set_fecha(self):
        while True:
                fecha = input('Ingrese la fecha de la cita (YYYY-MM-DD): ')
                try:
                    datetime.datetime.strptime(fecha, '%Y-%m-%d')
                    self.__fecha = fecha
                    break
                except ValueError:
                    print('La fecha ingresada no es válida. Ingrese de nuevo.')
                    
                    
    def get_hora(self):
        return self.__hora
    
    
    def set_hora(self):
        while True:
                hora = input('Ingrese la hora de la cita (HH:MM:SS): ')
                try:
                    datetime.datetime.strptime(hora, '%H:%M:%S')
                    self.__hora = datetime.datetime.strptime(hora, '%H:%M:%S')
                    break
                except ValueError:
                    print('La hora ingresada no es válida. Ingrese de nuevo.')
                    
                    
    def get_codigo_servicio(self):
        return self.__codigo_servicio


    def set_codigo_servicio(self):
        while True:
                codigo_servicio = int(input('Ingrese el código del servicio: '))
                if codigo_servicio >= 1 and codigo_servicio <= 9999999:
                    self.__codigo_servicio = codigo_servicio
                    break
                else:
                    print('El código del servicio debe estar entre 3 y 9999999.')


    def get_id_usuario(self):
        return self.__id_usuario
    
    
    def set_id_usuario(self):
        while True:
                id_usuario = int(input('Ingrese el código del usuario: '))
                if id_usuario >= 3 and id_usuario <= 9999999:
                    self.__id_usuario = id_usuario
                    break
                else:
                    print('El código del usuario debe estar entre 3 y 9999999.')
                    
                    
    def get_codigo_mascota(self):
        return self.__codigo_mascota
    
    
    def set_codigo_mascota(self):
        while True:
                codigo_mascota = int(input('Ingrese el código de la mascota: '))
                if codigo_mascota >= 3 and codigo_mascota <= 9999999:
                    self.__codigo_mascota = codigo_mascota
                    break
                else:
                    print('El código de la mascota debe estar entre 3 y 9999999.')
                    
    def get_estado(self):
        return self.__estado
    
    
    def set_estado(self):
        while True:
                estado = input('Ingrese el estado de la cita (Realizada, Pendiente, Cancelada): ')
                if estado.lower() in ['Pendiente','Confirmada','En Curso','Finalizada','Cancelada','Reprogramada','No Presentado']:
                    self.__estado = estado
                    break
                else:
                    print('El estado de la cita debe ser Realizada, Pendiente o Cancelada.')      
                    
    def capturar_datos(self):
        self.set_fecha()
        self.set_hora()
        self.codigo_servicio()
        self.id_usuario()
        self.get_codigo_mascota()
        self.estado()
        
                        
    def guardar_cita(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_cita = conexion.cursor()
            cursor_cita.callproc('InsertarCita', [
                self.get_fecha(), 
                self.get_hora(), 
                self.get_codigo_servicio(), 
                self.get_id_usuario(),
                self.get_codigo_mascota(), 
                self.get_estado()
                ])
            print('Cita registrada con éxito')
            conexion.commit()
            BaseDatos.desconectar()
            
    
    def modificar_cita(self):
         self.capturar_datos()
         conexion = BaseDatos.conectar()
         if conexion:
            try:
                 cursor_cita = conexion.cursor()
                 cursor_cita.callproc('ModificarCita', [
                     self.get_codigo_cita(), 
                     self.get_fecha(), 
                     self.get_hora(), 
                     self.get_codigo_servicio(), 
                     self.get_id_usuario(),
                     self.get_codigo_mascota(), 
                     self.get_estado()
                     ])
                 print('Cita modificada con éxito')
                 conexion.commit()
            except Exception as e:
                 print(f'Error al modificar la cita: {e}')
                 conexion.rollback()
            finally:
                 if conexion:
                     cursor_cita.close()
                     BaseDatos.desconectar()
         
        
    def buscar_cita_fecha(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cita_encontrada = False
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorFecha', [self.get_fecha()])
                for fila in cursor_cita.stored_results():
                    fila = fila.fetchone()
                    if fila:
                        cita_encontrada = True
                        print('Citas encontradas por fecha-> ')
                        print('=============================================================================================================================================================================================================================================')
                        print(f'| Código: {fila[0]}, | Fecha: {fila[1]}, | Hora: {fila[2]}, | Servicio: {fila[3]}, | Usuario: {fila[4]}, | Mascota: {fila[5]}, | Estado: {fila[6]}')
                        print('=============================================================================================================================================================================================================================================')
                    else:
                        print('No se encontraron citas para la fecha ingresada.')
            except Exception as e:
                    print(f'Error al bucar la cita: {e}')
            finally:
                    if conexion:
                        cursor_cita.close()
                        BaseDatos.desconectar()
            
            
    def buscar_cita_codigo(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorCodigo ',[self.get_codigo_cita()])
                for fila in cursor_cita.stored_results():
                    fila = fila.fetchone()
                    print('Citas encontradas por codigo: ')
                    print('=============================================================================================================================================================================================================================================')
                    print(f'| Código: {fila[0]}, | Fecha: {fila[1]}, | Hora: {fila[2]}, | Servicio: {fila[3]}, | Usuario: {fila[4]}, | Mascota: {fila[5]}, | Estado: {fila[6]}')
                    print('=============================================================================================================================================================================================================================================')
            except Exception as e:
                print(f'Error al buscar la cita por codigo: {e}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()
            
    
    def obtener_citas(self,codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('ObtenerCitas', [codigo])
                print('Todas las citas:')
                for result in cursor_cita.stored_results():
                    fila = result.fetchone()
                    print('=============================================================================================================================================================================================================================================')
                    print(f'| Código: {fila[0]}, | Fecha: {fila[1]}, | Hora: {fila[2]}, | Servicio: {fila[3]}, | Usuario: {fila[4]}, | Mascota: {fila[5]}, | Estado: {fila[6]}')
                    print('=============================================================================================================================================================================================================================================')
            except Exception as e:
                print(f'Error al buscar todas las citas: {e}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()
            
            
    def eliminar_cita(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('EliminarServicio', [self.get_codigo_servicio()])
                conexion.commit()
                print('Cita eliminada con éxito.')
            except Exception as e:
                print(f'Error al eliminar cita: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar()
    
        
        
    
        

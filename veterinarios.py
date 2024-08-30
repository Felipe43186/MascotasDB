from conexion10 import BaseDatos

class Veterinario:

    def __init__(self,
                id_usuario: int = None,
                especialidad: str = None,
                horario: str = None,
                ):
            self.__id_usuario = id_usuario
            self.__especialidad = especialidad
            self.__horario = horario


    def get_id_usuario(self):
          return self.__id_usuario
    

    def set_id_usuario(self):
          while True:
              try:
                  id_usuario = int(input('Escriba el codigo del veterinario: '))
                  if id_usuario >= 3 and id_usuario <= 9999999:
                      self.__id_usuario = id_usuario
                      break
                  else:
                      print('El codigo debe estar entre 3 y 9999999')
              except ValueError:
                  print('Debe ingresar un numero entero')


    def get_especialidad(self):
          return self.__especialidad
    

    def set_especialidad(self):
          while True:
                especialidad = input('Escriba la especialidad del veterinario: ')
                if len(especialidad) <= 20:
                    self.__especialidad = especialidad
                    break
                else:
                    print('La especialidad debe tener como maximo 30 caracteres')


    def get_horario(self):
          return self.__horario
    

    def set_horario(self):
         while True:
              horario = input('Escriba el horario del veterinario: ')
              if len(horario) == 3:
                  self.__horario = horario
                  break
              else:
                  print('El horario debe tener 5 caracteres')


    def insertar_veterinario(self):
          self.set_id_usuario()
          self.set_especialidad()
          self.set_horario()
          conexion = BaseDatos.conectar()
          if conexion:
              cursor_veterinario = conexion.cursor()
              cursor_veterinario.callproc('InsertarVeterinario', [
                  self.__id_usuario,
                  self.__especialidad,
                  self.__horario,
              ])
              conexion.commit()
              print('Veterinario insertado correctamente')
              BaseDatos.desconectar()

          else:
              print('Error al conectar con la base de datos')


    def buscar_veterinario_id(self):
         conexion = BaseDatos.conectar()
         if conexion:
            id_usuario = int(input('Escriba el codigo del veterinario: '))
            cursor_veterinario = conexion.cursor()
            cursor_veterinario.callproc('BuscarVeterinarioPorId', [id_usuario])
            print('Veterinario encontrado:')
            for result in cursor_veterinario.stored_results():
                fila = result.fetchone()
            while fila is not None:
                print('=============================================================================================================================================================================================================================================')
                print(f' | ID: {fila[0]}, | Especialidad: {fila[1]}, | Horario: {fila[2]}')
                print('=============================================================================================================================================================================================================================================')
                fila = result.fetchone()
         

    def buscar_veterinario_nombre(self):
          conexion = BaseDatos.conectar()
          if conexion:
            try:
                nombre = input('Escriba el nombre del veterinario: ')
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('BuscarVeterinarioPorNombre', [nombre])
                print('Veterinarios encontrados:')
                for result in cursor_veterinario.stored_results():
                    fila = result.fetchone()
                while fila is not None:
                    print('=================================================================================================')
                    print(f' | ID: {fila[0]}, | Especialidad: {fila[1]}, | Horario: {fila[2]}')
                    print('=================================================================================================')
            except Exception as e:
                print(f'Error al buscar veterinario por nombre: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_veterinario.close()
                    BaseDatos


    def buscar_veterinario_especialidad(self):
          conexion = BaseDatos.conectar()
          if conexion:
            try:
                especialidad = input('Escriba la especialidad del veterinario: ')
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('BuscarVeterinarioPorEspecialidad', [especialidad])
                print('Veterinarios encontrados:')
                for result in cursor_veterinario.stored_results():
                    fila = result.fetchone()
                while fila is not None:
                    print('=================================================================================================')
                    print(f' | ID: {fila[0]}, | Especialidad: {fila[1]}, | Horario: {fila[2]}')
                    print('=================================================================================================')
            except Exception as e:
                print(f'Error al buscar veterinario por especialidad: {e}')
                conexion.rollback()
            finally:
                if conexion:    
                    cursor_veterinario.close()
                    BaseDatos.desconectar()


    def actualizar_veterinario(self):
        self.set_id_usuario()
        self.set_especialidad()
        self.set_horario()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ActualizarVeterinario', [
                    self.__id_usuario,
                    self.__especialidad,
                    self.__horario
                ])
                for result in cursor_veterinario.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('=================================================================================================')
                        print(f' | ID: {fila[0]}, | Especialidad: {fila[1]}, | Horario: {fila[2]}')
                        print('=================================================================================================')
                conexion.commit()
                print('Veterinario actualizado correctamente')
            except Exception as e:
                print(f'Error al actualizar veterinario: {e}')
                conexion.rollback()  
            finally:
                cursor_veterinario.close()
                BaseDatos.desconectar()



    def eliminar_veterinario(self):
          conexion = BaseDatos.conectar()
          if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('EliminarVeterinario', [self.__id_usuario])
                conexion.commit()
                print('Veterinario eliminado correctamente')
            except Exception as e:
                print(f'Error al eliminar el veterinario: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_veterinario.close()
                    BaseDatos.desconectar()
          
          



from conexion1 import BaseDatos
from usuarios import Usuario
class Veterinarios(Usuario):
    def __init__(
            self,
            especialidad: str = None,
            horario: str = None,
            **kwargs
            ):
        super().__init__**kwargs
        self.__especialidad = especialidad
        self.__horario = horario
        
    # GET y SET
    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self):
            while True:
                try:
                    especialidad_veterinario = str(input('Escriba la especialida del veterinario =>'))
                    if len(especialidad_veterinario)>3:
                        self.__especialidad = especialidad_veterinario
                        break
                    else:
                        print('Error')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
 
    def get_horario(self):
        return self.__horario

    def set_horario(self):
        while True:
            try:
                horario = input('Horario del veterinario =>')
                if len(horario) >=3:
                    self.__horario = horario
                    break
                else:
                    print('Horario incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
            super().capturar_datos
            self.set_especialidad()
            self.set_horario()
            
    def registrar_veterinario(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_veterinario = conexion.cursor()
            cursor_veterinario.callproc('InsertarVeterinario', [
                self.get_id_usuario(),
                self.get_nombre(),
                self.get_apellido(),
                self.get_ciudad(),
                self.get_direccion(),
                self.get_telefono(),
                self.get_es_propietario(),
                self.get_es_veterinario(),
                self.get_es_administrador(),
                self.get_email(),
                self.get_contraseña(),
                self.get_especialidad(),
                self.get_horario()
                
            ])
            conexion.commit()
        print('Veterinario registrado correctamente...')
        if conexion:
            BaseDatos.desconectar()

    def buscar_veterinarioid(self, codigo_veterinario=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                veterinario_encontrada = False
                cursor_veterinario = conexion.cursor()
                print(f'Buscando el veterinario {codigo_veterinario}...')
                cursor_veterinario.callproc('ConsultarVeterinarioId', [codigo_veterinario])
                for busqueda in cursor_veterinario.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        veterinario_encontrada = True
                        print(veterinario_encontrada)
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return veterinario_encontrada
                    else:
                        print('Veterinario no encontrado. Intente de nuevo.')
                        print(veterinario_encontrada)
                        return veterinario_encontrada
            except Exception as e:
                print(f'Error al buscar el veterinario: {e}')
            finally:
                if conexion:
                    cursor_veterinario.close()
                    BaseDatos.desconectar()

    def actualizar_veterinario(self, codigo_veterinario):
        conexion = BaseDatos.conectar()
        veterinario_encontrada = self.buscar_veterinarionombre(codigo_veterinario)
        if veterinario_encontrada:
            try:
                print('Escriba los nuevos datos del veterinario =>')
                self.set_nombre(),
                self.set_apellido(),
                self.set_ciudad(),
                self.set_direccion(),
                self.set_telefono(),
                self.set_email(),
                self.set_contraseña(),
                self.set_especialidad(),
                self.set_horario()
                
                nuevo_nombre = self.get_nombre(),
                nueva_apellido = self.get_apellido(),
                nueva_ciudad = self.get_ciudad(),
                nueva_direccion = self.get_direccion(),
                nuevo_telefono = self.get_telefono(),
                nuevo_email = self.get_email(),
                nuevo_contraseña = self.set_contraseña(),
                nuevo_especialidad = self.set_especialidad(),
                nuevo_horario =  self.set_horario()

                print(f'Código => {codigo_veterinario}')
                print(f'Nuevo nombre=> {nuevo_nombre}')
                print(f'Nuevo apellido=> {nueva_apellido}')
                print(f'Nueva ciudad=> {nueva_ciudad}')
                print(f'Nueva direccion=> {nueva_direccion}')
                print(f'Nuevo telefono=> {nuevo_telefono}')
                print(f'Nuevo email=> {nuevo_email}')
                print(f'Nueva contraseña=> {nuevo_contraseña}')
                print(f'Nueva especialidad=> {nuevo_especialidad}')
                print(f'Nuevo horario=> {nuevo_horario}')

                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ActualizarVeterinario', [
                    codigo_veterinario,
                    nuevo_nombre,
                    nueva_apellido,
                    nueva_ciudad,
                    nueva_direccion,
                    nuevo_telefono,
                    nuevo_email,
                    nuevo_contraseña,
                    nuevo_especialidad,
                    nuevo_horario
                ])
                conexion.commit()
                cursor_veterinario.close()
                print('Veterinario actualizada')
            except Exception as error:
                print(f'Error al actualizar el veterinario: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Veterinario no encontrada. Intente otra vez')

    def buscar_veterinarionombre(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                Veterinario_encontrada = False
                cursor_Veterinario = conexion.cursor()
                print(f'Buscando veterinario...')
                cursor_Veterinario.callproc('ConsultarVeterinarioNombre')
                for busqueda in cursor_Veterinario.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return Veterinario_encontrada
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(Veterinario_encontrada)
                        return Veterinario_encontrada
            except Exception as e:
                print(f'Error al buscar el veterinario: {e}')
            finally:
                if conexion:
                    cursor_Veterinario.close()
                    BaseDatos.desconectar()    

    def eliminar_veterinarioid(self, codigo_veterinario):
        conexion = BaseDatos.conectar()
        Veterinario_encontrada = self.buscar_veterinarioid(codigo_veterinario)
        if Veterinario_encontrada:
            try:
                cursor_Veterinario = conexion.cursor()
                cursor_Veterinario.callproc('EliminarVeterinario', [codigo_veterinario])
                conexion.commit()
                cursor_Veterinario.close()
                print('Veterinarioeliminada')
            except Exception as error:
                print(f'Error al eliminar Veterinario: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()

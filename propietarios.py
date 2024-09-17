from conexion1 import BaseDatos
from usuarios import Usuario
class Propietarios(Usuario):
    def __init__(
            self,
            barrio: str = None,
            **kwargs
            ):
        super().__init__**kwargs
        self.__barrio = barrio
        
    # GET y SET
    def get_barrio(self):
        return self.__barrio

    def set_barrio(self):
            while True:
                try:
                    barrio = str(input('Escriba el barrio del propietario =>'))
                    if len(barrio)>3:
                        self.__barrio = barrio
                        break
                    else:
                        print('Error')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
            super().capturar_datos
            self.set_barrio()
            
    def registrar_propietario(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_propietario = conexion.cursor()
            cursor_propietario.callproc('InsertarPropietario', [
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
                self.get_barrio(),   
            ])
            conexion.commit()
        print('Propietario registrado correctamente...')
        if conexion:
            BaseDatos.desconectar()

    def buscar_propietarioid(self, codigo_propietario=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                propietario_encontrada = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando elpropietario {codigo_propietario}...')
                cursor_propietario.callproc('ConsultarPropietarioId', [codigo_propietario])
                for busqueda in cursor_propietario.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        propietario_encontrada = True
                        print(propietario_encontrada)
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return propietario_encontrada
                    else:
                        print('Veterinario no encontrado. Intente de nuevo.')
                        print(propietario_encontrada)
                        return propietario_encontrada
            except Exception as e:
                print(f'Error al buscar elpropietario: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()

    def actualizar_propietario(self, codigo_propietario):
        conexion = BaseDatos.conectar()
        propietario_encontrada = self.buscar_veterinarionombre(codigo_propietario)
        if propietario_encontrada:
            try:
                print('Escriba los nuevos datos del propietario =>')
                self.set_nombre(),
                self.set_apellido(),
                self.set_ciudad(),
                self.set_direccion(),
                self.set_telefono(),
                self.set_email(),
                self.set_contraseña(),
                self.set_barrio(),
               
                
                nuevo_nombre = self.get_nombre(),
                nueva_apellido = self.get_apellido(),
                nueva_ciudad = self.get_ciudad(),
                nueva_direccion = self.get_direccion(),
                nuevo_telefono = self.get_telefono(),
                nuevo_email = self.get_email(),
                nuevo_contraseña = self.set_contraseña(),
                nuevo_barrio = self.set_barrio(),
               

                print(f'Código => {codigo_propietario}')
                print(f'Nuevo nombre=> {nuevo_nombre}')
                print(f'Nuevo apellido=> {nueva_apellido}')
                print(f'Nueva ciudad=> {nueva_ciudad}')
                print(f'Nueva direccion=> {nueva_direccion}')
                print(f'Nuevo telefono=> {nuevo_telefono}')
                print(f'Nuevo email=> {nuevo_email}')
                print(f'Nueva contraseña=> {nuevo_contraseña}')
                print(f'Nueva especialidad=> {nuevo_barrio}')
            

                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ActualizarVeterinario', [
                    codigo_propietario,
                    nuevo_nombre,
                    nueva_apellido,
                    nueva_ciudad,
                    nueva_direccion,
                    nuevo_telefono,
                    nuevo_email,
                    nuevo_contraseña,
                    nuevo_barrio
                   
                ])
                conexion.commit()
                cursor_veterinario.close()
                print('Propietario actualizada')
            except Exception as error:
                print(f'Error al actualizar el Propietario: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Propietario no encontrada. Intente otra vez')

    def buscar_propietarionombre(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                propietario_encontrada = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando propietario...')
                cursor_propietario.callproc('ConsultarPropietarioNombre')
                for busqueda in cursor_propietario.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return propietario_encontrada
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(propietario_encontrada)
                        return propietario_encontrada
            except Exception as e:
                print(f'Error al buscar el veterinario: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()    

    def eliminar_propietarioid(self, codigo_propietario):
        conexion = BaseDatos.conectar()
        propietario_encontrada = self.buscar_propietarioid(codigo_propietario)
        if propietario_encontrada:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('EliminarPropietario', [codigo_propietario])
                conexion.commit()
                cursor_propietario.close()
                print('propietario eliminada')
            except Exception as error:
                print(f'Error al eliminar propietario: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()

from conexion10 import BaseDatos
from usuarios import Usuario

class Administradores(Usuario):
    def __init__(
            self,
            cargo: str = None,
            fecha_ingreso: str = None,
            **kwargs
            ):
        super().__init__**kwargs
        self.__cargo = cargo
        self.__fecha_ingreso = fecha_ingreso
        
    # GET y SET
    def get_cargo(self):
        return self.__cargo

    def set_cargo(self):
            while True:
                try:
                    cargo = str(input('Escriba el cargo de administradores =>'))
                    if len(cargo)>3:
                        self.__cargo = cargo
                        break
                    else:
                        print('Error')
                except KeyboardInterrupt:
                    print('El usuario ha cancelado la entrada de datos.')
                continue
 
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self):
        while True:
            try:
                fecha_ingreso= input('Fecha ingreso del administrador =>')
                if len(fecha_ingreso) >=3:
                    self.__fecha_ingreso = fecha_ingreso
                    break
                else:
                    print('Horario incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
            super().capturar_datos
            self.set_cargo()
            self.set_fecha_ingreso()
            
    def registrar_administrador(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_adminitradores = conexion.cursor()
            cursor_adminitradores.callproc('InsertarAdministrador', [
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
                self.get_cargo(),
                self.get_fecha_ingreso()
                
            ])
            conexion.commit()
        print('Administrador registrado correctamente...')
        if conexion:
            BaseDatos.desconectar()

    def buscar_administradorid(self, codigo_adminitrador=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                adminitrador_encontrada = False
                cursor_adminitrador = conexion.cursor()
                print(f'Buscando el adminitrador {codigo_adminitrador}...')
                cursor_adminitrador.callproc('ConsultarAdministradorPorId', [codigo_adminitrador])
                for busqueda in cursor_adminitrador.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        adminitrador_encontrada = True
                        print(adminitrador_encontrada)
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return adminitrador_encontrada
                    else:
                        print('adminitrador no encontrado. Intente de nuevo.')
                        print(adminitrador_encontrada)
                        return adminitrador_encontrada
            except Exception as e:
                print(f'Error al buscar el adminitrador: {e}')
            finally:
                if conexion:
                    cursor_adminitrador.close()
                    BaseDatos.desconectar()

    def actualizar_adminitrador(self, codigo_adminitrador):
        conexion = BaseDatos.conectar()
        adminitrador_encontrada = self.buscar_adminitradornombre(codigo_adminitrador)
        if adminitrador_encontrada:
            try:
                print('Escriba los nuevos datos del adminitrador =>')
                self.set_nombre(),
                self.set_apellido(),
                self.set_ciudad(),
                self.set_direccion(),
                self.set_telefono(),
                self.set_email(),
                self.set_contraseña(),
                self.set_cargo(),
                self.set_fecha_ingreso()
                
                nuevo_nombre = self.get_nombre(),
                nueva_apellido = self.get_apellido(),
                nueva_ciudad = self.get_ciudad(),
                nueva_direccion = self.get_direccion(),
                nuevo_telefono = self.get_telefono(),
                nuevo_email = self.get_email(),
                nuevo_contraseña = self.set_contraseña(),
                nuevo_cargo = self.set_cargo(),
                nuevo_fecha_ingreso =  self.set_fecha_ingreso()

                print(f'Código => {codigo_adminitrador}')
                print(f'Nuevo nombre=> {nuevo_nombre}')
                print(f'Nuevo apellido=> {nueva_apellido}')
                print(f'Nueva ciudad=> {nueva_ciudad}')
                print(f'Nueva direccion=> {nueva_direccion}')
                print(f'Nuevo telefono=> {nuevo_telefono}')
                print(f'Nuevo email=> {nuevo_email}')
                print(f'Nueva contraseña=> {nuevo_contraseña}')
                print(f'Nuevo cargo=> {nuevo_cargo}')
                print(f'Nueva fecha de ingreso=> {nuevo_fecha_ingreso}')

                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ActualizarAdministrador', [
                    codigo_adminitrador,
                    nuevo_nombre,
                    nueva_apellido,
                    nueva_ciudad,
                    nueva_direccion,
                    nuevo_telefono,
                    nuevo_email,
                    nuevo_contraseña,
                    nuevo_cargo,
                    nuevo_fecha_ingreso
                ])
                conexion.commit()
                cursor_veterinario.close()
                print('Adminitrador actualizada')
            except Exception as error:
                print(f'Error al actualizar el adminitrador: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Adminitrador no encontrado. Intente otra vez')

    def buscar_adminitradornombre(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                adminitrador_encontrada = False
                cursor_adminitrador = conexion.cursor()
                print(f'Buscando adminitrador...')
                cursor_adminitrador.callproc('ConsultarAdministradorPorNombre')
                for busqueda in cursor_adminitrador.stored_results():
                    resultados = busqueda.fetchall()
                    if resultados:
                        for datos in resultados:
                            print(datos)
                        return adminitrador_encontrada
                    else:
                        print('No se encontraron registros. Intente de nuevo.')
                        print(adminitrador_encontrada)
                        return adminitrador_encontrada
            except Exception as e:
                print(f'Error al buscar el adminitrado: {e}')
            finally:
                if conexion:
                    cursor_adminitrador.close()
                    BaseDatos.desconectar()    

    def eliminar_administradoid(self, codigo_administrador):
        conexion = BaseDatos.conectar()
        administrador_encontrada = self.buscar_administradorid(codigo_administrador)
        if administrador_encontrada:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('EliminarUsuarioYAdministrador', [codigo_administrador])
                conexion.commit()
                cursor_administrador.close()
                print('Administrador oeliminada')
            except Exception as error:
                print(f'Error al eliminaradministrador: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
    
    def consultar_todos_admin(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_admin = conexion.cursor()
                cursor_admin.callproc('ConsultarAdministradores')
                print('Administradores encontrados:')
                for fila in cursor_admin.stored_results():
                    fila = fila.fetchone()
                    print('Citas encontradas por código: ')
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
                    print(f'| Código: {fila[0]}, | Cargo: {fila[1]}, | Fecha: {fila[2]}, | Servicio: {fila[3]}, | Usuario: {fila[4]}, | Mascota: {fila[5]}, | Estado: {fila[6]}')
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
            except Exception as e:
                print(f'Error al consultar todos administradores: {e}')
            finally:
                if conexion:
                    cursor_admin.close()
                    BaseDatos.desconectar()
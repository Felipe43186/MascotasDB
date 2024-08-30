import re
from conexion10 import BaseDatos

class PropietariosMascotas():
    
    def __init__(
        self,
        id_usuario_propietario : int = None,
        nombre_propietario: str = None, 
        apellido: str = None ,
        ciudad: str = None,
        direccion: str = None,
        telefono: str = None ,
        email: str = None,
        barrio: str = None
        ):
        
        self.__id_usuario_propietario = id_usuario_propietario
        self.__nombre_propietario = nombre_propietario
        self.__apellido = apellido
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__barrio = barrio
        
        
    def get_id_usuario_propietario(self):
        return self.__id_usuario_propietario
    
    def set_id_usuario_propietario(self):
        while True:
            try:
                id_usuario_propietario = int(input('Escriba el codigo del propietario: '))
                if id_usuario_propietario >= 3 and id_usuario_propietario <= 9999999:
                    self.__id_usuario_propietario = id_usuario_propietario
                    break
                else:
                    print('El ID debe ser un entero positivo') 
            except KeyboardInterrupt:
                print('\nOperación cancelada por el usuario.')
            continue
        
        
    def get_nombre_propietario(self):
        return self.__nombre_propietario
    
    
    def set_nombre_propietario(self):
        while True:
            try:
                nombre_propietario = input('Nombre de la mascota: ')
                if len(nombre_propietario)>3:
                    self.__nombre_mascota = nombre_propietario
                    break
            except ValueError:
                print('Ingersar los letras')
            else:
                print('Nombre incorrecto. Intente de nuevo')
    
    
    def get_apellido(self):
        return self.__apellido
    
    
    def set_apellido(self):
        while True:
            try:
                apellido = input('Ingrese el apellido del propietario: ')
                if len(apellido)>3:
                    self.__apellido = apellido
                    break
            except ValueError:
                print('Ingresar los caracteres')
            else:
                print('Apellido incorrecto. Intente de nuevo')
                continue
            
            
    def get_ciudad(self):
        return self.__ciudad
    
    
    def set_ciudad(self):
        while True:
            try:
                ciudad = input('Ingrese la ciudad del propietario: ')
                if len(ciudad)>3:
                    self.__ciudad = ciudad
                    break
            except ValueError:
                print('Ingresar los caracteres correctos')
            else:
                print('Ciudad incorrecta. Intente de nuevo')
        
        
    def get_direccion(self):
        return self.__direccion
    
    
    def set_direccion(self):
        while True:
                direccion = input('Ingrese la direccion del propietario: ')
                if len(direccion)>5:
                    self.__direccion = direccion
                    print(f'La dirección es: {self.__direccion}')
                    break
                else:
                    print('Dirección incorrecta. Debe tener más de 5 caracteres. Intente de nuevo')
                
                
    def get_telefono(self):
        return self.__telefono
    
    
    def set_telefono(self):
        while True:
            telefono = input('Ingrese el teléfono del propietario (10 dígitos): ').strip()
            if re.match(r'^\d{10}$', telefono):
                self.__telefono = telefono
                print(f'Teléfono del propietario: {self.__telefono}')
                break
            else:
                print('Número de teléfono inválido. Debe contener exactamente 10 dígitos y solo números. Intente de nuevo.')
                continue
                
    def get_email(self):
        return self.__email
    
    
    def set_email(self):
        while True:
            email = input('Ingrese el correo electrónico del propietario: ').strip()
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z0-9-.]+$', email):
                self.__email = email
                print(f'Email del propietario: {self.__email}')
                break
            else:
                print('Correo electrónico inválido. Debe contener un símbolo "@" y un punto')
                continue
            
            
    def get_barrio(self):
        return self.__barrio
    
    
    def set_barrio(self):
        while True:
            barrio = input('Ingrese el barrio del propietario: ')
            if len(barrio)>5:
                self.__barrio = barrio
                print(f'El barrio es: {self.__barrio}')
                break
            else:
                print('Barrio incorrecto. Debe tener más de 5 caracteres. Intente de nuevo')
                
                
    def insertar_propietario(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_propietario = conexion.cursor()
            cursor_propietario.callproc('InsertarPropietario', [
                self.__id_usuario_propietario,
                self.__nombre,
                self.__apellido,
                self.__ciudad,
                self.__direccion,
                self.__telefono,
                self.__email,
                self.__contraseña
            ])
            conexion.commit()
        print('Propietario registrado correctamente...')
        if conexion:
            BaseDatos.desconectar()
            
            
    def consultar_propietario_id(self,id_propietario):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                propietario_encontrado = False
                cursor_propietario = conexion.cursor()
                print(f'Buscando el propietario {id_propietario}')
                cursor_propietario.callprroc('ConsultarPropietarioPorId',[id_propietario])
                for fila in cursor_propietario.stored_results():
                    resultado = fila.fetchone()
                if resultado:
                    propietario_encontrado
                    print('Propietario encontrado: ')
                    print('Resultado:') 
                    print('=============================================================================================================================================================================================================================================')
                    print(f'Id_Propietario: {fila[0]}, | Nombre: {fila[1]}, | Apellido: {fila[2]}, |  Ciudad: {fila[3]},  | Dreccion: {fila[4]}, | Teléfono: {fila[5]}, | Es Propietario: {fila[6]}, | Email: {fila[7]}, | Contraseña: {fila[8]}, | Barrio: {fila[9]}')
                    print('=============================================================================================================================================================================================================================================')
                    return propietario_encontrado
                else:
                    print('Propietario no encontrado. Intente de nuevo.')
                    print(propietario_encontrado)
                    return propietario_encontrado
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_propietario.close()
                    BaseDatos.desconectar()
        
            
    def consultar_propietario_nombre(self, nombre_propietario = None):
        try:
            conexion = BaseDatos.conectar()
            if not conexion:
                print('No se pudo establecer la conexión a la base de datos.')
                return False
            propietario_encontrada = False
            cursor_propietario = conexion.cursor()
            print(f'Buscando el nombre del propietario{nombre_propietario}...')
            cursor_propietario.callproc('ConsultarPropietarioPorNombre', [nombre_propietario])
            for fila in cursor_propietario.stored_results():
                resultado = fila.fetchone()
                if resultado:
                    propietario_encontrada = True
                    print('Resultado:')
                    print('=============================================================================================================================================================================================================================================')
                    print(f'Id_Propietario: {fila[0]}, | Nombre: {fila[1]}, | Apellido: {fila[2]}, |  Ciudad: {fila[3]},  | Dreccion: {fila[4]}, | Teléfono: {fila[5]}, | Es Propietario: {fila[6]}, | Email: {fila[7]}, | Contraseña: {fila[8]}, | Barrio: {fila[9]}')
                    print('=============================================================================================================================================================================================================================================')
                else:
                    print('Propietario no encontrado.')
            return propietario_encontrada
        except Exception as e:
            print(f'Error al buscar al propietario por el nombre: {e}')
            return False
        finally:
            if conexion:
                cursor_propietario.close()
                BaseDatos.desconectar()
                
                
    def consultar_todos_propietarios(self):
        try:
            conexion = BaseDatos.conectar()
            if not conexion:
                print('No se pudo establecer la conexión a la base de datos.')
                return []
            cursor_propietario = conexion.cursor()
            cursor_propietario.callproc('ConsultarPropietarios')
            resultados = []
            for resultado in cursor_propietario.stored_results():
                resultados.extend(resultado.fetchall())
            if resultados:
                print('Mascotas encontradas:')
                for fila in resultados:
                    print('Resultado:')
                    print('=============================================================================================================================================================================================================================================')
                    print(f'Id_Propietario: {fila[0]}, | Nombre: {fila[1]}, | Apellido: {fila[2]}, |  Ciudad: {fila[3]},  | Dreccion: {fila[4]}, | Teléfono: {fila[5]}, | Es Propietario: {fila[6]}, | Email: {fila[7]}, | Contraseña: {fila[8]}, | Barrio: {fila[9]}')
                    print('=============================================================================================================================================================================================================================================')
            else:
                print('No se encontraron mascotas.')
            return resultados
        except Exception as e:
            print(f'Error al obtener los propietarios: {e}')
        finally:
             if conexion:
                cursor_propietario.close()
                BaseDatos.desconectar()
                
                
    def actualizar_propietario(self,id_usuario_propietario):
        conexion = BaseDatos.conectar()
        propietario_encontrado = self.buscar_propietario(id_usuario_propietario)
        if propietario_encontrado:
            try:
                print('Escriba los nuevos datos del propietario: ')
                self.set_ciudad()
                self.set_direccion()
                self.set_telefono()
                self.set_email()
                self.set_barrio()
                
                nueva_ciudad = self.get_set_ciudad()
                nueva_direccion = self.get_direccion()
                nuevo_telefono = self.get_telefono()
                nuevo_email = self.get_email()
                nuevo_barrio = self.get_barrio()
                
                print(f'Id_Propietario: {id_usuario_propietario}')
                print(f'Nueva ciudad: {nueva_ciudad}')
                print(f'Nueva direccion: {nueva_direccion}')
                print(f'Nuevo telefono: {nuevo_telefono}')
                print(f'Nuevo email: {nuevo_email}')
                print(f'Nuevo barrio: {nuevo_barrio}')

                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarPropietario',[
                id_usuario_propietario,
                nueva_ciudad,
                nueva_direccion,
                nuevo_telefono,
                nuevo_email,
                nuevo_barrio
                ])
                conexion.commit()
                cursor_mascota.close()
                print('Propietario actualizada')
            except Exception as error:
                print(f'Error al actualizar el propietario: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Propietario no encontrado. Intente otra vez')
            
            
            
            

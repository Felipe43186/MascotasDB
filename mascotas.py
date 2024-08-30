from conexion10 import BaseDatos

class Mascota:
    def __init__(
            self,
            codigo: int = None,
            nombre: str= None,
            especie: str= None,
            raza: str= None,
            edad: float= None,
            peso: float= None,
            usuario: int = None,
            historial_medico= None
            ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__usuario = usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []


    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self):
        while True:
            try:
                codigo = int(input('Escriba el codigo de la mascota: '))
                if codigo >= 3 and codigo <= 9999999:
                    self.__codigo = codigo
                    break
                else:
                    print('Codigo incorrecto. Intente de nuevo') 
            except ValueError:
                print('El código debe ser un número entero.')
            except KeyboardInterrupt:
                print('\nOperación cancelada por el usuario.')
            continue


    def get_nombre(self):
        return self.__nombre
    

    def set_nombre(self):
        while True:
            nombre = input('Nombre de la mascota: ')
            if len(nombre)>3:
                self.__nombre = nombre
                break
            else:
                print('Nombre incorrecto. Intente de nuevo')


    def get_especie(self):
        return self.__especie

    
    def set_especie(self):
        while True:
            especie = input('Especie de la mascota (gato, perro...): ')
            if 2 < len(especie) <= 20:
                self.__especie = especie
                break
            else:
                print('Datos incorrectos. Intente de nuevo')


    def get_raza(self):
        return self.__raza
    

    def set_raza(self):
        while True:
            raza = input('Raza de la mascota: ')
            if raza.isalpha() and 2 < len(raza) <= 20:
                self.__raza = raza
                break
            else:
                print('Datos de raza incorrectos. Intente de nuevo')
        self.__raza = raza

    
    def get_edad(self):
        return self.__edad
    

    def set_edad(self):
        while True:
            edad = float(input('Edad de la mascota (años): '))
            if 0 < edad <= 25:
                self.__edad = edad
                break
            else:
                print('Edad no válida')


    def get_peso(self):
        return self.__peso
    

    def set_peso(self):
        while True:
            peso = float(input('Peso en kg: '))
            if (0 < peso <= 25):
                self.__peso = peso
                break
            else:
                print('Peso no válido')


    def get_usuario(self):
        return self.__usuario
    

    def set_usuario(self):
        while True:
            try:
                usuario = int(input('Id usuario: '))
                if 0 < usuario <= 1000000000:
                    self.__usuario = usuario
                    break
                else:
                    print('Usuario no válido. Debe estar entre 1 y 1000000000.')
            except ValueError:
                print('Solo se admiten números.')
            continue
    
    
    def get_historial(self):
        return self.__historial
    

    def agregar_historial_medico(self, entrada: str):
        self.__historial_medico.append(entrada)


    def capturar_datos(self):
            self.set_codigo()
            self.set_nombre()
            self.set_especie()
            self.set_raza()
            self.set_edad()
            self.set_peso()
            self.set_usuario()


    def registrar_mascota(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_mascota = conexion.cursor()
            cursor_mascota.callproc('CrearMascota' , [
                self.__codigo,
                self.__nombre,
                self.__especie,
                self.__raza,
                self.__edad,
                self.__peso,
                self.__usuario
            ])
            conexion.commit()
        print('Mascota registrada correctamente...')
        if conexion:
            BaseDatos.desconectar()

    def buscar_mascota(self, codigo_mascota=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrada = False
                cursor_mascota = conexion.cursor()
                print(f'Buscando la mascota {codigo_mascota}...')
                cursor_mascota.callproc('BuscarMascotaPorId', [codigo_mascota])
                for fila in cursor_mascota.stored_results():
                    resultado = fila.fetchone()
                    if resultado:
                        mascota_encontrada = True
                        print(mascota_encontrada)
                        print('Resultado:') 
                        print('=============================================================================================================================================================================================================================================')
                        print(f'Id_Propietario: {fila[0]}, | Nombre: {fila[1]}, | Apellido: {fila[2]}, |  Ciudad: {fila[3]},  | Dreccion: {fila[4]}, | Teléfono: {fila[5]}, | Es Propietario: {fila[6]}, | Email: {fila[7]}, | Contraseña: {fila[8]}, | Barrio: {fila[9]}')
                        print('=============================================================================================================================================================================================================================================')
                        return mascota_encontrada
                    else:
                        print('Mascota no encontrada. Intente de nuevo.')
                        print(mascota_encontrada)
                        return mascota_encontrada
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()
                   
                    
    def buscar_mascota_nombre(self, nombre = None):
     if nombre is None:
        self.set_nombre
        nombre = self.nombre  
        try:
            conexion = BaseDatos.conectar()
            if not conexion:
                print('No se pudo establecer la conexión a la base de datos.')
                return False
            mascota_encontrada = False
            cursor_mascota = conexion.cursor()
            print(f'Buscando la mascota por el nombre {nombre}...')
            cursor_mascota.callproc('BuscarMascotaNombre', [nombre])
            for fila in cursor_mascota.stored_results():
                resultado = fila.fetchone()
                if resultado:
                    mascota_encontrada = True
                    print('Resultado:')
                    print('=============================================================================================================================================================================================================================================')
                    print(f'Id_Propietario: {fila[0]}, | Nombre: {fila[1]}, | Apellido: {fila[2]}, |  Ciudad: {fila[3]},  | Dreccion: {fila[4]}, | Teléfono: {fila[5]}, | Es Propietario: {fila[6]}, | Email: {fila[7]}, | Contraseña: {fila[8]}, | Barrio: {fila[9]}')
                    print('=============================================================================================================================================================================================================================================')
                else:
                    print('Mascota no encontrada.')
            return mascota_encontrada
        except Exception as e:
            print(f'Error al buscar la mascota por el nombre: {e}')
            return False
        finally:
            if conexion:
                cursor_mascota.close()
                BaseDatos.desconectar()
                
            
    def obtener_mascotas(self):
        try:
            conexion = BaseDatos.conectar()
            if not conexion:
                print('No se pudo establecer la conexión a la base de datos.')
                return []
            cursor_mascotas = conexion.cursor()
            cursor_mascotas.callproc('ObtenerTodasLasMascotas')
            resultados = []
            for resultado in cursor_mascotas.stored_results():
                resultados.extend(resultado.fetchall())
            if resultados:
                print('Mascotas encontradas:')
                for fila in resultados:
                    print(f'Codigo: {fila[0]}, Nombre: {fila[1]}, Especie: {fila[2]}, Edad: {fila[3]}')
            else:
                print('No se encontraron mascotas.')
            return resultados
        except Exception as e:
            print(f'Error al obtener las mascotas: {e}')
        finally:
             if conexion:
                cursor_mascotas.close()
                BaseDatos.desconectar()


    def actualizar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.buscar_mascota(codigo_mascota)
        if mascota_encontrada:
            try:
                print('Escriba los nuevos datos de la mascota: ')
                self.set_nombre()
                self.set_especie()
                self.set_raza()
                self.set_edad()
                self.set_peso()
                
                nuevo_nombre = self.get_nombre()
                nueva_especie = self.get_especie()
                nueva_raza = self.get_raza()
                nueva_edad = self.get_edad()
                nuevo_peso = self.get_peso()
                
                print(f'Código: {codigo_mascota}')
                print(f'Nuevo nombre: {nuevo_nombre}')
                print(f'Nueva especie: {nueva_especie}')
                print(f'Nueva raza: {nueva_raza}')
                print(f'Nueva edad: {nueva_edad}')
                print(f'Nuevo peso: {nuevo_peso}')

                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarMascota', [
                    codigo_mascota,
                    nuevo_nombre,
                    nueva_especie,
                    nueva_raza,
                    nueva_edad,
                    nuevo_peso
                ])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota actualizada')
            except Exception as error:
                print(f'Error al actualizar la mascota: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Mascota no encontrada. Intente otra vez')


    def eliminar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                mascota_encontrada = self.buscar_mascota(codigo_mascota)
                if mascota_encontrada:
                    respuesta = input(f'Está seguro de eliminar la mascota con el código: {codigo_mascota}? (SI/NO): ')
                    if respuesta == 'si':
                        cursor_mascota = conexion.cursor()
                        cursor_mascota.callproc('EliminarMascota', [codigo_mascota])
                        conexion.commit()
                        cursor_mascota.close()
                        print('Mascota eliminada')
                    else:
                        print('Operación cancelada.')
            except Exception as error:
                print(f'Error al eliminar la mascota: {error}. Intente de nuevo')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
from conexion10 import BaseDatos

class Productos:
    
    def __init__(self, 
                 codigo: int = None,
                 nombre: str = None,
                 descripcion: str = None,
                 precio: float = None,
                 stock: int = None,):
        
        
        self._codigo = codigo,
        self._nombre = nombre,
        self._descripcion = descripcion
        self._precio = precio,
        self._stock = stock
        
        
    def get_codigo(self):
        return self._codigo
    
    
    def set_codigo(self):
        while True:
            try:
                codigo = int(input('Ingrese el código del producto: '))
                if codigo >= 1 and codigo <= 9999999:
                    self._codigo = codigo
                    break
                else:
                    print('El código debe estar entre 1 y 9999999.')
            except ValueError:
                print('El código debe ser un número entero.')
                
                
    def get_nombre(self):
        return self._nombre
    
    
    def set_nombre(self):
        while True:
            nombre = input('Ingrese el nombre del producto: ')
            if len(nombre) >= 3 and len(nombre) <= 50:
                self._nombre = nombre
                break
            else:
                print('El nombre debe tener entre 3 y 50 caracteres.')
                
    
    def get_descripcion(self):
        return self._descripcion
    
    
    def set_descripcion(self):
         while True:
             descripcion = input('Ingrese la descripción del producto: ')
             if len(descripcion) >= 5 and len(descripcion) <= 255:
                 self._descripcion = descripcion
                 break
             else:
                 print('La descripción debe tener entre 10 y 255 caracteres.')
                
                
    def get_precio(self):
        return self._precio
    
    
    def set_precio(self):
        while True:
            try:
                precio = float(input('Ingrese el precio del producto: '))
                if precio > 0:
                    self._precio = precio
                    break
                else:
                    print('El precio debe ser mayor a 0.')
            except ValueError:
                print('El precio debe ser un número decimal.')
                
                
    def get_stock(self):
        return self._stock
    
    
    def set_stock(self):
        while True:
            try:
                stock = int(input('Ingrese el stock del producto: '))
                if stock >= 0:
                    self._stock = stock
                    break
                else:
                    print('El stock debe ser un número entero positivo.')
            except ValueError:
                print('El stock debe ser un número entero.')
                
                
   
    def capturar_datos(self):
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()
        self.set_stock()


    def registrar_producto(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('ResgistrarProducto', [
                    self._codigo,
                    self._nombre,
                    self._descripcion,
                    self._precio,
                    self._stock,
                ])
                conexion.commit()
                print('Producto registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar producto: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
                
    def consultar_producto_codigo(self,codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarProductoPorCodigo', [codigo])
                print('Busqueda del producto completada')
                producto_encontrado = False
                for result in cursor_producto.stored_results():
                    fila = result.fetchone()
                    if fila:
                        producto_encontrado = True
                    while fila is not None:
                            print('===========================================================================================================')
                            print(f'| Código: {fila[0]} | Nombre: {fila[1]} | Descripción: {fila[2]} | Precio: {fila[3]:.2f} | Stock: {fila[4]} |')
                            print('===========================================================================================================')
                            break
                if not producto_encontrado:
                    print('No se encontro producto con el código propuesto.')
            except Exception as e:
                    print(f'Error al buscar producto: {e}')
            finally:
                    BaseDatos.desconectar()
        return None
                
                
    def consultar_producto_nombre(self, nombre):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarProductoPorNombre', [nombre])
                producto_encontrado = False
                for result in cursor_producto.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('========================================================================================================================')
                        print(f'| Código: {fila[0]} | Nombre: {fila[1]} | Descripción: {fila[2]} | Precio: {fila[3]:.2f} | Stock: {fila[4]} |')
                        print('========================================================================================================================')
                        producto_encontrado = True
                        fila = result.fetchone()
                if not producto_encontrado:
                    print('No se encontró producto con el nombre propuesto.')
                    
            except Exception as e:
                print(f'Error al buscar producto: {e}')
            finally:
                BaseDatos.desconectar()
        return None



    def consultar_todos_productos(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('ConsultarTodosProductos')
                print('Consulta de productos completada')
                for result in cursor_producto.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('========================================================================================================================================')
                        print(f'| Código: {fila[0]} | Nombre: {fila[1]} | Descripción: {fila[2]} | Precio: {fila[3]:.2f} | Stock: {fila[4]} |')
                        print('========================================================================================================================================')
                        fila = result.fetchone()
            except Exception as e:
                print(f'Error al consultar productos: {e}')
            finally:
                BaseDatos.desconectar()

    
    def actualizar_producto(self,codigo):
        self._codigo = codigo 
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('ActualizarProductos', [
                    self._codigo,
                    self._nombre,
                    self._descripcion,
                    self._precio,
                    self._stock,
                ])
                conexion.commit()
                cursor_producto.close() 
                print('Producto actualizado correctamente...')
            except Exception as e:
                print(f'Error al actualizar el producto: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()  


    def eliminar_producto(self, codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('EliminarProducto', [codigo])
                conexion.commit()
                print('Producto eliminado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el producto: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_producto = conexion.close()
                    BaseDatos.desconectar()
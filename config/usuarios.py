class Usuario:
    def __init__(self,id_us:str, nombre:str, apellido:str, edad:int, email:str, contraseña:str, direccion:str, telefono:str):
        self.__id_us = id_us
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__email = email
        self.__contraseña = contraseña
        self.__direccion = direccion
        self.__telefono = telefono
        
        
    def get_id_us(self):
        return self.__id_us
    
    
    def set_id_us(self,id_us):
        self.__id_us = id_us
        
        
    def get_nombre(self):
        return self.__nombre
    
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    
    def get_apellido(self):
        return self.__apellido
    
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
        
        
    def get_edad(self):
        return self.__edad
    
    
    def set_edad(self,edad):
        self.__edad = edad
        
        
    def get_email(self):
        return self.__email
    
    
    def set_email(self,email):
        self.__email = email
        
       
    def get_contraseña(self):
        return self.__contraseña
    

    def set_contraseña(self,contraseña):
        self.__contraseña = contraseña
        
        
    def get_direccion(self):
        return self.__direccion
    
    
    def set_direccion(self,direccion):
        self.__direccion = direccion
        
        
    def get_telefono(self):
        return self.__telefono
    
    
    def set_telefono(self,telefono):
        self.__telefono = telefono
        
        
    def iniciarSesion(self):
        print('Iniciando sesion')
    
    
    def registrarse(self):
        print('Esta en proceso de registrarse')
    
    
    def actualizarPerfil(self):
        print('Se esta actualizando su perfil')
        
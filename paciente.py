
#  Clase abstracta Paciente (con símbolos en código Unicode)
from abc import ABC, abstractmethod

class Paciente(ABC):
    #Constante de tasa administrativa
    TASA_ADM_CLINICA = 0.05  # 5%

    def __init__(self, nombre: str, identificacion: str, costo_base_servicio: float, dias_hospitalizacion: int = 0):
        #nombre vacío
        if not nombre.strip():
            raise ValueError("\u274C  Error: El nombre del paciente no puede estar vacío.")  

        #costo base negativo
        if costo_base_servicio < 0:
            raise ValueError("\u274C  Error: El costo base del servicio no puede ser negativo.")  

        #tipo incorrecto para días
        if not isinstance(dias_hospitalizacion, int):
            raise TypeError("\u26A0\uFE0F  Advertencia: Los días de hospitalización deben ser un número entero.")
        
        #días negativos
        if dias_hospitalizacion < 0:
            raise ValueError("\u274C  Error: Los días de hospitalización no pueden ser negativos.")  

        #Atributos privados y protegidos
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__costo_base_servicio = costo_base_servicio
        self._dias_hospitalizacion = dias_hospitalizacion

    #Obtener el nombre del paciente
    def get_nombre(self):
        return self.__nombre

    #Obtener la identificación del paciente
    def get_identificacion(self):
        return self.__identificacion

    #Obtener el costo base del servicio
    def get_costo_base_servicio(self):
        return self.__costo_base_servicio

    #Obtener los días de hospitalización
    def get_dias_hospitalizacion(self):
        return self._dias_hospitalizacion

    #Establecer los días de hospitalización
    def set_dias_hospitalizacion(self, dias):
        if not isinstance(dias, int):
            raise TypeError("\u26A0\uFE0F  Advertencia: Los días de hospitalización deben ser un número entero.")
        if dias < 0:
            raise ValueError("\u274C  Error: Los días de hospitalización no pueden ser negativos.")  
        
        self._dias_hospitalizacion = dias
        print("\u2705  Días de hospitalización actualizados correctamente.")  

    #Método abstracto para calcular el costo total
    @abstractmethod
    def calcular_costo_total(self):
        #Este método será implementado en las subclases
        pass
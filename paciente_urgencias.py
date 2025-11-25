
#Importación de la clase base Paciente
from paciente import Paciente

#Definición de la clase PacienteUrgencias que hereda de Paciente
class PacienteUrgencias(Paciente):
    #Recargo fijo por atención de urgencias
    RECARGO_URGENCIAS = 50000

    #Constructor de la clase PacienteUrgencias y sus atributos
    def __init__(self, nombre, identificacion, costo_base_servicio, prioridad):
        #Llamamos al constructor de la clase base -herencia
        super().__init__(nombre, identificacion, costo_base_servicio)
        
        #verificar que la prioridad no esté vacía
        if not prioridad.strip():
            raise ValueError("\u274C  Error: La prioridad del paciente no puede estar vacía.") 
        
        #tipo de dato de prioridad (debe ser texto)
        if not isinstance(prioridad, str):
            raise TypeError("\u26A0\uFE0F  Advertencia: La prioridad debe ser una cadena de texto.")
        
        #prioridad válida (solo valores esperados)
        prioridad_valida = prioridad.lower()
        if prioridad_valida not in ["alta", "media", "baja"]:
            raise ValueError("\u274C  Error: La prioridad debe ser 'alta', 'media' o 'baja'.")

        #Atributo privado
        self.__prioridad = prioridad_valida

    #Método para calcular el costo total del paciente de urgencias
    def calcular_costo_total(self):
        #Cálculo del costo base + recargo + tasa administrativa
        try:
            costo = self.get_costo_base_servicio() + self.RECARGO_URGENCIAS
            tasa_admin = costo * self.TASA_ADM_CLINICA
            total = costo + tasa_admin
            print(f"\u2705  Paciente de urgencias procesado. Costo total calculado: ${total:,.2f}")
            return total
        except Exception as e:
            print(f"\u26A0\uFE0F  Error al calcular el costo total del paciente: {str(e)}") 
            raise

#Importación de la clase base Paciente
from paciente import Paciente

#Definición de la clase PacienteUCI que hereda de Paciente
class PacienteUCI(Paciente):
    #Costo fijo por día en la Unidad de Cuidados Intensivos
    COSTO_DIA_UCI = 800000

    #Constructor de la clase PacienteUCI y sus atributos
    def __init__(self, nombre, identificacion, costo_base_servicio, dias_hospitalizacion, soporte_vital):
        #Llamada al constructor de la clase base
        super().__init__(nombre, identificacion, costo_base_servicio, dias_hospitalizacion)

        #Validación 1: verificar tipo de dato de soporte vital
        if not isinstance(soporte_vital, bool):
            raise TypeError("Error: El valor de 'soporte_vital' debe ser booleano (True o False).")

        #Validación 2: número de días de hospitalización debe ser positivo
        if self.get_dias_hospitalizacion() <= 0:
            raise ValueError("Error: El paciente UCI debe tener al menos 1 día de hospitalización.")

        #Validación 3: costo base no debe ser irrealmente bajo
        if self.get_costo_base_servicio() < 100000:
            raise ValueError("Advertencia: El costo base del servicio es demasiado bajo para un paciente UCI.")

        #Atributo privado
        self.__soporte_vital = soporte_vital

    #Método para calcular el costo total del paciente en UCI
    def calcular_costo_total(self):
        #Cálculo del costo total = base + (días * costo día UCI)
        costo = self.get_costo_base_servicio() + (self.get_dias_hospitalizacion() * self.COSTO_DIA_UCI)

        #Si el paciente usa soporte vital, se agrega un 20% adicional
        if self.__soporte_vital:
            costo *= 1.20  # +20%
            print("Soporte vital activo: se aplica recargo del 20%.")

        #Calcular tasa administrativa (5%)
        tasa_admin = costo * self.TASA_ADM_CLINICA
        total = costo + tasa_admin
        return total

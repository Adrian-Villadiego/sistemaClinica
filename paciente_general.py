#Importación de la clase base Paciente
from paciente import Paciente

#Definición de la clase PacienteGeneral que hereda de Paciente
class PacienteGeneral(Paciente):

    #Constructor de la clase PacienteGeneral y sus atributos
    def __init__(self, nombre, identificacion, costo_base_servicio, tipo_consulta, descuento_eps):
        #Llamada al constructor de la clase base Paciente
        super().__init__(nombre, identificacion, costo_base_servicio)

        # Validación 1️: tipo de consulta no puede estar vacío
        if not tipo_consulta.strip():
            raise ValueError("\u274C  Error: El tipo de consulta no puede estar vacío.")

        # Validación 2️: el descuento EPS debe estar entre 0 y 1 (ejemplo: 0.10 = 10%)
        if not (0 <= descuento_eps <= 1):
            raise ValueError("\u26A0\uFE0F  Error: El descuento EPS debe ser un valor entre 0 y 1.")

        #Validación 3️: tipo de consulta válido
        tipo_validos = ["general", "especialista", "control"]
        if tipo_consulta.lower() not in tipo_validos:
            raise ValueError("\u26A0\uFE0F  Error: El tipo de consulta debe ser 'general', 'especialista' o 'control'.")

        #Atributos privados
        self.__tipo_consulta = tipo_consulta.lower()
        self.__descuento_eps = descuento_eps

    #Método para calcular el costo total del paciente general
    def calcular_costo_total(self):
        try:
            # Cálculo del costo aplicando descuento EPS
            costo = self.get_costo_base_servicio()
            descuento = costo * self.__descuento_eps
            total = costo - descuento
            tasa_admin = total * self.TASA_ADM_CLINICA
            costo_final = total + tasa_admin

            #Mensaje de éxito
            print(f"\u2705  Paciente general procesado correctamente. Costo final: ${costo_final:,.2f}")
            return costo_final

        except Exception as e:
            print(f"\u274C  Error al calcular el costo total del paciente general: {str(e)}")
            raise
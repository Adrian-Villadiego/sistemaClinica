#Clase que administra el sistema de pacientes de una clínica
class SistemaClinica:
    #Constructor: inicializa la lista vacía de pacientes
    def __init__(self):
        self.lista_pacientes = []

    #Método para agregar un paciente al sistema
    def agregar_paciente(self, paciente):
        #verificar que el objeto sea de tipo Paciente
        from paciente import Paciente  # Evita importaciones circulares si se usa otro archivo
        if not isinstance(paciente, Paciente):
            raise TypeError("\u26A0\uFE0F  Error: Solo se pueden agregar objetos de tipo 'Paciente' al sistema.")

        #Si pasa la validación, se agrega a la lista
        self.lista_pacientes.append(paciente)
        print("\u2705  Paciente agregado correctamente al sistema.")

    #Método para generar el reporte de costos de todos los pacientes
    def generar_reporte_costos(self):
        #Validación 2: verificar si hay pacientes registrados
        if not self.lista_pacientes:
            raise ValueError("\u274C  Error: No hay pacientes registrados en el sistema. No se puede generar el reporte.")  # ❌

        total_facturacion = 0
        total_tasa_admin = 0

        print("\n\u1F4CA  Generando reporte de costos...\n")

        #Iterar sobre la lista de pacientes y calcular costos
        for p in self.lista_pacientes:
            try:
                costo = p.calcular_costo_total()
                admin = costo * p.TASA_ADM_CLINICA / (1 + p.TASA_ADM_CLINICA)
                total_facturacion += costo
                total_tasa_admin += admin
                print(f"Paciente: {p.get_nombre()} |  Costo Final: ${costo:,.2f}")
            except Exception as e:
                print(f"\u26A0\uFE0F  Advertencia: No se pudo calcular el costo de un paciente. Detalle: {str(e)}")

        #Mostrar resultados finales
        print("\n\u2705  Reporte generado exitosamente.")
        print(f"Total facturación: ${total_facturacion:,.2f}")
        print(f"Ingresos por Tasa Administrativa: ${total_tasa_admin:,.2f}")

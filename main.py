#importar las clases necesarias
from paciente_general import PacienteGeneral
from paciente_urgencias import PacienteUrgencias
from paciente_uci import PacienteUCI
from sistema_clinica import SistemaClinica

#funcion principal
def main():
    # Crear instancia del sistema de clínica
    sistema = SistemaClinica()
    print("\U0001F4C4  ----- DATOS DE LOS PACIENTES -----\n")

    #Pacientes de ejemplo
    paciente1 = PacienteGeneral("Adrian Villadiego", "1001", 1000, "general", 0.15)
    paciente2 = PacienteUrgencias("Luisa Brrio", "1002", 20000, "Alta")
    paciente3 = PacienteUCI("Andres Berrio", "1003", 2000000, 4, True)

    # Agregar pacientes al sistema
    sistema.agregar_paciente(paciente1)
    sistema.agregar_paciente(paciente2)
    sistema.agregar_paciente(paciente3)

    # Imprimir reporte en columnas
    print("\n\U0001F4CB  ----- REPORTE DE COSTOS -----\n")
    print(f"{' Paciente':<30} {'ID':<10} {'Costo Final':>20}")
    print("-" * 65)

    # Mostrar cada paciente (cada llamada calcular_costo_total() puede imprimir su propio mensaje)
    for p in sistema.lista_pacientes:
        costo = p.calcular_costo_total()
        print(f"{p.get_nombre():<30} {p.get_identificacion():<10} ${costo:>18,.2f}")

    # Calcular y mostrar total facturación
    total_facturacion = sum(p.calcular_costo_total() for p in sistema.lista_pacientes)
    print("-" * 65)
    print(f"{'TOTAL FACTURACIÓN':<40} ${total_facturacion:>18,.2f}")

    print("\n\u2705  Reporte generado exitosamente.")

if __name__ == "__main__":
    main()
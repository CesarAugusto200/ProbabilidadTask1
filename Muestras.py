import random
#El tipo de muestra respondiendo al incio A) es Estratificacion ya que este lo divide en grupos 
# y estan diferenciado por decirlo haci por un rol(caracteristica)

poblacion = {
    'RH': 150,
    'Administración': 450,
    'Docentes': 200,
    'Deportes': 100
}


tamano_muestra = 180


total_trabajadores = sum(poblacion.values())
proporciones = {depto: poblacion[depto] / total_trabajadores for depto in poblacion}


tamanos_muestra_por_depto = {depto: round(proporciones[depto] * tamano_muestra) for depto in poblacion}


muestra_final = {}

for depto, tamano_muestra_depto in tamanos_muestra_por_depto.items():
    empleados_depto = [f'{depto}_{i}' for i in range(1, poblacion[depto] + 1)]
    muestra_depto = random.sample(empleados_depto, tamano_muestra_depto)
    muestra_final[depto] = muestra_depto


print("Muestra Final:")
for depto, empleados in muestra_final.items():
    print(f"Departamento: {depto}")
    print(f"Empleados Seleccionados: {', '.join(empleados)}")
    print()

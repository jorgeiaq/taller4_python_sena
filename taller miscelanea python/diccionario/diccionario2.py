print("calcular promedio")

def notas_calculo(notas_finales):
    total_notas = 0
    students = len(notas_finales)

    for notas in notas_finales.values():
        total_notas += sum(notas)

    average = total_notas / students
    return average

alumnos = {
  "ivan" : [80, 78, 67],
  "andrea" : [90, 78, 89],
  "brayan" : [78, 68, 100]
}

promedio = notas_calculo(alumnos)
print("el promedio final de los tres alumnos es:", promedio)
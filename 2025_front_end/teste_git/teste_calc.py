import numpy
import calc.calculadora as cal

entrada = input ("digite no formato 'valor operador valor': ")
partes = entrada.split( )
if partes[0] == "pi":
    partes[0] = numpy.pi
elif partes[2] =="pi":
    partes[2] = numpy.pi

a = float(partes[0])
operador = partes[1]
b = float(partes[2])

print(cal(a,b,operador))

#teste
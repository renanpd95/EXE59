import os

name = str(input("Nome: "))
sexo = str(input("Sexo (M/F): "))
idad = int(input("Idade: "))
altu = float(input("Altura: "))
saud = str(input("Saude (boa/ruim): "))

os.system('clear')

if(sexo == "M" and idad == 18 and altu >= 1.70 and saud == "boa"):
  print(name)
  print("Está pessoa está apta a servir seu pais!")
else:
  print("Está pessoa não está apta")
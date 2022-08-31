print("Vamos calcular o IMC")
peso = float(input("Informe o seu peso em kg:"))
altura = float(input("Informe a sua altura em m:"))
resultado = peso / (altura*altura)
print("O seu IMC é {:.2f}".format(resultado))
if resultado < 18.5:
   print("Você está abaixo do peso")  
elif resultado >= 18.5 and resultado < 24.9:
   print("Você está normal")
elif resultado > 24.9 and resultado <= 30:
   print("Sobrepeso")
elif resultado > 30:
   print("Obesidade")                         
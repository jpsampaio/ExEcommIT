import random

num = input("Estou pensando em um número de 0 a 5. Você consegue adivinhar qual é?")
num2 = random.randrange(0,5)
if num == num2:
  print("Parabéns! Você acertou!")
else:
  print("Não foi dessa vez!")
print("O numéro que escolhemos foi {}".format(num2))



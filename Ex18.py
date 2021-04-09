from math import radians, tan, cos, sin

ang = float(input('Digite o ângulo:'))

seno = sin(radians(ang))
tang = tan(radians(ang))
cosse = cos(radians(ang))

print(f'O ângulo de {ang}º tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang}º tem o COSSENO de {cosse:.2f}')
print(f'O ângulo de {ang}º tem o TANGENTE de {tang:.2f}')
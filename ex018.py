import math
num = float(input('Digite o ângulo que deseja:'))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo de {}º tem o seno de {:.2f}.'.format(num, seno))
print('O ângulo de {}º tem o cosseno de {:.2f}.'.format(num, cos))
print('O ângulo de {}º tem o tangente de {:.2f}.'.format(num, tan))

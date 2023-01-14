print('-=' * 15)
#Python Exercise 73: Create a tuple filled with the top 20 finishers in the Brazilian Football Championship Table, in the order of placement. Then show:
#a) The first 5 teams.
#b) The last 4 placed.
#c) Times in alphabetical order.
#d) In what position is the Chapecoense team.
times = ('SE Palmeiras', 'SC Internacional', 'Fluminense', 'Corinthians', 'CR Flamengo', 'Atlético Paraense', 'Atlético Mineiro', 'Fortaleza EC', 'São Paulo FC', 'América FC', 'Botafogo FR', 'Santos FC', 'Goiás EC', 'RB Bragantino', 'Coritiba FC', 'Cuiaba EC', 'Ceará SC', 'AC Goianiense', 'Avaí FC', 'EC Juventude')
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os cinco últimos são {times[16:21]}')
print('-=' * 15)
print(f'Em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O time do Fluminense está na {times.index("Fluminense")+1} colocação') 
print('-=' * 15)

from random import choice
nome = str(input('Escreva seu nome completo: ')).strip()
#minus = nome.lower()
#maius = nome.upper()
explname = nome.split()
semesp = ''.join(explname)
pnome = explname[0]
print("""A frase original é "{}", ela
com todas as letras maiúsculas ficou "{}",
ela com todas as letras minusculas ficou "{}",
ela sem espaços tem "{}" caracteres e  seu
primeiro nome é {}""".format(nome, nome.upper(), nome.lower(), len(nome)-nome.count(' '), pnome))

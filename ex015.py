kmrod = float(input('Quantos km você fez?: '))
dias = int(input('Alugou por quantos dias: '))
pgkm = kmrod*0.15
pgdia = dias*60
print('Total a Pagar: R${:.2f}'.format((pgkm)+(pgdia)))
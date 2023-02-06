convidados = ['elon musk', 'paulo muzy', 'pewdiepie']
mensagem1 = 'Olá ' + convidados[0].title() + ' convidar para um jantar'
mensagem2 = 'Olá ' + convidados[1].title() + ' convidar para um jantar'
mensagem3 = 'Olá ' + convidados[2].title() + ' convidar para um jantar'


msg_removido = convidados[0] + ' não podera mais participar do jantar'
print(msg_removido)
print('')
convidados.remove('elon musk')

print(mensagem2)
print('')
print(mensagem3)
print('')
print('acabei encontrando uma mesa maior')
print('')

convidados.insert(3, 'barack obama')
convidados.insert(4, 'walter white')
convidados.insert(5, 'gus freman',)

print(convidados)
print('')

print('deu que a mesa nao chegara a tempo logo terei que diminuir a lista')
convidados.pop()
convidados.pop()
convidados.pop()

convidados.remove('paulo muzy')
convidados.remove('pewdiepie')

print(convidados)

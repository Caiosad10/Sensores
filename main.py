#Criando função que identifica se tem agua no bebedouro

def bebedouro(agua):
  if agua is True:
    return 'Tem agua'
  else:
    return 'Não tem agua'

print(bebedouro()) #retorna "Não toma agua"
print('')

#Criando a mesma coisa so que com a função lambda

bebedouro2 = lambda agua: 'Toma agua' if agua is True else 'Não toma agua'

print(bebedouro2()) #retoorna "Toma agua"
print('')

#Criando uma função dentro de outra. Criando um verificador de agua e criando um recipiente que recebe a agua

def verificadorAgua(agua):
  def recipienteAgua():
    if agua is True:
      return 'Tem agua no recipiente'
    else:
      return 'Não tem agua no recipiente'
  return recipienteAgua()

print(verificadorAgua()) #retorna "Tem agua no recipiente"
print('')

#Versão lambda da função acima

def verificador_Agua(agua):
  recipiente = lambda recipiente: 'Tem agua no recipiente' if agua is True else 'Não tem agua no recipiente'
  return recipiente(recipiente)

print(verificador_Agua())#retorna "Não tem agua no recipiente"

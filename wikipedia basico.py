import wikipedia

""" busca = wikipedia.search('Brasil')

for lista in busca:
    print(wikipedia.summary(lista)) """

busca = 'brasil'
wikipedia.set_lang('pt')
pesquisa = wikipedia.summary(busca, 3)

print(pesquisa)
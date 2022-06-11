import wikipedia #Biblioteca

""" busca = wikipedia.search('Brasil')

for lista in busca:
    print(wikipedia.summary(lista)) """

busca = 'brasil'    #Conteudo da pesquisa
wikipedia.set_lang('pt') # linguagem
pesquisa = wikipedia.summary(busca, 3) # conteudo e Quantidade de linhas

print(pesquisa)# mostra a pesquisa
    #__init__ -> inicializador da class mãe

class Programa:
    def __init__(self, nome, ano):
         self._nome = nome.title()
         self.ano = ano
         self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    #__str__ -> metodo especial que consegue representar uma classe textualmente
    def __str__(self):
       return f'{self.nome} - {self.ano} - {self.likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        #super ->  vai chamar a classe mãe
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes'

class Serie(Programa):
    def __init__(self,nome ,ano, temporadas):
        super(). __init__(nome,ano)
        self.temporadas = temporadas 
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'
        #função que representa textualmente nosso código


        # A class List vai gerir diversas funcionalidades para a class Playlist
class Playlist:
    def __init__(self,nome, programas):
        self.nome = nome
        self._programas = programas

    #__getitem__ -> é um método especial que define se alguem é iterável,ganhamos o in e o for in
    # nesse trecho estamos passsado o 'item' para a lista interna programas
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    #para podermos implementar o metodo unsized
    def __len__(self):
        return len(self._programas)
    
vingadores = Filme('vingadores - Gguerra inifinita', 2018, 160 )
atlanta = Serie('Atlanta', 2018, 4,)
todo_mundo_em_panico = Filme ('Todo mundo em pânico', 1999, 100)
demolidor = Serie ('Demolidor', 2016, 2)

vingadores.dar_likes()
todo_mundo_em_panico.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()

print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta, demolidor, todo_mundo_em_panico]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

#playlist_fim_de_semana é um unsizeble, que é um objeto que pode dizer seu próprio tamanho
#print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana: 
   print(programa)

len(playlist_fim_de_semana)

#Com essa função podemos ver se um objeto está dentro de um objeto do tipo playlist
print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}:')

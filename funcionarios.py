class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando Cursos - {mes}' if mes else 'Mostrando cursos desse mês' )

class Alura(Funcionario):
    #def mostrar_tarefas(self):
    #    print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'
    #É uma MIXIN
    #Quando não queremos instanciar
    #Uma classe desprendida da class Mãe
    #Depende de um nome para seu funcionamento

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


luan = Senior('Luan')
print(luan)

#Classes MIXIN, bastante usado qunado precisamos fazer o compartilhamento de algum comportamento que não é o mais importante da classe 

#MRO - Tem repetição/ Esquerda para direita
#pleno > Alura > Caelum > Funcionario 
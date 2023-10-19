from abc import ABC # abstract base classes
from collections.abc import MutableSequence
from numbers import Complex# Complex não é uma clase abstrata, portanto podemos criar instancias dele e usar seus métodos, incluido o __getitem__

class Numero(Complex):
    def __getitem__(self,item):
        super().__getitem__()

filmes = Numero()
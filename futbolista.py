from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    _listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, anosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", anosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    #getters
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    
    #setters
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados=golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil=piernaHabil
        
    def __str__(self):
        cadena = "Mi nombre es "+ self._nombre + " soy profesional en el deporte " + self._deporte + " Tengo " + str(self._edad) + " años de edad y llevo " + str(self._anosPracticando) + " años en el deporte"
        return cadena
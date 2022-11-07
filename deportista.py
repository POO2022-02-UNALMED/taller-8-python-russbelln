class Deportista:
    def __init__(self, deporte, anosPracticando):
        self._deporte=deporte
        self._anosPracticando=anosPracticando
    #getters
    def getDeporte(self):
        return self._deporte
    def getAñosPracticando(self):
        return self._anosPracticando
    
    #setters
    def setDeporte(self, deporte):
        self._deporte=deporte
    def setAñosPracticando(self, anosPracticando):
        self._anosPracticando=anosPracticando
    
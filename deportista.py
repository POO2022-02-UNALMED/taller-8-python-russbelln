class Deportista:
    def __init__(self, deporte, anosPracticando):
        self._deporte=deporte
        self._anosPracticando=anosPracticando
    #getters
    def getDeporte(self):
        return self._deporte
    def getA├▒osPracticando(self):
        return self._anosPracticando
    
    #setters
    def setDeporte(self, deporte):
        self._deporte=deporte
    def setA├▒osPracticando(self, anosPracticando):
        self._anosPracticando=anosPracticando
    
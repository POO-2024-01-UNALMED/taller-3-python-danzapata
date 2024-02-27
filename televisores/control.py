class Control:
    
    def __init__(self):
        self._tv = None

    ## apagar y encender
    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()
    
    ## canal Up canal Down
    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    ## volumen Up volumen Down
    def volumenUp(self):
        self._tv.volumenUp()
    
    def volumenDown(self):
        self._tv.volumenDown()

    ## set volumen y set canal
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)
    
    def setCanal(self, canal):
        self._tv.setCanal(canal)

    ## set y get tv
    def setTv(self, tv):
        self._tv = tv

    def getTv(self):
        return self._tv
    
    ## enlazar
    def enlazar(self, tv):
        self.setTv(tv)
        self._tv.setControl(self)
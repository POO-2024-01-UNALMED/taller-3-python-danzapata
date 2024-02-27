class TV:
    
    _numTV = int
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado

        self._control = self._control

        self._volumen = 1
        self._canal = 1
        self._precio = 500

        TV._numTV = TV._numTV+1
    
    
    ## set y get marca
    def setMarca(self, marca):
        self._marca=marca
         
    def getMarca(self):
        return self._marca
    
    ## set y get canal 
    def setCanal(self, canal):
        if (self._estado == True):
            if(canal>=1 and canal<=120):
                self._canal = canal

    def getCanal(self):
        return self._canal    
    
    ## set y get precio
    def setPrecio(self, precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    ## set y get volumen
    def setVolumen(self, volumen):
        if (self._estado == True):
            if(volumen>=0 and volumen<=7):
                self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    ##set y get control
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
    
    ## set y get numTV
    def setNumTV(numTV):
        TV._numTV = numTV

    def getNumTV():
        return TV._numTV

    ## trunOn y turnOff + getEstado
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    ## canal Up y canal Down
    def canalUp(self):
        if (self._estado == True):
            if (self._canal>=1 and self._canal<120):
                self._canal = self._canal+1
    
    def canalDown(self):
        if (self._estado == True):
            if (self._canal>1 and self._canal<=120):
                self._canal = self._canal-1
    
    ## volumen Up and voluemn Down 
    def volumenUp(self):
        if (self._estado == True):
            if(self._volumen>=0 and self._volumen<7):
                self._volumen = self._volumen+1

    def volumenDown(self):
        if (self._estado == True):
            if(self._volumen>0 and self._volumen<=7):
                self._volumen = self._volumen-1
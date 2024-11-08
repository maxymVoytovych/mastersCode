class CourantFunctions:
    
    def __init__(self,I=0,NOFE=10,L=0.01):
        self.i = I
        self.NumberOfFiniteElements = NOFE
        self.Length = L
    
    def fi(self,x):
        h = self.Length / self.NumberOfFiniteElements
        if x<0 or x>self.Length:
            return 0
        else:
            if (self.i - 1) * h < x and x <= self.i * h:
                return (x - (self.i - 1) * h) / h
                
            if self.i * h < x and x <= (self.i + 1) * h:
                return ((self.i + 1) * h - x) / h
            
            else:
                return 0
        
    
    def fiDerivative(self,x):
        h = self.Length / self.NumberOfFiniteElements
        if x<0 or x>self.Length:
            return 0
        else:
            if (self.i - 1) * h < x and x <= self.i * h:
                return self.NumberOfFiniteElements / self.Length
                
            if self.i * h < x and x <= (self.i + 1) * h:
                return -self.NumberOfFiniteElements / self.Length
            
            else:
                return 0
        
class Operation():
    def __init__(self,nombre1):
        self.nombre1 = nombre1
    def __add__(self,nombre2):
        return Operation(self.nombre1+nombre2)   
o = Operation(14)
o1 = o
o+=5
print(o.nombre1)


        


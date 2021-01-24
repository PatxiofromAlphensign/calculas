import sympy

def toCountVar(count):
        var = ["x%d" % i for i in range(count)] 
        if count > 3:
            return sympy.symbols(var)
        x,y,z = sympy.symbols(var)
        return x,y,z

class res2multivar:
    def __init__(self, count, order=2):
        self.vars  = toCountVar(count)
        self.order = order

    def diff(self,order):
        self.k=0
        for var in self.vars:
            self.k = self.k + sympy.Derivative(var, (var, self.order))
        return self.k

    def integrate(self, bounts, diff=True):
        if not diff:
            self.k()
        else:
            self.k = 0 
            for var in self.vars:
                self.k = self.k + var
        integ = 0
        for var in self.vars:
            integ = integ +self.k.integrate(var) 
        
        return integ

if __name__ == "__main__":
    print(res2multivar(4).integrate(2))

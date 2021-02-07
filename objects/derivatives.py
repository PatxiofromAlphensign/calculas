import sympy

def toCountVar(count, typ=None,name="x"):
        var = ["%s%d" % (name, i) for i in range(count)] 
        if count > 3:
            return sympy.symbols(var, cls=typ)
        x,y,z = sympy.symbols(var)
        return x,y,z

def toCountFunc(count, name="f"):
        var = " ".join(["%s%d" % (name, i) for i in range(count)])
        return sympy.symbols(var, cls=sympy.Function)

class res2multivar:
    def __init__(self, count, order=2):
        self.vars  = toCountVar(count)
        self.order = order

    def __iter__(self):
        return iter(self.vars)

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

class generaleq:
    def __init__(self, nvars):
        self.varss = res2multivar(nvars)
        self.dvars = [x + res2multivar(4).diff(1) for x in res2multivar(4)]
        self.F,self.f  = sympy.symbols("F f", cls=sympy.Function)

    def diff(self):
        res = 0
        for x,dx in zip(self.varss, self.dvars):
            res = res + self.F.diff(self.F.diff(self.f(x))) * self.f(x).diff(x) * dx
        return res

class equations4(generaleq):

    x1,y1, x2,y2 = res2multivar(4)
    xp1, yp1, xp2,yp2 = [x + res2multivar(4).diff(1) for x in res2multivar(4)]
    F,f  = sympy.symbols("F f", cls=sympy.Function)
    eq1 = (F.diff(x2) * F(y1)) + F(x1)*F(y1).diff(y1)

    def __init__(self):
        pass
    @property
    def chains(self):
        dFdf = self.F.diff(self.f(self.x1))*self.f.diff(self.y1)
        dFdy = self.F.diff(self.f(self.y1))*self.f.diff(self.y1)
        return dFdf + dFdy 

    @property
    def grads(self):
        grad_x1y1 = self.chains

if __name__ == "__main__":
    q =equations4()
    qg = generaleq(12)
    print(qg.diff())
    #print(res2multivar(4).integrate(2))


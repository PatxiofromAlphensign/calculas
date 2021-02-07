import sympy
import derivatives
from derivatives import res2multivar, generaleq 

class gradiant(derivatives.equations4):
    def __init__(self):
        super().__init__()
    def chain_varname(self, f):
        s1=  {self.x1,self.y1,self.x2,self.y2}
        res = 0
        for i in range(len(s1) - 2):
            res += f.diff(f(list(s1)[i])) + f.diff(f(list(s1)[i+1]))
        return res 
    def grad(self,count):
        F = derivatives.toCountFunc(count, name="f")
        grads = [self.chain_varname(f) for f in F]
        self.g = grads 
        return sum(grads)

    def directional_grad(self, direction):
        self.grad(6)
        k = 0
        for i in range(0,len(self.g),2):
            k += self.g[i]/(self.g[i]*self.g[i+1]) + self.g[i].diff(sympy.symbols(direction))
        self.k = k
        return k

def grandGrad():
    count = 4
    g = gradiant()
    main_grad = g.grad(count)
    return main_grad*(g.directional_grad("x") + g.directional_grad("y"))
    
def MultiDimGrad(dim):
    g = gradiant()
    getnames = lambda cout : [str(i) for i in range(cout)]
    for x in getnames(dim):
        g.directional_grad(x)

if __name__ == "__main__":
    MultiDimGrad(5)

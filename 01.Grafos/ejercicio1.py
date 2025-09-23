import csv
import json

class G:
    def _init_(self):
        self.mat = []
        self.v = []
    
    def csv(self, arch):
        with open(arch, 'r') as f:
            r = csv.reader(f)
            self.mat = []
            for fila in r:
                if fila:
                    self.mat.append([int(x) for x in fila])
        self.v = list(range(len(self.mat)))
    
    def js(self, arch):
        with open(arch, 'r') as f:
            d = json.load(f)
        self.v = d["P"]
        n = len(self.v)
        self.mat = [[0]*n for _ in range(n)]
        for o, ds in d["E"].items():
            i = self.v.index(o)
            for dest in ds:
                j = self.v.index(dest)
                self.mat[i][j] = 1
    
    def min(self):
        r = []
        for j in range(len(self.mat)):
            if not any(self.mat[i][j]==1 for i in range(len(self.mat))):
                r.append(self.v[j])
        return r
    
    def max(self):
        r = []
        for i in range(len(self.mat)):
            if not any(self.mat[i][j]==1 for j in range(len(self.mat))):
                r.append(self.v[i])
        return r
    
    def vd(self, nodo):
        if nodo not in self.v:
            return []
        i = self.v.index(nodo)
        return [self.v[j] for j in range(len(self.mat)) if self.mat[i][j]==1]
    
    def vi(self, nodo):
        if nodo not in self.v:
            return []
        j = self.v.index(nodo)
        return [self.v[i] for i in range(len(self.mat)) if self.mat[i][j]==1]
    
    def show(self):
        for fila in self.mat:
            print(fila)

def main():
    g = G()
    
    print("csv 1")
    g.csv("01.csv")
    g.show()
    print("min:", g.min())
    print("max:", g.max())
    print("vd0:", g.vd(0))
    print("vi0:", g.vi(0))
    
    print("\csv 2")
    g.csv("02.csv")
    g.show()
    print("min:", g.min())
    print("max:", g.max())
    print("vd0:", g.vd(0))
    print("vi4:", g.vi(4))
    
    print("\ncsv1")
    g.js("01.json")
    print("min:", g.min())
    print("max:", g.max())
    print("vd1:", g.vd('1'))
    print("vi10:", g.vi('10'))

if __name__ == "__main__":
    main()

def GCD(num, deno):
    if(deno == 0):
        return num
    else:
        return GCD(deno ,num % deno)
class Fraction:
    def __init__(self):
        self.num = 0
        self.deno = 1
    def get(self):
        self.num = int(input("Enter a numerator: "))
        self.deno = int(input("Enter denominator: "))
    def simplfy(self):
        common_divisor = GCD(self.num, self.deno)
        self.num //= common_divisor
        self.deno //= common_divisor
    def __add__(self, f):
        temp = Fraction()
        temp.num = (self.num * f.deno) + (f.num * self.deno)
        temp.deno = self.deno * f.deno
        return temp
    def display(self):
        self.simplfy()
        print(self.num, "/" ,self.deno)
f1 = Fraction()
f1.get()
f2 = Fraction()
f3 = f1 + f2
print("RESULTANT FRACTION: ")
f3.display()
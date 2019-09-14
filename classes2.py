class Matrix:
    def __init__(self,list):
        self.list = list
    def display(self):
         print(self.list)
    def __add__(self, M):
        temp = Matrix([])
        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                temp.list.append(self.list[i][j]+M.list[i][j])
        return temp
m1 = Matrix([[1,2],[2,3]])
m2 = Matrix([[3,4],[5,1]])
m3 = Matrix([])
m3 = m1 + m2
print("Resultant Matrix is:  ")
m3.display()




# create a method to find whether to line intersect each other or not 

class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)
    
    def intersection_of_line(self,other):
        if self.A*other.B == self.B*other.A:

            if self.A*other.C == self.C**other.A:
                return 'Lines are coincident'
            else:
                return 'Lnes are parallel(do not intersect)'
        
        else:
            return 'Lines intersect at one point'

l1 = Line(1,2,3)
l2 = Line(2,4,5)

print(l1)
print(l2)
print(l1.intersection_of_line(l2))
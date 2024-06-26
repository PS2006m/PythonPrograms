class Point:
    def __init__(self,x,y):
        print("Init called")
        self.x=x
        self.y=y
    def _str_(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
p1=Point(10,20)#init method called
print(p1)#str method called


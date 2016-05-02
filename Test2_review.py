# class Color(object):
#     def __init__(self,c):
#         self.color = c
#         self.red = c[0]
#         self.green = c[1]
#         self.blue = c[2]
        
#     def __str__(self):
#         return('red: %s, green: %s, blue: %s') % (self.red,self.green,self.blue)
        
#     def __add__(self,rhs):
#         return Color(((self.red+rhs.red)//2,(self.green+rhs.green)//2,(self.red+rhs.red)//2))

# class GrayScaler(Color):
#     def __init__(self,c = (255,255,255)):
#         super().__init__(c)
        
#     def Lightness(self):
#         return (max(self.red,self.green,self.blue) + min(self.red,self.green,self.blue)) / 2
      
#     def Average(self):
#         return (self.red + self.green + self.blue) / 3  
        
#     def Luminosity(self):
#         return 0.21 * self.red + 0.72 * self.green + 0.07 * self.blue
        
#     def Custom(self,w1,w2,w3):
#         return w1 * self.red + w2 * self.green + w3 * self.blue
        
#     def SetColor(self,w1,w2,w3):
#         self.red = w1
#         self.green = w2
#         self.blue = w3

# class A(object):

#     def __init__(self):
#         print("Constructor A was called")

# class B(A):

#     def __init__(self):
#         super().__init__()
#         print("Constructor B was called")

# class C(B):

#     def __init__(self):
#         super().__init__()
#         print("Constructor C was called")  

# class Test(object):
#     def no_return(self):
#         print("I am about to raise an exception") 
#         raise Exception("This is always raised") 
#         print("This line will never execute") 
#         return "I won't be returned" 
#     def ratio(a,b):
#         try:
#             return a / b 
#         except ZeroDivisionError:
#             print("Divided by zero")
#         except TypeError:
#             print("Type Error")

class item(object):
    def __init__(self,key,name,cost):
        self.key = key              # Unique key for a candy
        self.name = name            # Name of candy
        self.cost = cost            # Cost per box or bag
        #self.amount = amount            # Number in stock
        
    def __str__(self):
        return ('id:%d , name:%s , cost:%3.2f') % (self.key, self.name, self.cost)
        
class inventory(object):
    def __init__(self):
        self.d = {}
        
    def __str__(self):
        val = ''
        for i in self.d:
            val += str(self.d[i])
            val += "\n"
        return val
        
    def addItem(self,item,amount):
        if not item.key in self.d:
            self.d[item.key] = [amount,item.cost]
        else:
            self.d[item.key][0] += amount
            
    def sellItem(self,key,amount):
        self.d[key][0] -= amount
        return self.d[key][1] * amount


if __name__ == '__main__':
    # c1 = Color((100,255,255))
    # c2 = Color((0,0,0))
    # c3 = c1 + c2
    # print(c3)
    # print(c1.red)
    # c1.blue = 255
    # print(c1)
    # myColor = (255,0,0)
    # grayish = GrayScaler(myColor)
    # print(grayish)
    # gray1 = grayish.Average()
    # print(gray1)
    # gray2 = grayish.Custom(.33,.44,.23)
    # print(gray2)
    # grayish2 = GrayScaler() # defaults to black in the class if no color provided
    # print(grayish2)
    # grayish2.SetColor(255,192,203)
    # print(grayish2)
    # gray3 = grayish2.Luminosity()
    # print(gray3)
    # x = C()
    # What happens? Anything printed?
    # t = Test()
    # t.no_return()
    a = item(1,"paper pad",3.99)
    b = item(2,"tape",1.99)
    c = item(3,"scissors",4.99)
    i = inventory()
    i.addItem(a,35)
    i.addItem(b,20)
    i.addItem(c,40)
    print(i.sellItem(2,4))
    print(a)
    print(i)
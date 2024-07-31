class Block:
    def __init__(self, color, height, width):
        self._color = color
        self._height = height
        self._width = width

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        
class KBlock(Block):
    def __init__(self, color, height, width, material):
        super().__init__(color, height, width)
        self.material = material  


block = Block('white', 20, 30)
#block.color = 'black'
print(block.color)



penoplast = KBlock('white', 20, 30, 'penoplast')
print(penoplast.color)     
print(penoplast.material)  



'''

class Class1():
    def method(self):
        print("Method of Class1")

class Class2():
    def method(self):
        print("Method of Class2")

def b_method(cl):
    cl.method()

cl1 = Class1()
cl2 = Class2()

b_method(cl1)
b_method(cl2)



class obsh_class():
    def big_method(self):
        print('obsh_vivod')

class podclass(obsh_class):
    def __init__(self, attribute_1, attribute_2):
        #super().__init__()
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2



PDclass = podclass('A1', 'A2')
print(PDclass.attribute_1)
PDclass.big_method()'''






#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size

    @property
    def size(slef):
        return slef.__size   
    
    @size.setter
    def size(self, size):
        if type(size) != int:
            print('size must be an integer')
        else:
            self.__size = size   

    def cobble(slef):
        print('Your shoe is as good as new!')
        slef.condition = 'New'        
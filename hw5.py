'''
Author: Zach Rosson
Date: 2/15/18
Class: ISTA 350
Section Leader: Sarah Stueve
Colabortion:                                             
Description:
this program will take a binary string put it into a lst and use different functions to do different 
math related things to it. there is a add function, subtract function, negative function, absolute 
function, equal function, left greater function, and a function to get the decimal value of the 
binary number.
'''
import functools

class Binary:
    def __init__(self, bin_str='0'):
        '''this function takes one argument. it takes a str of 1's and 0's and sets up the instance'''
        wrong = [i !='1' and i !='0' for i in bin_str]
        if len(bin_str) > 16 or True in wrong:
            raise RuntimeError("Incorrect input for Binary...")
        self.num_list = [int(x) for x in bin_str]
        if len(self.num_list) == 0:
            self.num_list .append(0)
        if len(self.num_list) != 16:
            self.pad()
    def pad(self):
        '''this function takes no arguments. this function adds a pad onto the Binary list
        if the length of the list is shorter than 16'''
        while len(self.num_list) != 16:
            self.num_list.insert(0, self.num_list[0])
    def __repr__(self):
        '''this function takes no arguments. this function returns a string of Binary'''
        return ''.join(str(i) for i in self.num_list)
    def __add__(self, other):
        '''this function takes one argument. the argument is an instance to be added from
        self. this returns a new binary of self + other'''
        result = []
        carry = 0
        for i in range(15, -1, -1):
            bit_sum = carry + self.num_list[i] + other.num_list[i]
            result.insert(0, bit_sum % 2)
            carry = int(bit_sum > 1)
        if self.num_list[0] == other.num_list[0] != result[0]:
            raise RuntimeError("Binary: Overflow")
        return Binary(''.join([str(i) for i in result]))
    def __neg__(self):
        '''this function takes no arguments. '''
        negat = ''
        for b in self.num_list:
            if b == 0:
                negat += '1'
            else:
                negat += '0'
        return Binary(negat) + Binary("01")
    def __sub__(self, other):
        '''this function takes one argument. the argument is an instance to be subtracted from
        self. this returns a new binary of self - other'''
        return self + -other
    def __int__(self):
        '''this function takes no arguments. this function returns the decimal value of the binary self'''
        decim = 0
        anti_pos = 0
        if self.num_list[0] == 1:
            anti_pos = 1
        for i in range(16):
            decim += self.num_list[len(self.num_list) - 1  -i] * (2**i)
        if anti_pos == 1:
            decim = decim - 65536
        return decim
    def __eq__(self, other):
        '''this function takes one argument. the argument is an instance to be compared with
        self to see if they are equal'''
        return self.num_list == other.num_list
    def __lt__(self, other):
        '''this function takes no arguments. this function returns true if self > other or false otherwise'''
        one = int(self)
        two = int(other)
        if one < two:
            return True
        else:
            return False
    def __abs__(self):
        '''this function takes no arguments. this function return the absolute of the instances self lst'''
        lst = self.num_list
        str1 = ''.join(str(i) for i in lst)
        if self.num_list[0] == 1:
            return -Binary(str1)
        else:
            return Binary(str1)
def main():
    '''this program will take a binary string put it into a lst and use different functions to do different 
    math related things to it. there is a add function, subtract function, negative function, absolute 
    function, equal function, left greater function, and a function to get the decimal value of the 
    binary number.'''
if __name__ == '__main__':
    main()
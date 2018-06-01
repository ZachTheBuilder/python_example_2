'''
Author: Zach Rosson
Date: 2/29/18
Class: ISTA 350
Section Leader: Sarah Stueve
Colabortion:                                             
Description:
this program will reverse an array, double an array, double an array with out change the original, 
take all the evens and make them 0 and all the odds and make them 1, square all the evens, do a 
binary search, insert into an array, swap values and given points, and add two arrays together
'''
import numpy as np
def reverse(arr):
    '''this fuction takes an array copies it and reverse it'''
    new_arr = arr.copy()
    return new_arr[::-1]
def odd_even_mask(arr):
    '''this function takes an array copies it  and returns the new array that has ones where the
    odds where and 0 where the evens were'''
    new_arr = arr.copy()
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            new_arr[i] = 0
        else:
            new_arr[i] = 1
    return new_arr
def cycle(arr, num):
    '''this function takes an array and int as its peramiter. it will copy the array and return that
    new array but shifted the way and amount dictated by the int'''
    new_arr = arr.copy()
    while num > len(arr):
        num -= len(arr)
    new_arr = np.append([new_arr[-num:]], new_arr[:-num]) 
    return new_arr
def double(arr):
    '''this functions takes an array and copies it and returns the new array with everything doubled
    inside it'''
    new_arr = arr.copy()
    return new_arr * 2
def double_ip(arr):
    '''this function takes an array doubles it and returns nothing changing the array in place'''
    arr *= 2
def square_evens(arr):
    '''this function takes an array and doubles every even value in place. return none'''
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]**2
def binary_search(key, arr):
    '''this funciton takes an array and an int as its peramiters. it uses a binary search tech
    to search through the arr to find the indices at the given key'''
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < key:
            lo = mid + 1
        elif key < arr[mid]:
            hi = mid - 1
        else:
            return mid
    return -1
def insert(arr, index, value, overwrite):
    '''this fucntion takes an array, bool, and two ints. if the bool is true overwrite in the array
    else add to the array. if the index is outside the array raise runtimeeorror. otherwiswe it will
    replce the given value at the given index'''
    if index < len(arr):
        if overwrite:
            for i in range(len(arr)):
                if i == index:
                    arr[i] = value
        else:
            for i in range(len(arr)):
                if i == index:
                    temp = arr[i]
                    arr[i] = value
                    for x in range(i+1,len(arr)-1):
                        next = arr[x]
                        arr[x] = temp
                        temp = next
                    arr[len(arr)-1] = temp
    else:
        raise IndexError("IndexError")
def swap(arr, pos1, pos2):
    '''this function takes an array, and two ints. the ints will be swaped with each other in the 
    array'''
    num1 = 0
    num2 = 0
    for i in range(len(arr)):
        if i == pos1:
            num1 = arr[i]
        if i == pos2:
            num2 = arr[i]
    for i in range(len(arr)):
        if i == pos1:
            arr[i] = num2
        if i == pos2:
            arr[i] = num1
def add_arrays(arr1, arr2):
    '''this fucntion takes two arrays. it will reutnr the length of the loger array. it will add
    the value from both array and put it in the same index in the new array. '''
    new_arr = []
    if len(arr1) > len(arr2):
        for i in range(len(arr1)):
            if i >= len(arr2):
                new_arr.append(arr1[i])
            else:
                new_arr.append(arr1[i] + arr2[i])
    else:
        for i in range(len(arr2)):
            if i >= len(arr1):
                new_arr.append(arr2[i])
            else:
                new_arr.append(arr1[i] + arr2[i])
    return np.array(new_arr)
def main():
    '''this program will reverse an array, double an array, double an array with out change the original, 
    take all the evens and make them 0 and all the odds and make them 1, square all the evens, do a 
    binary search, insert into an array, swap values and given points, and add two arrays together'''
    
if __name__ == '__main__':
    main()
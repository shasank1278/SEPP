import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def binary_search(arr,low, high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return-1
arr=[]
n=int(input("enter the number of element"))


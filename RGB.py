import hashlib
import os
from PIL import Image
import math
from random import randrange, seed


def shuffle_encrypt(dir_address,BLKSZ,file_address):
    #function to rotate the given pixle block 180 degree
    def rot(arr, n, x, y): 
        temple = []
        for i in range(n):
            temple.append([])
            for j in range(n):
                temple[i].append(arr[x+i, y+j])
        for i in range(n):
            for j in range(n):
                arr[x+i,y+j] = temple[n-1-i][n-1-j]
    
    #function to rotate pixle of every share of image
    def rotate(im,arr,BLKSZ):
        xres,yres =im.size
        for i in range(2, BLKSZ+1):
            for j in range(int(math.floor(float(xres)/float(i)))):
                for k in range(int(math.floor(float(yres)/float(i)))):
                    rot(arr, i, j*i, k*i)
        for i in range(3, BLKSZ+1):
            for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
                for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
                    rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))

    #reafing image file
    image = Image.open(file_address,"r")
    #spliting image into 3 share of its RGB components
    lis=image.split()
    r=lis[0]
    g=lis[1]
    b=lis[2]
    arr1 = r.load()
    arr2 = g.load()
    arr3 = b.load()
    #calling rotate function for each component
    rotate(r,arr1,BLKSZ)
    rotate(g,arr2,BLKSZ-20)
    rotate(b,arr3,BLKSZ-10)
    #after shuffling the RGB component merging all 3 component to produce one single image
    image=Image.merge("RGB",(r,g,b))
    image.save(dir_address)
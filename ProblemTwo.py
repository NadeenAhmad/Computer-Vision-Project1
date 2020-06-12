import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import ImageFilter
import math

def integralImage(image):
    F = np.asarray(PIL.Image.open(image))
    #F = np.asarray(PIL.Image.open('C:/Users/Malak/Desktop/CV1/Cameraman.bmp'))
    
    I = np.random.randn(*F.shape) #normalized input
    S = np.random.randn(*F.shape) #summation of rows
    II = np.random.randn(*F.shape)#summation of columns, final matrix
    tmp = 0
    mm = 0
    norm = 0
    maxValue = max(map(max, F))
    for i in range(len(F)):
        for j in range(len(F[0])):
            norm = (F[i][j]/maxValue)*255
            I[i][j] = norm 
    
    
    for i in range(len(I)):
        for j in range(len(I[0])):
            if(j == 0):
                mm = I[i][j]
                S[i][j] = mm
            else:
                jj = j
                while(jj>-1): 
                    tmp +=I[i][jj]
                    jj = jj-1
                S[i][j] = tmp
                tmp = 0
              
             
           
    for j in range(len(S[0])):
        for i in range(len(S)):
            if(i == 0):
                mm = S[i][j]
                II[i][j] = mm
            else:
                ii = i
                while(ii>=0):
                    tmp+=S[ii][j]
                    ii = ii-1
                II[i][j] = tmp
                tmp = 0
   # plt.gcf()
    plt.matshow(II, cmap="gray") 
   # print(II)
    
    plt.savefig('Camera_Integ.png')
    return II
    
           
def AverageFilter(image,s):
    Array = integralImage(image)
    size = s
    start = s//2
    final = np.random.randn(*Array.shape)
   # print(new)
    A = 0
    B = 0
    C = 0
    D = 0
    
    for i in range(start,len(Array)-start):
        for j in range(start,len(Array[0])-start):
            A = Array[i-start][j-start]
            B=Array[i-start][j+start]
            C = Array[i+start][j-start]
            D= Array[i+start][j+start]
          
            r =  (A+D-B-C)*(255/(size*size))
            final[i][j] = (math.ceil(r))
            A=0
            B=0
            C=0
            D=0
            #print(final[i][j]) 

    plt.gcf()
    plt.matshow(final, cmap="gray") 
    if(s == 3):
        plt.savefig('Camera_Filt_3.jpg')
    if(s==5):
        plt.savefig('Camera_Filt_5.jpg')
    
AverageFilter('C:/Users/Malak/Desktop/CV1/Cameraman.bmp',3)  
AverageFilter('C:/Users/Malak/Desktop/CV1/Cameraman.bmp',5)   
'''
Problem link - https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
@author - anurag kar
'''


#!/bin/python3
import sys

def jumpingOnClouds(c,n):
    min=0
    i=0
    while(i<n):
        if(i<n-2):
            if((c[i+1]==1) and (c[i+2]==0)):
                i+=2

            elif((c[i+1]==0) and (c[i+2]==0)):
                i+=2

            elif((c[i+1]==0) and (c[i+2]==1)):
                i+=1

        else:
            if(c[n-3]==0):
                min+=1
            else:
                min+=2
            break
     

        min+=1
        print("JUMPS:")
        print(min)
        print("CLOUD:")
        print(i)
        print("\n")
            

    return min

if __name__=='__main__':

    n=int(input())
    if((n<2) or (n>100)):
        sys.exit(1)
        
    c = list(map(int, input().strip().split()))[:n]
    
    if((c[0]!=0) or (c[n-1]!=0)):
        sys.exit(1)

    minimum=jumpingOnClouds(c,n)
    if(n==2):
        print(minimum)
    elif(n!=2):
        print(minimum-1)


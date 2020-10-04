'''
Problem link - https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
@author - anurag kar
'''
#!/bin/python3

import sys

def Pairs(S, N):

    number = 0
    count=0
    Flag=0
    for i in range(N):  
      Flag=0
      for k in range(i):
        if (S[i] == S[k]):
          Flag=1
      
      if (Flag ==1):
        pass

      else:
        count=0 
        for j in range((i+1),N):
            if (S[i] == S[j]):
                if((count%2)==0):
                    number+=1
                else:
                    pass
                count+=1


    return(number)

if __name__ == "__main__":
  
  n=int(input())
  ar = list(map(int, input().strip().split()))[:n]
  if (n<1) or (n>100) :
    sys.exit(1)
  
  for x in ar :
    if (x<1) or (x>100) :
      sys.exit(1)

  P=Pairs(ar, n)
  print(P)
  sys.exit(0)

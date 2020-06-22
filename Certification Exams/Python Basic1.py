'''
Input 1:
STDIN      Function
-----      --------
2 5    →   arguments = [2, 5]

Output 1:
3.50

Input 2:
STDIN      Function
-----      --------
7      →   arguments = 7

Output 2:
7.00
'''

def avg(*nums):
    return sum(nums)/len(nums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
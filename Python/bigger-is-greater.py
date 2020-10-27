
'''

Bigger is Greater:
https://www.hackerrank.com/challenges/bigger-is-greater/problem

'''

def swap(a, ix1, ix2):
    tmp = a[ix1]
    a[ix1] = a[ix2]
    a[ix2] = tmp

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # convert string to list of chars
    chars = list(w)
    # See if we can swap 2 characters, starting at the last character and working forward
    swapped = False
    smallest_ix = len(chars) - 1
    for i in range(len(chars) - 2, -1, -1):
        if chars[i] < chars[i + 1]:
            smallest_char = 'zzz'
            for c_i in range(i+1, len(chars)):
                if chars[c_i] > chars[i] and chars[c_i] < smallest_char:
                    smallest_char = chars[c_i]
                    smallest_ix = c_i

            swap(chars, i, smallest_ix)

            ret_str = chars[:i+1]
            sort_str = chars[i+1:]
            sort_str = sorted(sort_str)
            print(ret_str, sort_str)
            swapped = True
            break

    if not swapped:
        return "no answer"

    return "".join(list(ret_str + sort_str))

if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)

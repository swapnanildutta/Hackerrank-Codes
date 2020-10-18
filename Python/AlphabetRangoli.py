# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

# Input Format

# Only one line of input containing , the size of the rangoli.

# Constraints


# Output Format

# Print the alphabet rangoli in the format explained above.

# Sample Input

# 5
# Sample Output

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


def print_rangoli(n):
    import string
    letter_count = dict(zip(string.ascii_lowercase, [0]*26))
    alph =  list([key for key  in letter_count.keys()])
    d = (n-1)*2
    k = n-1 
    f = 0
    for i in range(n):
        k-=1
        m= int(k)
        if i!=0:
            f = 1
        if m==-1:
            m= None
        print("-"*d, end="")
        print("-".join(alph[n-1:m:-1]), end="")
        print("-"*(f)+"-".join(alph[n-i:n]), end="")
        print("-"*d)
        d -= 2
    d = 2
    f = 1
    for i in range(n-1,0,-1):
        if i==1:
            f = 0
        print("-"*d, end="")
        print("-".join(alph[n-1:n-i-1:-1]),end="")
        print("-"*f+"-".join(alph[n-i+1:n]), end="")
        print("-"*d)
        d += 2


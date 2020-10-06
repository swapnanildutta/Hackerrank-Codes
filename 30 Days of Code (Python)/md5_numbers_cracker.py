import hashlib
import time
import random
import numpy as np

counter = 1

md5_pass = input("Enter md5 password: ")

for i in np.arange(0.0, 1000000.0, 0.0000001):
    hash_obj = hashlib.md5(i)
    start = time.time()
    print("trying paasword %d -----> %s " % (counter, i))
    counter += 1
    end = time.time()
    t_time = end - start

    if hash_obj == md5_pass:
        print("Password Found !!! Password is : %s " % i)
        print("Total Running Time: ", t_time, "Seconds")
        time.sleep(10)
        break

else: 
    print("Password Not Found")
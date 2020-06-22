'''
Input 1:
STDIN           Function
-----           -------
2             → number of queries, q = 2
car 151 km/h  → query parameters = ["car 151 km/h", "boat 77"]
boat 77

Output 1:
Car with the maximum speed of 151 km/h
Boat with the maximum speed of 77 knots

Input 2:
STDIN         Function
-----         --------
3           → number of queries, q = 2
boat 101    → query parameters = ["boat 101", "car 120 mph", "car 251 km/h"]
car 120 mph
car 251 km/h

Output 2:
Boat with the maximum speed of 101 knots
Car with the maximum speed of 120 mph
Car with the maximum speed of 251 km/h
'''
class Car:
    def __init__(self, max_speed, unit_speed):
        self.max_speed=max_speed
        self.unit_speed=unit_speed
    
    def __str__(self):
        return 'Car with the maximum speed of {} {}'.format(self.max_speed,self.unit_speed)

class Boat:
    def __init__(self, max_speed):
        self.max_speed=max_speed
    
    def __str__(self):
        return 'Boat with the maximum speed of {} knots'.format(self.max_speed)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
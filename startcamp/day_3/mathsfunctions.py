print (__name__)

def average(numbers):
    return sum (numbers) / len (numbers)

def cube(x) : 
    return x*x*x 


def main():
    my_score=[12,34,15,12]
    print('평균:',average(my_score))
    print (cube(3))
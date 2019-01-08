def second_number(*args):
    numbers=list(args)
    for i in numbers:
        n=0
        if i < numbers[n-2] and i < numbers[n-1]:
            n+1           
        else:
            return i
        
print (second_number(100,12,13))

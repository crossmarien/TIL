print (__name__)

from mathsfunctions import cube,average


def main():
    my_score=[12,34,15,12]
    print('평균:',average(my_score))
    print (cube(3))


if __name__=='__main__':
    main()
from derivate import derivate
from method import newton_method

def main():
    '''Run code.'''   
    res, cnt = newton_method("x**3", 3, 0.1 ,100)
    print(res, cnt)


if __name__ == "__main__":
    main()

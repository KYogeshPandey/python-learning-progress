x=2
match x:
    case 0:
        print("x is zero")
    case 1 if x%2==0:
        print("x is even")
    case _ if x<10:
        print("x is <10")
    case _:
        print("x is >=10")
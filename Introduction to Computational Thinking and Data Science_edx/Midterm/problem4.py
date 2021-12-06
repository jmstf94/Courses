def eq(x1,x2,x3,x4):
    return 25*x1+10*x2+5*x3+x4

def solve(s):
    """
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    x = 0
    x1, x2, x3, x4 = (0,0,0,0)
    while (not eq(x1,x2,x3,x4)==s):
        x+=1
        for x1 in range(0,x+1):
            for x2 in range(0,x+1):
                for x3 in range(0,x+1):
                    for x4 in range(0,x+1):
                        if eq(x1,x2,x3,x4)==s:
                            return [x1,x2,x3,x4]


def test():
    test_dict = {"1":[0, 0, 0, 1], "5":[0, 0, 1, 0], "10":[0, 1, 0, 0], "25":[1, 0, 0, 0],
    "4":[0, 0, 0, 4], "20":[0, 2, 0, 0], "50":[2, 0, 0, 0], "15":[0, 1, 1, 0],"35":[1, 1, 0, 0],
    "26":[1, 0, 0, 1], "27":[1, 0, 0, 2], "28":[1, 0, 0, 3], "29":[1, 0, 0, 4],
    "30":[1, 0, 1, 0], "99":[3, 2, 0, 4], "100":[4, 0, 0, 0]}
    cornum = 0
    for key in test_dict:
        calc = solve(eval(key))
        corans = test_dict.get(key)
        if calc == corans:
            print("True: " + key + "gives " + str(corans))
            cornum+=1
        else:
            print("False: " + key + "gives "+ str(corans)+" but you found " + str(calc))
        grade = (cornum/0.8)
    print("Your grade is : "+str(grade)+"/20.")

test()

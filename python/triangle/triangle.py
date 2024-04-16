def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    is_equilateral = False
    if a == b and b == c and a != 0:
        is_equilateral = True
    return is_equilateral
def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    is_isosceles = False
    if equilateral(sides) == True:
        is_isosceles = True
    if (a != b and b == c) or (a == b and a != c) or (a == c and a != b):
         if a + b >= c and b + c >= a and a + c >= b:
            is_isosceles = True
    return is_isosceles
def scalene(sides):  
    a = sides[0]
    b = sides[1]
    c = sides[2]
    is_scalene = False
    if equilateral(sides) == False:
        if isosceles(sides) == False:
            if a + b >= c and b + c >= a and a + c >= b:
                is_scalene = True
    return is_scalene
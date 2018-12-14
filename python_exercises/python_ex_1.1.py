def root_equation2():
    a=float(input('insert value of a: '))
    b=float(input('insert value of b: '))
    c=float(input('insert value of c: '))
    from math import sqrt
    if b**2-4*a*c>=0:
        root1=(-b+sqrt(b**2-4*a*c))/2*a
        root2=(-b-sqrt(b**2-4*a*c))/2*a
        return root1, root2
    else:
        return 'no real solution'

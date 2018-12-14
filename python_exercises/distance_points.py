def distance_btw_two_points(x,y):
    a=int(x[0]); b=int(x[1])
    c=int(y[0]); d=int(y[1])
    x=[a,b]
    y=[c,d]
    return sqrt((a-c)**2 + (b-d)**2)



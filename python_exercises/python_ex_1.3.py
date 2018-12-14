def distance_btw_points3(): #function to calculate distance btw 2 points in 3D plane
    a=input('give coordinates of first point between []: ') #create 2 lists for coordinates
    b=input('give coordinates of secondo point between []: ')
    from math import sqrt
    distance = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    return distance 

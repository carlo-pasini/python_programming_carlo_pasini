#This script takes the string s and gives back anothere string f in which 3 is
#added to each number

s = '234 4329 7654 8923'
v = ''                      #create cumulative function
for i in range(0,18):       #use numbers 0 to 17 to refer to index of string s
    if s[i] != ' ':         #avoid the trasnformation of ' ' in int 
       d = int(s[i]) + 3    #add 3 to each substring of s(transformed in int)
       v = v + ' ' + str(d) #define a function 'v' that will store the new
    else:                   #substrings of s
        d = ' '              

g = v.split() #creates a list of all numbers in 'v'
f = ''.join(g[0:3])+' '+''.join(g[3:7])+' '+''.join(g[7:11])+' '+''.join(g[11:15])
    #create a new string with the propper spacing btw different blocks of dig. 
print ('%s'%f)



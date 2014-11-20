#PROBLEM 4  (10/10 points)

def myLog(x, b):
    i = 0
    while b**(i + 1) <= x:
        i += 1
    return i
    
#PROBLEM 5  (10/10 points)

def laceStrings(s1, s2):
    length = len(s1) + len(s2)
    lacedstr = ""
    s1taken = 0
    s2taken = 0
    for i in range(0, length):
        
        if ((s1taken >= len(s1)) and s2taken <= len(s2)):
                lacedstr = lacedstr + s2[s2taken]
                s2taken += 1
        elif ((s2taken >= len(s2)) and s1taken <= len(s1)):
            lacedstr = lacedstr + s1[s1taken]
            s1taken += 1 
            
    
        elif i % 2 == 0:
                try:
                    lacedstr = lacedstr + s1[i/2]
                    s1taken += 1
                except IndexError:
                    try:
                        lacedstr = lacedstr + s2[i/2]
                        s2taken += 1
                    except IndexError:
                        pass
        elif i % 2 != 0:
                try:
                    lacedstr = lacedstr + s2[(i-1)/2]
                    s2taken += 1
                except IndexError:
                    try:
                        lacedstr = lacedstr + s1[(i+1)/2]
                        s1taken += 1
                    except IndexError:
                        pass
    return lacedstr
    
#PROBLEM 6  (10/10 points)

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + laceStringsRecur(s1[1:], s2[1:])
    return helpLaceStrings(s1, s2, '')
    
#PROBLEM 7  (10/10 points)

def McNuggets(n):
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                if 6*x + 9*y + 20*z == n:
                    #print "x=%d y=%d z=%d" % (x, y, z)
                    return True
    return False
    
#PROBLEM 8-1  (5/5 points)

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

#PROBLEM 8-2  (5/5 points)

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

#PROBLEM 8-3  (5/5 points)

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)

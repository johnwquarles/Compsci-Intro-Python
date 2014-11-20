#PROBLEM 1: PAYING THE MINIMUM  (10/10 points)

apr = annualInterestRate
mpr = monthlyPaymentRate
t = 0

def p(x):
    next = ( x - mpr * x ) + ( ( apr / 12 ) * ( x - (mpr * x ) ) )
    return next
    
for x in range(1, 13):
    print "Month : %s" % x
    print "Minimum monthly payment: %s" % round((balance * mpr), 2)
    t = t + (balance * mpr)
    balance = p(balance) 
    print "Remaining balance: %s" % round(balance, 2)
    
print "Total paid: %s" % round(t, 2)
print "Remaining balance: %s" % round(balance, 2)

#PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15/15 points)

apr = annualInterestRate #annual interest rate here!

def p(x):
    next = ( x - fixedpay ) + ( ( apr / 12 ) * ( x - (fixedpay) ) )
    return next

for i in range(0, 1000, 10):    
    debt = balance                           #write balance here!
    fixedpay = i
    for x in range(1, 13):
        debt = p(debt) 
    if debt <= 0:
        break
print fixedpay

#PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER  (25/25 points)

n = 0
debt = balance
testdebt = balance
apr = annualInterestRate


def p(x):
    next = ( x - fixedpay ) + ( ( apr / 12.0 ) * ( x - (fixedpay) ) )
    return next

hi = ((debt*(1+((annualInterestRate)/12.0))**12.0)/12.0)
lo = (debt/12.0)
tol = .001
i = (hi + lo)/2.0 

while n <= 9999:
    
    debt = balance 
    testdebt = balance
    
    fixedpay = i
    fixedpaycopy = i             #
    for x in range(1, 13):      #   f(c) = debt
        debt = p(debt)           #
        debt = round(debt,3)
    
    if abs(debt) <= tol:
        fixedpay = round(fixedpay,2)
        print fixedpay
        break
    
    fixedpay = hi                #
    for x in range(1, 13):      #   f(a) = testdebt
        testdebt = p(testdebt)   #
    
    if (debt * testdebt) > 0:
        hi = fixedpaycopy
    else:
        lo = fixedpaycopy
    i = (hi + lo)/2.0
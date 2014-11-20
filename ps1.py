#COUNTING VOWELS  (10/10 points)

vowelcount = 0
for x in "aeiou":
    vowelcount += s.count(x)
print vowelcount

#COUNTING BOBS  (15/15 points)

x = 0
count = 0
while True:
    check = s[x:x+3]
    if check == "bob":
       count +=1
    if x == (len(s) - 3):
        break
    x += 1
        
print count

#ALPHABETICAL SUBSTRINGS  (15/15 points)

longest = ""
current = s[0]

for x in range(1, len(s)-1):
    if s[x] >= s[x-1]:
        current = current + s[x]
        if len(current) > len(longest):
            longest = current
    else:
        if len(current) > len(longest):
            longest = current
        current = s[x]

if len(longest) > 0:
    if longest[len(longest)-1] == s[len(s)-2]:
        if s[len(s)-1] > longest[len(longest) - 1]:
            longest = longest + s[len(s)-1]

print "Longest substring in alphabetical order is: %s" % longest
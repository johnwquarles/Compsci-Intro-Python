#PROBLEM 1: ENCRYPTION (BUILDCODER)  (15/15 points)

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    dict = {}
    for A in ALPHA:
        
        oldIndex = ALPHA.index(A)
        newIndex = (oldIndex + shift) % 26
        dict[A] = ALPHA[newIndex]
        
    for a in alpha:    
        
        oldIndex = alpha.index(a)
        newIndex = (oldIndex + shift) % 26
        dict[a] = alpha[newIndex]
    
    return dict
    
#PROBLEM 1: ENCRYPTION (APPLYCODER)  (15/15 points)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newText = ""
    for a in text:
        newText += coder.get(a, a)
    return newText
    
#PROBLEM 1: ENCRYPTION (APPLYSHIFT)  (5/5 points)

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.

    return applyCoder(text, buildCoder(shift))
    
#PROBLEM 2: DECRYPTION (FINDBESTSHIFT)  (15/15 points)

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    best = 0
    bestShift =0
    
    for i in range(0, 26):
        decryptTry = applyShift(text, i)
        
        decryptTryWords = decryptTry.split(" ")
        
        numberOfWords = 0
        for word in decryptTryWords:
        
            if isWord(wordList, word):
                numberOfWords += 1
        if numberOfWords > best:
            best = numberOfWords
            bestShift = i
    
    return bestShift
    
#PROBLEM 2: DECRYPTION (DECRYPTSTORY)  (5/5 points)

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    encryptedStory = getStoryString()
    bestShift = findBestShift(wordList, encryptedStory)
    return applyShift(encryptedStory, bestShift)
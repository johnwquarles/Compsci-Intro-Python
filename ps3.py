#RADIATION EXPOSURE  (25/25 points)

def radiationExposure(start, stop, step):
    sum = 0
    i = start
    while i < stop:
        sum += f(i) * step
        i += step
    return sum
    
#HANGMAN PART 1: IS THE WORD GUESSED?  (5/5 points)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in range(0, len(secretWord)):
        letter = secretWord[x]
        if (letter in lettersGuessed) == False:
            return False
    return True
    
#PRINTING OUT THE USER'S GUESS  (5/5 points)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ""
    for x in range(0, len(secretWord)):
        if (secretWord[x] in lettersGuessed) == True:
            result += secretWord[x]
        else:
            result += "_ "
    return result
    
#PRINTING OUT ALL AVAILABLE LETTERS  (5/5 points)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    avail = ""
    import string
    for x in range(0, len(string.ascii_lowercase)):
        if (string.ascii_lowercase[x] in lettersGuessed) == False:
            avail += string.ascii_lowercase[x]
    return avail
    
#HANGMAN PART 2: THE GAME  (15/15 points)

def hangman(secretWord):
	print "Welcome to the game Hangman!"
	print "I am thinking of a word that is %s letters long." % len(secretWord)
	print "------------"
	lettersGuessed = []
	mistakesMade = 0
	while mistakesMade < 8:
		sameletter = 0
		print "You have %d guesses left." % (8 - mistakesMade)
		print "Available letters: %s" % getAvailableLetters(lettersGuessed)
		guess = raw_input("Please guess a letter: ").lower()
		if (guess in lettersGuessed) == True:
			print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed)
			print "------------"
			sameletter = 1
		lettersGuessed.append(guess)
		good = 0
		for x in range(0, len(secretWord)):
			if (secretWord[x] == guess and sameletter != 1):
				print "Good guess: %s" % getGuessedWord(secretWord, lettersGuessed)
				print "------------"
				good = 1
				if isWordGuessed(secretWord, lettersGuessed) == True:
					print "Congratulations, you won!"
					return True
				break
		if (good == 0 and sameletter != 1):
			mistakesMade += 1
			print "Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed)
			print "------------"
	print "Sorry, you ran out of guesses. The word was %s ." % secretWord
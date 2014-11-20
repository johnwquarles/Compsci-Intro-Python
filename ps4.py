#WORD SCORES  (10/10 points)

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    turn = 0 #check for whether or not we're on the first turn
    x = 0
    y = 0
    if ((turn == 0) and (len(word) == n)):   #check for initial turn/all letter bonus
        for i in word:
            x += SCRABBLE_LETTER_VALUES[i]
        y = (x * len(word)) + 50
        return y
    elif len(word) > n:
        print "You don't have that many letters!"
    else:
        for i in word:
            x += SCRABBLE_LETTER_VALUES[i]
        y = x * len(word)
        return y

#DEALING WITH HANDS  (10/10 points)

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for i in word:
        if i in newHand:
            newHand[i] -= 1
            if newHand[i] <= 0:
                del newHand[i]
    return newHand

#VALID WORDS  (10/10 points)

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if (word in wordList) != True:
        return False
    else:
        amt = getFrequencyDict(word)
        for i in word:
            if amt.get(i, 0) > hand.get(i, 0):
                return False
        return True

#HAND LENGTH  (5/5 points)

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())
    
#PLAYING A HAND  (15/15 points)

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
   # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        # Ask user for input
        word = raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        # If the input is a single period:
        if word == "." :
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) != True:
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, sir!\n"
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print word,
                print "earned ",
                print getWordScore(word, n),
                print "points.",
                score += getWordScore(word, n)
                print "Total: %i points\n" % score
                # Update the hand 
                hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Total score: " + str(score) + " points."
    
#PLAYING A GAME  (10/10 points)

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    while True:
        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif choice == "r":
            try:
                playHand(hand, wordList, HAND_SIZE)
            except NameError:
                print "You have not played a hand yet. Please play a new hand first!"
        elif choice == "e":
            break
        else:
            print "Invalid command."
            
#COMPUTER CHOOSES A WORD  (15/15 points)

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    topScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    topWord = None
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(i, hand, wordList) == True:
            # Find out how much making that word is worth
            wordScore = getWordScore(i, n)
            # If the score for that word is higher than your best score
            if wordScore > topScore:
                # Update your best score, and best word accordingly
                topScore = wordScore
                topWord = i

    # return the best word you found.
    return topWord

COMPUTER PLAYS A HAND  (10/10 points)

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    topScore = 0
   
    topWord = None
   
    for i in wordList:
       
        if compValidWord(i, hand) == True:
            
            wordScore = getWordScore(i, n)
           
            if wordScore > topScore:
               
                topScore = wordScore
                topWord = i

    
    return topWord

def compValidWord(word, hand):
    amt = getFrequencyDict(word)
    for i in word:
        if amt.get(i, 0) > hand.get(i, 0):
            return False        
    return True
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    compScore = 0
    
    while compChooseWord(hand, wordList, n) != None:
        
        print "Current Hand: ",
        displayHand(hand)
        compChoice = compChooseWord(hand, wordList, n)
        print "\"" + compChoice + "\"",
        print "earned ",
        print getWordScore(compChoice, n),
        print "points.",
        compScore += getWordScore(compChoice, n)
        print "Total: %i points\n" % compScore
        hand = updateHand(hand, compChoice)
        n = calculateHandlen(hand)
    
    if n != 0:
         print "Current Hand: ",
         displayHand(hand)
         
    print "Total score: " + str(compScore) + " points."
    
YOU AND YOUR COMPUTER  (15/15 points)

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)"""
    
    while True:
        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice == "n":
            while True:
                who = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if who == "u":
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif who == "c":
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print "Invalid command."
        elif choice == "r":
            try:
                hand == 0
                while True:
                    who = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if who == "u":                    
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif who == "c":                    
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print "Invalid command."
            except NameError:
                print "You have not played a hand yet. Please play a new hand first!"
        elif choice == "e":
            break
        else:
            print "Invalid command."
#PART I: DATA STRUCTURE DESIGN  (5/5 points)

class NewsStory:
    
    def __init__(self, GUID, title, subject, summary, linkToMore):
        
        self.GUID = GUID
        self.title = title
        self.subject = subject
        self.summary = summary
        self.linkToMore = linkToMore

    def getGuid(self):
        return self.GUID
        
    def getTitle(self):
        return self.title
    
    def getSubject(self):
        return self.subject
    
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.linkToMore
        
#PART II: WORD TRIGGERS  (20/20 points)

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        searchHere = text.lower()
        searchFor = self.word.lower()
        
        import string
        to_be_removed = string.punctuation
        
        for character in to_be_removed:
            searchHere = searchHere.replace(character, " ")
        
        searchHere = searchHere.replace("  ", " ")
        searchHere = searchHere.split()
        
        for i in searchHere:
            if i == searchFor:
                return True
        return False
                
class TitleTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
        
class SummaryTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
        
#PART II: COMPOSITE TRIGGERS  (15/15 points)

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        searchHere = text.lower()
        searchFor = self.word.lower()
        
        import string
        to_be_removed = string.punctuation
        
        for character in to_be_removed:
            searchHere = searchHere.replace(character, " ")
        
        searchHere = searchHere.replace("  ", " ")
        searchHere = searchHere.split()
        
        for i in searchHere:
            if i == searchFor:
                return True
        return False
                
class TitleTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class NotTrigger(Trigger):

    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)
        
class AndTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) and self.trigger2.evaluate(story))

class OrTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) or self.trigger2.evaluate(story))
        
#PART II: PHRASE TRIGGERS  (5/5 points)

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        searchHere = text.lower()
        searchFor = self.word.lower()
        
        import string
        to_be_removed = string.punctuation
        
        for character in to_be_removed:
            searchHere = searchHere.replace(character, " ")
        
        searchHere = searchHere.replace("  ", " ")
        searchHere = searchHere.split()
        
        for i in searchHere:
            if i == searchFor:
                return True
        return False
                
class TitleTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
        
class SummaryTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
        
class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
        self.phrase = phrase
        
    def isPhraseIn(self, text):
        return self.phrase in text
        
    def evaluate(self, story):
        return (self.isPhraseIn(story.getTitle()) or self.isPhraseIn(story.getSubject()) or
                    self.isPhraseIn(story.getSummary()))
                    
#PART III: FILTERING  (10/10 points)

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        searchHere = text.lower()
        searchFor = self.word.lower()
        
        import string
        to_be_removed = string.punctuation
        
        for character in to_be_removed:
            searchHere = searchHere.replace(character, " ")
        
        searchHere = searchHere.replace("  ", " ")
        searchHere = searchHere.split()
        
        for i in searchHere:
            if i == searchFor:
                return True
        return False
                
class TitleTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
        
class SummaryTrigger(WordTrigger):
    
    def __init__(self, word):
        WordTrigger.__init__(self, word)
    
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
        self.phrase = phrase
        
    def isPhraseIn(self, text):
        return self.phrase in text
        
    def evaluate(self, story):
        return (self.isPhraseIn(story.getTitle()) or self.isPhraseIn(story.getSubject()) or
                    self.isPhraseIn(story.getSummary()))

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    storyList = []
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i):
                storyList.append(i)
                break
    
    return storyList

#PART IV: USER-SPECIFIED TRIGGERS  (10/10 points)

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
    
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
        
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
       
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
       
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
          
    elif triggerType == "PHRASE":
        argument = " ".join(params)
        triggerMap[name] = PhraseTrigger(argument)
    return triggerMap[name]
#PROBLEM 4  (10/10 points)

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess *= 2
        elif sign == 1:
            guess -= 1
        else:
            foundNumber = True
    return guess

#PROBLEM 5-1  (10/10 points)

class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        self.grade = grade
        self.course = course
        
        for i in self.myCourses:
            if i.courseName == self.course:
                i.setGrade(self.grade)
        pass
        
    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        self.course = course
        
        for i in self.myCourses:
            if i.courseName == self.course:
                return i.getGrade()
        return -1
        pass

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        self.pset = pset
        self.score = score
        self.course = course
        
        for i in self.myCourses:
            if i.courseName == self.course:
                i.setPset(self.pset, self.score)
        pass

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        self.pset = pset
        self.course = course
        
        for i in self.myCourses:
            if i.courseName == self.course:
                return i.getPset(self.pset)
        return -1
        pass
        
#PROBLEM 6-7  (20/20 points)

class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        
        a_ancestors = []
        b_ancestors = []
        
        i = self.names_to_nodes[a]
        while i != self.root:
            i = i.get_parent()
            a_ancestors.append(i)
        
        i = self.names_to_nodes[b]
        while i != self.root:
            i = i.get_parent()
            b_ancestors.append(i)

        if self.names_to_nodes[a] == self.names_to_nodes[b]:
            return (-1, 0)
        elif (self.names_to_nodes[a] in b_ancestors) or (self.names_to_nodes[b] in a_ancestors):
            if (self.names_to_nodes[a] == self.names_to_nodes["a"]) or (self.names_to_nodes[b] == self.names_to_nodes["a"]):
                removed = max(len(a_ancestors), len(b_ancestors))
                return (-1, removed)
            else:
                removed = abs(len(a_ancestors) - len(b_ancestors))
                return (-1, removed)
        else:
            for i in a_ancestors:
                if i in b_ancestors:
                    common_ancestor = i
                    break
            a_length = len(a_ancestors[:a_ancestors.index(common_ancestor)])
            b_length = len(b_ancestors[:b_ancestors.index(common_ancestor)])
            removed = abs(a_length - b_length)
            
            if a_length == b_length:
                return (a_length, 0)
            else:
                cousinality = min(a_length, b_length)
                return (cousinality, removed)
                
#PROBLEM 7-1  (10/10 points) -- Doubly-Linked List

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    
    """atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    """
    
    endpt = False
    if newFrob.myName() == atMe.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            temp = atMe.getBefore()
            newFrob.setAfter(atMe)
            newFrob.setBefore(temp)
            temp.setAfter(newFrob)
            atMe.setBefore(newFrob)
            
    
    elif newFrob.myName() < atMe.myName():
        i = atMe
        while newFrob.myName() < i.myName():
            temp = i
            i = i.getBefore()
            if i is None:
                endpt = True
                break
        if endpt == True:
            newFrob.setAfter(temp)
            temp.setBefore(newFrob) 
        else:
            newFrob.setBefore(i)
            newFrob.setAfter(temp)
            temp.setBefore(newFrob)
            i.setAfter(newFrob)
    
    else:
        i = atMe
        while newFrob.myName() > i.myName():
            temp = i
            i = i.getAfter()
            if i is None:
                endpt = True
                break
        if endpt == True:
            newFrob.setBefore(temp)
            temp.setAfter(newFrob)
        else:
            newFrob.setAfter(i)
            newFrob.setBefore(temp)
            i.setBefore(newFrob)
            temp.setAfter(newFrob)
            
#PROBLEM 7-2  (10/10 points)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    temp = start
    i = start.getBefore()
    if i is None:
        return temp
    else:
        return findFront(i)
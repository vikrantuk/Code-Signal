'''
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
'''

def areFollowingPatterns(strings, patterns):
    hash=dict()
    hash1=dict()
    
    for i in range(len(strings)):
        if(strings[i] not in hash):
            hash[strings[i]]=set()
        hash[strings[i]].add(i)

    for i in range(len(patterns)):
        if(patterns[i] not in hash1):
            hash1[patterns[i]]=set()
        hash1[patterns[i]].add(i)
    li=[]
    for el in hash:
        li.append(hash[el])
    ind=0
    for el in hash1:
        if(hash1[el]!=li[ind]):
            return(False)
        ind+=1
    return(True)

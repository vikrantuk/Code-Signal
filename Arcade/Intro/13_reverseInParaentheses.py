'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''

def reverseInParentheses(inputString):
    if(len(inputString)<3):
        if('(' in inputString):
            return ""
        return(inputString)
    if('(' not in inputString):
        return(inputString)

    count=0
    li=[]
    for el in inputString:
        if(el=='('):
            count+=1
        li.append(el)
    
    for _ in range(count):
        st=0
        end=0
        for i in range(len(li)):
            if(li[i]=='('):
                st=i
            elif(li[i]==')'):
                end=i
                li=invert(li,st,end)
                break
    inputString = ""
    for el in li:
        inputString+=el
    return(inputString)

def invert(l,s,e):
    l.pop(e)
    l.pop(s)
    for i in range(0,int((e-1-s)/2)):
        l[i+s],l[e-2-i] = l[e-2-i], l[i+s]
    return(l)

'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''

def checkPalindrome(inputString):
    flag = True
    for i in range(int(len(inputString)/2)+1):
        if(inputString[i]!=inputString[-i-1]):
            return False
    return True

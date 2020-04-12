'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
'''

def evenDigitsOnly(n):
    n=str(n)
    for el in n:
        if(int(el)%2==1):
            return False
    return True

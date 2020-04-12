'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
'''

def variableName(name):
    if('0'<=name[0]<='9'):
        return False
    for el in name:
        if('0'<=el<='9' or 'a'<=el<='z' or 'A'<=el<='Z' or el=='_'):
            pass
        else:
            return False
    return True

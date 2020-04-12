'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
'''

from itertools import permutations

def oneLetterDiff(first_string, second_string):
    letter_pairs = zip(first_string, second_string)
    misses = (a != b for (a,b) in letter_pairs)
    return True if sum(misses) == 1 else False

def stringsRearrangement(inputArray):
    arrangements = permutations(inputArray)
    for current_arrangement in arrangements:
        string_comparisons = zip(current_arrangement, current_arrangement[1:])
        comparison_results = (oneLetterDiff(a, b) for (a, b) in string_comparisons)
        if all(comparison_results):
            return True
    return False

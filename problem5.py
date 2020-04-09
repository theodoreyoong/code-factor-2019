"""
Key idea: extract all the maximum length sub-strings that contain only vowels.
For all these substrings we count the number of subsubstrings that contain the each vowel at least once.
We use a two-pointer technique.
"""

def isVowel(c):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return c in vowels

"""
Helper function to count number of subsubstrings from a pure vowel substring.
If substring at current iteration has all vowels at once, not only does it satisfy the condition...
...but ANY substring with length longer than that satisfies the condition as well!
Thus, we just add l-1 subsubstrings, where l is the length of the substring.
Then, we just update the start pointer and count for the next iteration.
Note: use dict.fromkeys(vowels, 0) instead of dict.fromkeys(substring, 0).
If not, all(value > 0 for value in vowelMap.values()) will give the wrong answer.
E.g. suppose the last substring is just 'a'.
Then, all values is just the value of 'a' which is indeed > 0 and will return 1.
"""

def countFromPure(substring):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowelMap = dict.fromkeys(vowels, 0)
    l = len(substring)
    while(all(value > 0 for value in vowelMap.values())):
        c += l-i
        vowelMap[substring[start]] -= 1
        start += 1
    return(c)

def vowelSubstring(s):
    l = len(s)
    n = 0
    helper = []
    for i in range(l):
        if isVowel(s[i]):
            helper.append(s[i])
        else:
    if len(set(helper)) == 5:
        n += countFromPure(helper)
    return(n)
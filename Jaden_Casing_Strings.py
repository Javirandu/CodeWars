"""
Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, 
but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""

def to_jaden_case(string):
    """instead of all the code we could use:
    import string

    def toJadenCase(NonJadenStrings):
        return string.capwords(NonJadenStrings)
    """
    jaden_cased = string.split(" ")  #string turned into list
    jaden_cased = [word.capitalize() for word in jaden_cased] #capitalizing every word
    space= " "
    return space.join(jaden_cased) #joining every word with an space



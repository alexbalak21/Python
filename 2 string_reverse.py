s = "I love coding in python"


def reverse_string(s):
    r = ""
    for i in range(len(s)-1, -1, -1):
        r += s[i]
    return r

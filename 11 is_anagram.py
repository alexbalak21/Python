#  Anagram check Write a function is_anagram(s1, s2) that returns True if two strings are anagrams of each other.


def is_anagram(s1:str, s2:str)->bool:
    return sorted(s1.lower()) == sorted(s2.lower())



print(is_anagram("Listen", "Silent"))
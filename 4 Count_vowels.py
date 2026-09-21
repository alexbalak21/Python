
def count_vowels(s:str):
    vowels = "aeiouy"
    count = 0
    for l in s:
        if l.lower() in vowels:
            count+=1
    return count

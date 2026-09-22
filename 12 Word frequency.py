# Word frequency Write a function word_frequency(text) that returns a dictionary mapping each word to its number of occurrences.
test_text = """
The Python programming language is an amazing language for data science, web development, 
and automation. Python is designed to be highly readable, using English keywords frequently 
where other languages use punctuation. 

Learning Python opens up many doors. Data science relies heavily on Python; web development 
with frameworks like Django and Flask relies on Python too. Many developers say: "Python is 
my favorite language!" Is it your favorite language too?

Let's test how well the word_frequency function counts words. It should count 'Python', 
'python', and 'Python;' as the same word if we clean the punctuation properly. 
Spaces    between    words    should    also    not    cause    empty    strings!
"""


def word_frequency(text :str) -> dict:
    words = text.lower().split()
    unique_words = set(words)
    word_count = dict() 
    for word in unique_words:
        word_count[word] = words.count(word)
    return word_count


print(word_frequency(test_text))
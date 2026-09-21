s1 = "radar"
s2 = "level"
s3 = "kayak"


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome(s1), is_palindrome(s2), is_palindrome(s3), is_palindrome("hello"))
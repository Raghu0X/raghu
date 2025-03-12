def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]
result = is_palindrome("A man a plan a canal Panama")
print(result)

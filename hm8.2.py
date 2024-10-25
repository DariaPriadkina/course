import string

def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char not in string.punctuation and char != ' ')
    text_2 = text[::-1]
    if text == text_2: return True
    else: return False

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))
def is_palindrome(word: str) -> bool:
    s: str = ''
    for i in range(len(word)):
        s += word[-i - 1]
    if word == str(s):
        return True
    return False


print(is_palindrome('elbek'))
x = input()
x = x.strip("\"")


def is_plindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False


def longestPalindrome(s):
    if not s: return ""
    length = len(x)
    for i in range(length, 0, -1):
        j = 0
        while i + j <= length:
            sub_str = x[j:j+i]
            if is_plindrome(sub_str):
                return "\""+sub_str+"\""
            j += 1

x = longestPalindrome(x)
print(x)
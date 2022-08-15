s = "abc"
t = "hbgdc"

# s = "axc"
# t = "ahbgdc"

# def is_subsequence(s, t):
#     current_pos = 0
#     for letter in s:
#         current_pos = t.find(letter, current_pos) + 1
#         if current_pos == 0:
#             return False
#     return True

def is_subsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)

print(is_subsequence(s,t))

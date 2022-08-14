from collections import defaultdict
s = 'abca'
# s = "aab"
# s = "pwwkew"
# s = 'dvdf'

found = defaultdict(int)
max_len = 0
start = 0

for i, char in enumerate(s):
    if char in found:
        start = max(start, found[char] + 1)

    found[char] = i
    max_len = max(max_len, i - start + 1)

print(max_len, found)

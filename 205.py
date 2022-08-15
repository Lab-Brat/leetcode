from collections import defaultdict

# s = "egg"
# t = "add"

# s = "foo"
# t = "bar"

# s = "paper"
# t = "title"

s = ''
t = ''

def get_struct(s):
    dd = defaultdict(int)
    struct = []
    for i, letter in enumerate(s):
        if letter not in dd:
            dd[letter] = i
            struct.append(i)
        else:
            struct.append(dd[letter])
    return struct
    

print(get_struct(s) == get_struct(t))
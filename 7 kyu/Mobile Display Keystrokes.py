def mobile_keyboard(s):
    mob = {'a': 2, 'b': 3, 'c': 4, 'd': 2, 'e': 3, 'f': 4, 'g': 2, 'h': 3, 'i': 4, 'j': 2, 'k': 3, 'l': 4, 'm': 2,
        'n': 3, 'o': 4, 'p': 2, 'q': 3, 'r': 4, 's': 5, 't': 2, 'u': 3, 'v': 4, 'w': 2, 'x': 3, 'y': 4, 'z': 5}
    c = 0
    for i in range(len(s)):
        if s[i] in mob:
            c += mob[s[i]]
        else:
            c += 1
    return c
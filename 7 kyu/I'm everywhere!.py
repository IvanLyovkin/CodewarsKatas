def i(word):
    if not word or word[0].islower() or word[0] == 'I':
        return "Invalid word"
    vowels = ['a', 'e', 'u', 'i', 'o']
    vow = 0
    for i in range(0, len(word)):
        if word[i].lower() in vowels:
            vow += 1
    con = len(word) - vow
    return 'Invalid word' if con <= vow else 'i' + word
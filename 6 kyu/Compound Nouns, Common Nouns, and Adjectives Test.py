def part(word):
    if word in adjectives:
        return "adjective"
    if word in nouns:
        return "common"
    for set in adjectives:
        if len(word) > len(set):
            if word[len(set):] in nouns:
                 return "compound"
    for set in nouns:
        if len(word) > len(set):
            if word[len(set):] in nouns:
                return "compound"
    return "neither"
# https://www.codewars.com//kata/51e056fe544cf36c410000fb

import re
from collections import Counter

def top_3_words(text):
    c = Counter(re.findall(r"'*[a-z][a-z|']*",  text.lower()))
    return [w for w,_ in c.most_common(3)]
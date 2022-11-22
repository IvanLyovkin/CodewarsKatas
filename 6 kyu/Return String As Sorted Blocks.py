import string

def blocks(s):
    n = ""
    while s:
        for i in string.ascii_letters + string.digits:
            if i in s:    
                s = s.replace(i,"",1)
                n += i
        if s: 
            n += "-"
    return n
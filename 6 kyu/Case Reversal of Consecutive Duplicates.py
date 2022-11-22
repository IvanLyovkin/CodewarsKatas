def reverse(str):
    str += " "
    str = list(str)
    result = ""
    for i in range(0,len(str)-1):
        if str[i]!=str[i+1] and str[i]!=str[i-1]:
            result += str[i]
        else:
            if str[i]==str[i].lower():
                result += str[i].upper()
            else:
                result += str[i].lower()
    return result
def disarium_number(number):
    n = str(number)
    c = 0
    for i in range(len(n)):
        c += pow(int(n[i]), i + 1)
    return 'Disarium !!' if c == number else 'Not !!'
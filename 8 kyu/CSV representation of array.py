def to_csv_text(array):
    for i in range(len(array)):
        array[i] = ",".join(map(str, array[i]))
    return "\n".join(array)   
def csv_columns(csv, indices):
    result = []
    lines = csv.splitlines()
    for line in lines:
        l = line.split(',')
        result.append(','.join(l[i] for i in set(indices) if i < len(l)))
    return '\n'.join(result).strip()
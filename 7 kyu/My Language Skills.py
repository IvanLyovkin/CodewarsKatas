def my_languages(results):
    c = []
    results = dict(sorted(results.items(), key=lambda item: -item[1]))
    for item in results:
        if results[item] >= 60:
            c.append(item)
    return c
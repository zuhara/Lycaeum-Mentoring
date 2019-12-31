def mode(s):
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    m = max(d.values())
    for j,k in d.items():
        if k == m:
            return j


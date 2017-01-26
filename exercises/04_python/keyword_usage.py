def keyword_usage(s, l):
    splitStr = s.split()
    r = []
    for i in l:
        r.append(i in splitStr)
    return tuple(r)
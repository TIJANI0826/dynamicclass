def read_text():
    with open('subject.txt', 'rt') as f:
        l = []
        for n in f.readlines():
            l.append(n)
    return l

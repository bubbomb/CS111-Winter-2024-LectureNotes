def f(s=None):
    if s is None:
        s = []

    s.append(3)
    return len(s)

print(f())
print(f())
print(f())
print(f())
class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


cars  = Link('cars1')
print(cars)
print(cars.rest)

cars2 = Link('cars2')


cars_franchise = Link('cars1', Link('cars2', Link('cars3', Link('planes', Link('Turbo')))))
cars2.rest = cars_franchise
print(cars_franchise)

cars.rest = cars2

print(cars)

print(cars_franchise.rest.rest.rest.rest.rest)



def range_link(start, end):
    """Return a Link containing consecutive integers
    from start to end, not including end.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))


some_links = range_link(3,6)

# print(some_links)


s = Link("A", Link("B", Link("C")))
t = s.rest
t.rest = s

print(t.rest.rest.rest.rest)
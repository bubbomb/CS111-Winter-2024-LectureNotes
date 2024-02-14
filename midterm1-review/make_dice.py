from random import randint

def make_die_maker(n):
    
    def make_die():
        return lambda : randint(1,n)

    return make_die


make_d6 = make_die_maker(6)

d6 = make_d6()
d6_again = make_d6()

print(make_d6)
print(d6())
print(d6_again())
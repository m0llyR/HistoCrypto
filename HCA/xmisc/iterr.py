
def count(start=0):
    num = start
    while True:
        yield num
        num += 1

def rfe(keyword, start=0):
    """ Repeat for ever - looping over keyword """
    n = start
    while True:
        if n > len(keyword)-1: n = 0
        yield keyword[n]
        n += 1

keyw = rfe("abc")

for x in keyw:
    print(x)
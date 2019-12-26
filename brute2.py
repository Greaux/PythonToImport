from zipfile import ZipFile
import itertools

def cartesian_product(ls):
    return list(itertools.product(*ls)) # unpack list into arguments

# another way:
#def cartesian_product(ls):
#    if len(ls) == 0:
#        return [[]]
#    return [[e] + p for e in ls[0] for p in cartesian_product(ls[1:])]

with ZipFile('zzz.zip') as h:
    for i in range(1, 5): # [1, 2, 3, 4]
        symbols = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        passwds = map(lambda x: ''.join(x), cartesian_product([symbols] * i))
        found = False
        for passwd in passwds:
            try:
                h.extractall(pwd=passwd)
                print 'Password: ' + passwd
                found = True
                break
            except:
                pass
        if found:
            break

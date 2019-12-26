#!/usr/bin/python

import hashlib
import random

mval = 10 ** 6
kval = 50 # >= 1

def apply_reduction(h):
    return '{:06d}'.format(sum([int(h[i * 8:(i + 1) * 8], 16) for i in range(4)]) % mval)

def apply_encryption(p):
    return hashlib.md5(p).hexdigest()

def apply_chain(p, k=kval):
#    p = apply_reduction(h)
    for i in range(k):
        p = apply_reduction(apply_encryption(p))
    return p

def restore_passwd(p, h, k=kval):
    for i in range(k):
        hval = apply_encryption(p)
        if hval == h:
            return p
        p = apply_reduction(hval)
    return None

passwd = '{:06d}'.format(random.randint(0, mval - 1))
print 'passwd: ' + passwd
hashval = hashlib.md5(passwd).hexdigest()
print 'hashval: ' + hashval

#chainval = apply_chain(hashval)
#print chainval

plist = map(lambda x: '{:06d}'.format(x), random.sample(range(0, mval), 200000))
pdict = {p: apply_chain(p) for p in plist}

p = None
for k in range(kval):
    p = apply_reduction(hashval) if k == 0 else apply_chain(p, k=1)
    found = None
    for f in [v[0] for v in pdict.items() if v[1] == p]:
        found = restore_passwd(f, hashval)
        if found is not None:
            print 'Password was found: ' + found
            break
    if found is not None:
        break

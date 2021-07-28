from itertools import *
from gmpy2 import *
def x(a,b):
    return bytes(islice((x^y for x,y in zip(cycle(a), cycle(b))), max(*map(len, [a, b]))))
def t(x):
    return sum((((x & 28) >> 4) & 1) << i for i, x in enumerate(x))
T = t(x(b"jctf{not_the_flag}", b"*-*")) | 1
print(T)
l = 420
flag = 2535320453775772016257932121117911974157173123778528757795027065121941155726429313911545470529920091870489045401698656195217643
binf = bin(flag)[2:]
for i in range(421337):
	if binf[0] == "1":
		# (popcount(flag & T) & 1) == 1
		tmp_flag = binf[1:]
		if (popcount(int(tmp_flag+"1",2) & T) & 1) == 1:
			binf = binf[1:]+"1"
		else:
			assert (popcount(int(tmp_flag+"0",2) & T) & 1) == 1
			binf = binf[1:]+"0"
	else:
		#assert flag.bit_length() == l-1
		# (popcount(flag & T) & 1) == 0
		tmp_flag = binf[1:]
		if (popcount(int(tmp_flag+"1",2) & T) & 1) == 0:
			binf = binf[1:]+"1"
		else:
			assert (popcount(int(tmp_flag+"0",2) & T) & 1) == 0
			binf = binf[1:]+"0"
		#assert flag.bit_length() == l-1
	#print(i, flag.bit_length())
	assert len(binf) == l
from Crypto.Util.number import *
print(binf)
print(long_to_bytes(int(binf,2))[::-1])

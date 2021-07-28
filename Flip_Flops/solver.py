from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "chal.imaginaryctf.org", 42011
s, f = sock(HOST, PORT)
#print(read_until(f))
#print(read_until(f,"solution: "))
#sol = input("> ")
#s.send(sol.encode()+b"\n")
for _ in range(25-8+1): print(read_until(f))

print(read_until(f,"'gimmeflag'."))
for _ in range(2): print(read_until(f))
print(read_until(f,"> "))
s.send(b"1\n")
pt = "31"*48
print(read_until(f,"(in hex): "))
s.send(pt.encode()+b"\n")
enc = read_until(f).strip()
print("got mes:",enc)

print(read_until(f,"'gimmeflag'."))
for _ in range(2): print(read_until(f))
print(read_until(f,"> "))
s.send(b"2\n")

val = bytes_to_long(b"gimmeflag"+b"\x07"*7)
pt0 = int("31"*16,16)
ct1 = int(enc[:32],16)
key = pt0^ct1
ppt0 = val^key
ans0 = hex(ppt0)[2:]
while len(ans0) < 32: ans0 = "0"+ans0
ans0 += enc[32:64]
print(read_until(f,"(in hex): "))
s.send(ans0.encode()+b"\n")
while True: print(read_until(f))


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')


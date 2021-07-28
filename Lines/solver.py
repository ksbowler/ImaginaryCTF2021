from Crypto.Util.number import *

p = 82820875767540480278499859101602250644399117699549694231796720388646919033627
encrypt_flag = 26128737736971786465707543446495988011066430691718096828312365072463804029545
encrypt_msg = 15673067813634207159976639166112349879086089811595176161282638541391245739514
msg = bytes_to_long(b":roocursion:")
# s*msg mod p = encrypt_mes : s = enc * mes^-1
s = (inverse(msg,p)*encrypt_msg)%p
# s*flag mod p = encrypt_flag : flag = enc * s^-1
flag = (encrypt_flag*inverse(s,p))%p
print(long_to_bytes(flag))

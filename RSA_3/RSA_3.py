from Crypto.Util.number import getPrime, bytes_to_long


p = getPrime(256)
q = getPrime(256)

n = p * q
e1 = 0b101
e2 = 0b10001

flag = #hidden

m = bytes_to_long(flag)

ciphertext1 = pow(m, e1, n)
ciphertext2 = pow(m, e2, n)


print(f"n = {n}")
print(f"e1 = {e1}")
print(f"ciphertext1 = {ciphertext1}")
print(f"e2 = {e2}")
print(f"ciphertext2 = {ciphertext2}")


""" OUTPUT :
n = 8298232832557779165642568688802433012489581247231191888479510911015306473265728786076358309051720683403847251927146410008022750148812822375234802808658397
e1 = 5
ciphertext1 = 7611556122577415112210529426872991308187196876396054246914338018377600487553046800777125501339576995163885571672393185787648756786539304271560901275280928
e2 = 17
ciphertext2 = 4426515305111583405180029048732181557535316286857631111340077481869273384649493412824424568570078126498459735464049970809300130889395721864827529236783207
"""
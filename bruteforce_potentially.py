from Crypto.Util.number import inverse
import matplotlib as pl

#sidenotes: entered sequence must be lowercase
# lezem el mod ykoun prime ig


flag = "ksvtd"
guess = 'abcde'


modulus = 31
def calculate_polynomial(guess , number ,flag):
    if not guess:
        print(str(number) + 'final guess')
        return number
    else:
        print(number)
        number = ( number * ( - ord(guess[ -1 ]) + ord(flag [ -1 ])) + 1 ) % modulus
        return calculate_polynomial(guess[:-1] , number , flag[:-1])

print(calculate_polynomial (guess , 1,flag) )


outputs = []
print("---------------------")
outputs.append(calculate_polynomial ('baaaa' , 1 , flag))
print("---------------------")
outputs.append(calculate_polynomial ('abaaa' , 1 , flag))
print("---------------------")
outputs.append(calculate_polynomial ('aabaa' , 1 , flag))
print("---------------------")
outputs.append(calculate_polynomial ('aaaba' , 1 , flag))
print("---------------------")
outputs.append(calculate_polynomial ('aaaab' , 1 , flag))
print("---------------------")
P = calculate_polynomial('aaaab' , 1 , flag)
P_inverse = inverse(P,modulus)
print(f'outputs : {outputs}')
print(f'final_target : {P}')

isolated_variables = []
factors = []
for i in range(len(outputs)):
    isolated_variables.append( (outputs[i] - P) % modulus )
    iso = (isolated_variables[i] * P_inverse) % modulus
    orda = ord('a')
    factors.append(inverse(iso,modulus))
    print(f'iso : {factors[i]}   , i :  {i} , letter :  {ord(flag[i]) - orda}')

print(f'factors : {factors}')




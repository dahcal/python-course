from fractions import gcd
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import itertools

# source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def decryption(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

#n = 232805337824709187758567614345164369640905196906161190117399914999084869280501377034146427509821310414018646093699105528219624749717431457106237039734270204290594088884317268823351960048222904591377231999511261693392492917096983385403575193640490238594096249866899523020243255292818672149033458690078581352942476216908273781672014930971L
#e= 65537L

e=29815
n=100127

#secret_message = open("E:\Downloads\message.txt").read()
secret_message = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
## http://www.factordb.com was used to get factors 
#q = 99999989L
#p = 2328053634332991654214758107075035474662954181986571919696910316650983524413201455793624412396898467799017918828962126468030158980491802425160637165012790194312862263258021646615900728231309151357778969350799245521841936573582856948150016232906688005676643123099738771173697382034898745329196573112408855894398910552962898642639L

pq_list = primes(n)
p = pq_list[0]
q = pq_list[1]

phi = (p-1)*(q-1)
gcd, x, y = egcd(e, phi)

assert gcd == 1 # should be 1 = they have to be coprime
d = x % phi

private_key = (d,n)

plain = decryption(private_key, secret_message)

print(plain)


## "fancy" method from lib. Not working due to cipher not being in bytes/padded
#decryptor = PKCS1_OAEP.new(RSA.construct((n, e, d)))
#private_key = RSA.construct((n, e, d))
#plain = decryptor.decrypt(secret_message)
#print(plain)
#print(private_key)
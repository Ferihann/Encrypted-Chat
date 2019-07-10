# This class make encryption using RSA algorithm

import random
large_prime = []  # Is array for storing the prime numbers then select into it randomly


class Rsa:

    def generate_prime(self, lower, upper):  # this function simply generate prime numbers

        for num in range(lower, upper+1):
            if num > 1:
                for i in range(2, num):
                    if(num % i) == 0:
                        break
                else:
                    large_prime.append(num)

    def generate_public_and_private_key(self):  # generates public and private keys
        q = random.choice(large_prime)
        p = random.choice(large_prime)

        n = p * q
        e = 2
        z = (q - 1) * (p - 1)

        while e < z:

            #  e is co-prime with toitient number , its gcd should equals 1
            if self.gcd(e, z) == 1:
                break
            else:
                e += 1
        w = 1
        while((e*w) % z) != 1:  # de = 1 modz
            w += 1

        d = w
        # print("n is : ", n , " e is : ", e)
        return [(e, n), (d, n)]  # public key (e,n) private key (d,n)

    def gcd(self, a, h):  # Calculation of great common divisor
        temp = 0
        while 1:
            temp = a % h
            if temp == 0:
                return h
            a = h
            h = temp

    def encrypt(self, public_key, plaintext):  # Encrypt the plain text
        ciphertext = ""
        key, n = public_key
        for i in plaintext:
            c = (ord(i) ** key) % n
            ciphertext += chr(c)
        return ciphertext

    def decrypt(self, private_key, ciphertext):  # Decrypt the plain text
        plaintext=""
        key, n = private_key
        for i in ciphertext:
            m = (ord(i) ** key) % n
            plaintext += (chr(m))
        return plaintext

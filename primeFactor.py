from math import sqrt

num = 600851475143

def primeList(N):
  halfN = int(sqrt(N))
  primeCandidate = [1] * halfN # index start from number 2
  prime = []

  for i in xrange(2, halfN):
    if primeCandidate[i-2] == False:
      continue
    prime.append(i)
    for j in xrange(2, halfN):
      if i*j-2 < halfN:
        primeCandidate[i*j-2] = False
      else: break
  return prime
  
def primeFactor(N):
  for i in reversed(primeList(N)):
    if N % i == 0:
      return i

print(primeFactor(num))



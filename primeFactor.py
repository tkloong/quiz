from math import sqrt

N = 600851475143

def primeList(N):
  # index start from number 2
  halfN = int(sqrt(N))
  primeCandidate = [1] * halfN
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
  for i in primeList(N):
    if N % i == 0:
      return N/i

print(primeFactor(N))



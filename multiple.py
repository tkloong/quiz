def calc(n):
  aSet = set()

  for i in xrange(3, n, 3):
    aSet.add(i)
  for i in xrange(5, n, 5):
    aSet.add(i)
  return aSet

print sum(calc(1000))


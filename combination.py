table = dict()

def Combination(n, r):
  global table
  if r == 1: 
    return n
  if r == 0 or r == n:
    return 1
  if table.get((n, r)) is None: 
    table[(n, r)] = Combination(n-1, r) + Combination(n-1, r-1)
  else:  # Solved
    return table[(n, r)]
  return table[(n, r)]

print Combination(990, 33)


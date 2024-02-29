def convert(s, numR):
  if numR == 1:
    return s
  rows = ["" for _ in range(numR)]
  currR = 0
  dir = -1

  for char in s:
    rows[currR] += char
    if currR == 0 or currR == numR - 1:
      dir *= -1
    currR += dir

return ''.join(rows)
    

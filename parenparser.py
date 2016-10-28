def parse_paren(expression):
  if expression.count('(') != expression.count(')'):
    raise Error('parethises mismatch')
  if expression.count('(') == 0:
    return [expression]
  ret = []
  rem = expression # remaining expression to parse

  while rem.count('(')>0:
    start = rem.find('(')
    if start > 0:
      ret.append(rem[0:start])
      rem = rem[start:]
    if start == -1:
      ret.append(rem)
    left, right = find_olp(rem)
    inParen = rem[left+1: right]
    rem = rem[right+1:]
    ret.append(parse_paren(inParen))
  ret.append(rem)
  return ret
  
   
def find_olp(expression):
  # find the index of the parethesis matching the leftmost parethesis.
  # returns the indices of the pair
  left = expression.find('(')
  pos = left
  levels = 1
  while levels > 0:
    nl = expression.find('(', pos+1)
    nr = expression.find(')', pos+1)
    if nr == -1:
      raise Exception('right match not found')
    if nl == -1:
      nl = len(expression) + 1
    if nl<nr:
      levels += 1
      pos = nl
    elif nr<nl:
      levels -= 1
      pos = nr
    else:
      raise Exception('positionEqualParen')
  return left, nr


def substring_copy(str, n):
  flen = 3
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 3))
print(substring_copy('pyurds', 5));


def reemplazo(string):
  s = ""
  for i in string:
    if i.isupper():
      s = s + "$"
    else:
      s = s + i

  return s
print(reemplazo("Mira Que Bien"))
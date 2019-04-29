import operator
Buscar="house"
Buscar=Buscar.lower()
released = {
    0 : 0}
for linea in LineFiltered:
  Id=""
  contador=0
  frecuencia=0
  coleccionPalabras=tokenizer.tokenize(linea)
  for palabra in coleccionPalabras:
    contador+=1
    if palabra==Buscar:
      frecuencia+=1
    if contador==2:
      Id=palabra
      
      
  released[Id]=frecuencia
sorted_x = sorted(released.items(), key=operator.itemgetter(1))
sorted_x.reverse()
print (sorted_x)    

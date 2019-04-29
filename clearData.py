import io
import nltk 
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer 

lineas=sc.textFile('dbfs:///FileStore/tables/TextoPrueba.txt')
lineasCollect=lineas.flatMap(lambda line: line.split('\n')).collect()
wordsFiltered=[]
global contadorComas
comilla=False
lineanew=""
stopWords=set(stopwords.words('english'))

contador=0
tokenizer = RegexpTokenizer(r'\w+') 
LineFiltered=[]
for linea in lineasCollect:
  contadorComas=0
  linea=linea.lower()
  indice=""
  contenido=""
  contenidoLimpio=""
  limpio=[]
  wordsFiltered=[]
  
  for x in linea:
     
      if contadorComas<9:
        indice=indice+x
        
      else:  
        contenido=contenido+x
        
        
    
      if x == ',':
        contadorComas+=1
        
    
      if x=='"' and comilla==True:
        comilla=False
      else:
        if x=='"':
          comilla=True
        
      if comilla==True :
        if x==',':
          contadorComas-=1
 
     
  limpio = tokenizer.tokenize(contenido)
  
  for word in limpio:
  
    if word not in stopWords:
       wordsFiltered.append(word)
        
  contenidoLimpio=" ".join(wordsFiltered)
  contenidoLimpio=indice+contenidoLimpio
  LineFiltered.append(contenidoLimpio)
print(LineFiltered)   
  

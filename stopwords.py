# importar la libreria nltk
import nltk

# Desde nltk descargar el paquete de stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('spanish')

# Imprimir las stopwords
print(lista_stopwords)


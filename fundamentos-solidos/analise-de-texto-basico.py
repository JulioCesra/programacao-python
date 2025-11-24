"""
DESAFIO: Implemente um módulo de análise de texto com as seguintes funções:

1. contar_palavras(texto: str) -> int
   - Retorna o número total de palavras

2. palavra_mais_frequente(texto: str) -> tuple[str, int]
   - Retorna (palavra, frequência) da palavra mais comum

3. inverter_ordem_palavras(texto: str) -> str
   - Retorna texto com palavras em ordem inversa

4. eh_palindromo(frase: str) -> bool
   - Verifica se a frase é palíndromo (ignorar espaços, pontuação e case)

REGRAS:
- Considere palavra como sequência de caracteres alfanuméricos
- Ignore case nas análises (case-insensitive)
- Trate pontuação adequadamente
- Documente suas funções
- Escreva código limpo e legível

EXEMPLO:
texto = "Python é legal. Python é poderoso."
contar_palavras(texto) -> 6
palavra_mais_frequente(texto) -> ('python', 2)
inverter_ordem_palavras(texto) -> "poderoso. é legal. é Python"
eh_palindromo("A base do teto desaba") -> True
"""

# Sua implementação abaixo:

def limpar_pontuacao(texto:str) -> str:
   """
   Remove pontuações, deixando somente letras, números e espaços.
   
   Args:
       texto (str): Texto que vai ser retirada as pontuações.
       
   Returns:
       str: Texto com as pontuações removidas.
       
   """
   pontuacao = '!@#$%^&*()_+-=[]{}|;:",.<>?/`~'
   for char in pontuacao:
      texto = texto.replace(char, " ")
   return texto

def contar_palavras(texto:str) -> int:
   """
   Retorna a quantidade de palavras que existe em um texto.
   
   Args:
       texto (str): Texto que vai ser analisado.

   Returns:
       int: Quantidade de palavras que o texto possui.
   """
   if not texto or not texto.split():
      return 0
   
   return len(texto.split())

from collections import Counter
from typing import Tuple

def palavra_mais_frequente(texto:str) -> Tuple[str, int]:
   """
   Retorna qual a palavra mais frequente no texto e quantas vezes ela apareceu.

   Args:
      texto (str): Texto que vai ser analisado.

   Returns:
      Tuple[str, int]: Palavra mais frequente, vezes que apareceu.
   """    
   if not texto:
      return ("",0)
   
   texto = limpar_pontuacao(texto)
   palavras = [palavra.lower() for palavra in texto.split() if palavra]

   if not palavras:
      return ("",0)
   
   return Counter(palavras).most_common()[0]

def inverter_ordem_palavras(texto:str) -> str:
   """
   Retorna o texto de origem com as palavras invertidas.
   Args:
       texto (str): Texto que vai ter as palavras invertidas.

   Returns:
       str: Texto com as palavras invertidas.
   """
   if not texto:
      return ""
   
   return ' '.join(reversed(texto.split()))

def eh_palindromo(frase: str) -> bool:
   """
   Retorna True se a frase for um palíndromo ou False se não for. 
   Args:
       frase (str): Texto que vai ser analisado.

   Returns:
       bool: True se for palíndromo ou False se não for.
   """
   if not frase:
      return False

   frase = limpar_pontuacao(frase).replace(' ','').lower()
   
   return frase == frase[::-1] 

if __name__ == '__main__':
   texto = 'Python é legal. Python é poderoso.'

   print("Quantidade de palavras: ",contar_palavras(texto))
   print("Palavra mais frequente: ",palavra_mais_frequente(texto))
   print("Texto invertido: ",inverter_ordem_palavras(texto))
   print("É um palíndromo?: ",eh_palindromo(texto))

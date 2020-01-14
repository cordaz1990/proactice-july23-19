#string slicing

>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'

greeting = 'Hello, World!'
new_greeting = 'J' + greeting[1:]
new_greeting
'Jello, world!"

def find(word, letter)
    index = 0 
    while index < len(word):
      if word[index] == letter:
          return index
      index = index + 1
    return -1
      

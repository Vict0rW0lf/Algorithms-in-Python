#O(n) where N is the size of the String
def valid_parenthesis(txt):
  stack = []
  types = {"}": "{", ")": "(", "]": "["}
  
  for letter in txt:
   if letter in types.values():
     stack.append(letter)
   elif letter in types:
     if len(stack) != 0 and stack.pop() != types[letter]:
       return False

  return len(stack) == 0

print(valid_parenthesis("((()(())))"))

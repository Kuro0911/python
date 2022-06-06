import random
def game(comp , you ):
  if comp == you:
    return None
  elif comp == 'R':
    if you=='S':
      return False
    elif you=='P':
      return True

  elif comp == 'P':
    if you=='S':
      return True
    elif you=='R':
      return False  

  elif comp == 'S':
    if you=='P':
      return False
    elif you=='R':
      return True   

#print("COMP turn : ROCK(R), PAPER(P) ,SCISSOR(S)")
  
randNo=random.randint(1 , 3)
#print(randNo)
if randNo == 1:
  comp = 'R'
elif randNo == 2:
  comp = 'P'
else:
  comp = 'S'   


you = input(" YOUR  turn : ROCK(R), PAPER(P) ,SCISSOR(S)")

a = game( comp ,you)

print(f"computer chose {comp}")

print(f"you chose {you}")

if a == None:
  print('''
  ************************
  -----G A M E -- TIE-----
  ************************

  ''')
elif a:
  print('''
  ************************
  -----Y O U -- W I N-----
  ************************

  ''')

else:
  print('''
  ************************
  -----Y O U -- L O S E-----
  ************************

  ''')

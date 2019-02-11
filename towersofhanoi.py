from stack import Stack

print("\nLet's play Towers of Hanoi!\n\nThe goal of the puzzle is to move\nall the disks from the leftmost peg\nto the rightmost peg, adhering to\nthe following rules:\n\n1) Move only one disk at a time.\n2) A larger disk may not be\nplaced ontop of a smaller disk.\n3) All disks, except the one\nbeing moved, must be on a peg.")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = 0
while num_disks <3:
  try:
    num_disks = int(input("\nHow many disks do you want to play with?\n"))
  except ValueError:
    continue
  while num_disks <3:
    try:
      num_disks = int(input("Enter a number greater than or equal to 3\n"))
    except ValueError:
      print("Please enter a number")
  for disk in range(num_disks,0,-1):
    left_stack.push(disk)
  num_optimal_moves = (2 ** num_disks)-1
  print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))
  
#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
        name = stacks[i].get_name()
        letter = stacks[i].get_name()[0]
        print("Enter {letter} for {name}".format(letter=letter,name=name))
    user_input = input("")
    if user_input.upper() in choices:
      for i in range(len(choices)):
        if user_input.upper() == choices[i]:
          return stacks[i]      
#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    else:
      print("\nWhich stack do you want to move to?\n")
      to_stack = get_input()
      if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        break
      else:
        print("\n\nInvalid Move. Try Again")
if num_user_moves == num_optimal_moves:
  print("\n\nCongratulations! You beat the game\nin the least number of moves, {0}.\nGood job :)".format(num_optimal_moves))
else:
  print("\n\nYou completed the game in {0} moves,\nand the optimal number of moves is {1}.\nNot too shabby, but you can do better ;)".format(num_user_moves,num_optimal_moves))
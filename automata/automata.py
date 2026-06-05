# Variables to store automata data
transitions = {}
start_state = ""
final_states = set()


def teach_automata():
  global transitions, start_state, final_states

  # Reset automata data
  transitions = {}
  final_states = set()

  # Get input from user
  states = input("Enter states (space separated): ").split()
  start_state = input("Enter Start state: ")
  final_states = set(input("Enter final state (space separated): ").split())

  # Validate input data
  if start_state not in states or not final_states.issubset(states):
    print("Invalid start state or final state")
    return
  
  print("\nEnter transitions:")
  print("Format: current_state symbol next_state")
  print("Enter 'done' when finished \n")

  while True:
    transition = input("Transition: ")

    if transition.lower() == "done":
      break
    
    parts = transition.split()

    # To validate format
    if len(parts) != 3:
      print("Invalid transition")
      continue

    current_state, symbol, next_state = parts

    # Check if states exist
    if current_state not in states or next_state not in states:
      print("States do not exist")
      continue
    
    
    transitions[current_state, symbol] = next_state
  
  print("Automata saved \n")


def test_string():
  global transitions, start_state, final_states
  
  # Check if automata exists
  if not transitions:
    print("Teach automata first\n")
    return
  
  word = input("\nEnter string: ")
  current_state = start_state
  valid = True

  # Start checking
  for char in word:
    # If transition does not exist, string is invalid
    if (current_state, char) not in transitions:
      valid = False
      break
    else:
      # Move to next state
      current_state = transitions[(current_state, char)]

  # Check if final state is reached
  if valid and current_state in final_states:
    print("yes\n")
  else: 
    print("no\n")


while True:
  print("1. Teach automata")
  print("2. Test string")
  print("3. Exit")

  choice = input("Choice: ")

  if choice == "1":
    teach_automata()
  elif choice == "2":
    test_string()  
  elif choice == "3":
    break
  else:
    print("Invalid choice \n\n")
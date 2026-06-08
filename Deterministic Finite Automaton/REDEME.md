Finite Automaton Simulator

A command-line tool that simulates a finite automaton (DFA).
You can define states, transitions, and test strings against the automaton.


# How to Use

## 1. Teach Automata
- Enter states (e.g. `q0 q1 q2`)
- Enter start state (e.g. `q0`)
- Enter final states (e.g. `q2`)
- Enter transitions in format: `current_state symbol next_state` (e.g. `q0 a q1`)
- Type `done` when finished

## 2. Test String
- Enter a string to test
- The program will output `yes` if the string is accepted, `no` if not

# Example
This automaton checks if a string end with `a` 

**Setup:**

States: q0 q1
Start state: q0
Final state: q1

Transitions:
q0 a q1
q0 b q0
q1 a q1
q1 b q0


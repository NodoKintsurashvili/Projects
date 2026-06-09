from typing import Dict, Tuple, Set

class DeterministicFiniteAutomata:
    def __init__(self):
        self.states: Set[str] = set()
        self.start_state: str = ""
        self.final_states: Set[str] = set()
        self.transitions: Dict[Tuple[str, str], str] = {}

    def set_automaton_data(self, states: list, start_state: str, final_states: list) -> bool:
        self.states = set(states)
        self.start_state = start_state
        self.final_states = set(final_states)


        if self.start_state not in self.states or not self.final_states.issubset(self.states):
            return False
        return True

    def add_transition(self, current_state: str, symbol: str, next_state: str) -> bool:
        if current_state not in self.states or next_state not in self.states:
            return False
        
        self.transitions[(current_state, symbol)] = next_state
        return True

    def validate_string(self, word: str) -> bool:
        if not self.transitions:
            raise ValueError("Automaton has no transitions defined.")

        current_state = self.start_state
        
        for char in word:
            if (current_state, char) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, char)]

        return current_state in self.final_states

def main():
    dfa = DeterministicFiniteAutomata()
    
    print("--- Teach Automaton ---")
    states = input("Enter states (space separated): ").split()
    start = input("Enter Start state: ")
    finals = input("Enter final states (space separated): ").split()

    if not dfa.set_automaton_data(states, start, finals):
        print("Invalid setup data!")
        return

    print("\nEnter transitions (Format: current_state symbol next_state). Type 'done' to finish:")
    while True:
        line = input("Transition: ")
        if line.lower() == 'done':
            break
        
        parts = line.split()
        if len(parts) != 3:
            print("Invalid format!")
            continue
            
        curr, sym, nxt = parts
        if dfa.add_transition(curr, sym, nxt):
            print("Transition saved.")
        else:
            print("Error: States do not exist.")

    print("\n--- Test Strings ---")
    while True:
        word = input("Enter string to test (or 'exit'): ")
        if word.lower() == 'exit':
            break
        
        result = dfa.validate_string(word)
        print("YES" if result else "NO")

if __name__ == "__main__":
    main()

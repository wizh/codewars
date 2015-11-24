class Automaton(object):

    def __init__(self):
        self.states = ['q1', 'q2', 'q3']
        self.transitions = {('q1', '0'): 0, ('q1', '1'): 1,
                            ('q2', '0'): 2, ('q2', '1'): 1,
                            ('q3', '0'): 1, ('q3', '1'): 1}
        self.current = 'q1'
        self.accepting = ['q2']

    def read_commands(self, commands):
        for c in commands:
            self.current = self.states[self.transitions[(self.current, c)]]
        return self.current in self.accepting

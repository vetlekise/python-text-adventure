class Puzzle:
    def __init__(self, description, answer, reward, is_solved=False):
        self.description = description
        self.answer = answer
        self.reward = reward
        self.is_solved = is_solved
    
    def check_answer(self, player_input):
        ...
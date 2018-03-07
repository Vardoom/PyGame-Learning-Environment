from ple.games.flappybird import FlappyBird
from ple import PLE

game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
agent = myAgentHere(allowed_actions=p.getActionSet())

n_generations = 100 # The number of generations used

p.init()
reward = 0.0

for i in range(n_generations):
    if p.game_over():
        p.reset_game()

    observation = p.getScreenRGB()
    action = agent.pickAction(reward, observation)
    reward = p.act(action)

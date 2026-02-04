class SoccerAgent:
    def __init__(self, name):
        self.name = name
        print(self.name, "PEAS Agent Started")

    def perceive(self, ball_position, opponent_near, teammate_open, goal_open):
        self.ball_position = ball_position
        self.opponent_near = opponent_near
        self.teammate_open = teammate_open
        self.goal_open = goal_open

    def decide_action(self):
        if self.ball_position == "close" and self.goal_open:
            return "Kick towards goal"
        elif self.opponent_near and self.teammate_open:
            return "Pass to teammate"
        elif self.opponent_near:
            return "Dribble away from opponent"
        elif self.ball_position == "far":
            return "Move towards ball"
        else:
            return "Maintain position"

    def act(self, action):
        print("Action:", action)


agent = SoccerAgent("Striker")

print("\nScenario 1")
agent.perceive("close", False, False, True)
agent.act(agent.decide_action())

print("\nScenario 2")
agent.perceive("close", True, True, False)
agent.act(agent.decide_action())

print("\nScenario 3")
agent.perceive("far", False, False, False)
agent.act(agent.decide_action())

print("\nScenario 4")
agent.perceive("close", True, False, False)
agent.act(agent.decide_action())

print("\nScenario 5")
agent.perceive("close", True, True, True)
agent.act(agent.decide_action())

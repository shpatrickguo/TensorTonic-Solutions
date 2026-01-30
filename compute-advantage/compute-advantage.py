import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    T = len(rewards)
    returns = np.zeros(T)
    running_returns = 0
    for t in reversed(range(T)):
        running_returns = rewards[t] + gamma*running_returns
        returns[t] = running_returns
    return returns - V


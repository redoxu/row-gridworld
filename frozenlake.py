import gymnasium as gym
from policies import compute_q_value, improve_policy,epsilon
import numpy as np  
#0: Move left; 1: Move down; 2: Move right; 3: Move up
env=gym.make("FrozenLake-v1")
class FrozenLakeWrapper:
    def __init__(self):
        self.env = gym.make("FrozenLake-v1")
        self.nS = self.env.observation_space.n
        self.nA = self.env.action_space.n
        self.P = self.env.unwrapped.P
env= FrozenLakeWrapper()
P=env.P
print(P[0][0])  # Affiche les transitions pour l'état 0 et l'action 0

###Avec Policy Iteration
V=np.zeros(16)  # Valeurs initiales
"""
pi= np.ones((16, 4)) / 4  # Politique uniforme initiale
i=0
while True:
    i+=1
    V,improved=evaluate_policy(env,pi,0.9,V,epsilon=epsilon)
    pi=improve_policy(env, pi, V)
    if not improved:
        print("Convergence après {} itérations".format(i))
        break
print(pi[0])
"""
###Avec Value Iteration
i=0
while True:
    i+=1
    delta=0
    for s in range(env.nS):
        q_s = np.zeros(env.nA)
        for a in range(env.nA):
            q_s[a] = compute_q_value(env, V, s, a, gamma=0.95)
        newV= np.max(q_s)
        delta= max(delta, abs(newV - V[s]))
        V[s] = newV
    if delta < epsilon:
        print("Value Iteration terminé après {} itérations.".format(i),V)
        break
pi=np.ones((env.nS, env.nA)) / env.nA  # Politique uniforme initiale
pi=improve_policy(env, pi, V)
print("Politique finale:", pi[0])  # Affiche la politique pour l'état
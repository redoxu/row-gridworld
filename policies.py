import numpy as np
from dictionnaire import GridworldRow
env=GridworldRow()
pi=np.ones((env.nS, env.nA)) *0.5
V=np.zeros(env.nS)
gamma=0.99
epsilon=0.00001 #seuil de similitude


def compute_q_value(env,s,a,gamma):
    q=0
    for p_sPrime,sPrime,reward,_ in env.P[s][a]:
        q += p_sPrime * (reward + gamma * V[sPrime])
    return q
"""
###policy evaluation
i=0
while True:
    delta=0
    i+=1
    for s in range(env.nS):
        V_new = 0
        for a in range(env.nA):
            V_new += pi[s][a] * compute_q_value(env, s, a, gamma)
        delta=max(delta,np.abs(V_new - V[s])) #maximum sur toutes les differences des composantes de V
        V[s] = V_new
    if delta < epsilon:
        print("Convergence après {} iterations".format(i))
        break
print(V)

###Policy improvement
for s in range(env.nS):
    q_s=np.zeros(env.nA)
    for a in range(env.nA):
        q_s[a]=compute_q_value(env,s,a,gamma)
    best_a=np.argmax(q_s)
    pi[s]=np.eye((env.nA))[best_a]  # Met à jour la politique pour choisir la meilleure action
print(pi)
"""

###Policy iteration
def evaluate_policy(env, pi, gamma,V,epsilon):
    V_updated = np.copy(V)
    improved =True
    while True:
        delta=0
        for s in range(env.nS):
            V_new = 0
            for a in range(env.nA):
                V_new += pi[s][a] * compute_q_value(env, s, a, gamma)
            delta=max(delta,np.abs(V_new - V[s])) #maximum sur toutes les differences des composantes de V
            V[s] = V_new
        if delta < epsilon:
            break
    if(np.array_equal(V, V_updated)):
        improved = False
    return V, improved
def improve_policy(env, pi):
    for s in range(env.nS):
        q_s=np.zeros(env.nA)
        for a in range(env.nA):
            q_s[a]=compute_q_value(env,s,a,gamma)
        best_a=np.argmax(q_s)
        pi[s]=np.eye((env.nA))[best_a]  # Met à jour la politique pour choisir la meilleure action
    return(pi)

i=0
while True:
    i+=1
    V, improved = evaluate_policy(env, pi, gamma, V, epsilon)
    pi= improve_policy(env, pi)
    if not improved:
        print("Convergence après {} iterations".format(i))
        break
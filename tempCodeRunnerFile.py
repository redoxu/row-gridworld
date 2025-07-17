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

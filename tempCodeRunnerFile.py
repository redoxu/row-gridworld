
pi= np.ones((16, 4)) / 4  # Politique uniforme initiale
V=np.zeros(16)  # Valeurs initiales
i=0
while True:
    i+=1
    V,improved=evaluate_policy(env,pi,0.9,V,epsilon=epsilon)
    pi=improve_policy(env, pi, V)
    if not improved:
        print("Convergence après {} itérations".format(i))
        break
print(pi[0])

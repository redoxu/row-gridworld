# Le dictionnaire P
Convention pour établir un environnement

P={s0:{a0:[(s'),(s')],a1:[(s'),(s')]},s1:{a0:[(s'),(s')],a1:[(s'),(s')]}}

(s')=(p(s'|s,a),s',r(s',s,a),done)

done = bool vrai si lenvironnement sarrete si on atteint s' 

## Exemple du row gridworld

S0(death)   S1    S2    S3     S4(win)

-100        0     0     0      +10

etat initial:S2

action0: aller a gauche ; action1: aller a droite

si S0 ou S4 fin du jeu

# Implémentation de Policy evaluation,Improvement,Iteration
## Policy Evaluation
calcul de la value function de la policy aleatoire

On représente la policy pi sous forme de matrice  pi(aj|si)

## Policy Improvement
deduction de pi' grace a v_pi

## Policy Iteration
Alternance des deux taches


# Implémentation de Modified Policy Iteration et Value iteration

# Environnement Frozen Lake
FrozenLake est un environnement Gym de type gridworld.
L'agent possède 4 actions : 0: Move left
1: Move down
2: Move right
3: Move up

Toutes les actions ne sont cette fois toutefois pas deterministes , il ya possibilité de glisser,  si on choisit laction haut 
on a 1/3 de chance d'aller en haut , 1/3 a droite et 1/3 a gauche.
Il y a 16 states (cases) , dont certainnes sont de l'eau mortelle (done=True)
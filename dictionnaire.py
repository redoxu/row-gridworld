class GridworldRow():
    def __init__(self, size=5):
        self.size = size
        self.nS=size
        self.nA=2
        
        self.MAX_X = size - 1
        
        P= {}
        for s in range(self.nS):
            dictionnaire_s = {}
            for a in range(self.nA):
                s_prime_list = []
                p=1 if s !=0 and s != self.MAX_X else 0
                if a == 0:
                    s_prime = s - 1 if s > 0 else s
                else:
                    s_prime = s + 1 if s < self.MAX_X else s
                if s_prime == 0:
                    reward=-100
                    done=True
                elif s_prime == self.MAX_X:
                    reward=10
                    done=True
                else:
                    reward=0
                    done=False
                s_prime_list.append((p, s_prime, reward, done))
                dictionnaire_s[a] = s_prime_list
            P[s] = dictionnaire_s
        self.P = P
env=GridworldRow()
P=env.P

import numpy as np
import math as m
import matplotlib.pyplot as plt

# Paramètres initiaux
S0 = 100         # Prix initial du sous-jacent
r = 0.05         # Taux sans risque
vol = 0.5      # Volatilité
T = 1.0          # Horizon de temps (en années)
N = 1000         # Nombre de trajectoires
n = 252          # Nombre de pas de temps (1 an = 252 jours de trading)
K=110            #prix strike


dt=T/n 
tGrille= np.linspace(0,T,n+1)

#simulation trajectoires
S=np.zeros((N,n+1))
S[:,0]= S0 #initialisation des trajectoires

for t in range (1,n+1):
    Z=np.random.normal(0,1,N)
    S[:,t]=S[:,t-1]*np.exp((r-vol**2*0.5)*dt+vol*np.sqrt(dt)*Z)


# Visualisation de quelques trajectoires
plt.figure(figsize=(10, 6))
for i in range(10):  # Afficher 10 trajectoires aléatoires
    plt.plot(tGrille, S[i])
plt.title("Trajectoires simulées du sous-jacent")
plt.xlabel("Temps (années)")
plt.ylabel("Prix du sous-jacent")
plt.grid(True)
plt.show()



#PAYOFF option asiatique

#calculer moy prix simulés pour chaque trajectoire
average_price = np.mean(S[:, 1:], axis=1) 

#calcule Payoff pour chaque trajectoire
payoff = np.maximum(average_price - K, 0)

#moyenne des payoff pr estimer prix de l'option

prixEstime=np.mean(payoff)

#prix actualisé
prixActu=prixEstime*np.exp(-r*T)

print(f"Prix estimé de l'option asiatique (call) : {prixActu:.2f}")



#PAYOFF option lookback call

#calcule Smax pour chaque trajectoire
Smax = np.max(S[:,1:], axis=1)
#calcule Payoff pour chaque trajectoire
payoffLbCall = np.maximum(Smax - K, 0)

#moyenne des payoff pr estimer prix de l'option

prixEstimeLbCall=np.mean(payoffLbCall)

#prix actualisé
prixActuLbCall=prixEstimeLbCall*np.exp(-r*T)

print(f"Prix estimé de l'option lookback (call) : {prixActuLbCall:.2f}")

#PAYOFF option lookback put

#calcule Smin pour chaque trajectoire
Smin = np.min(S[:,1:], axis=1)
#calcule Payoff pour chaque trajectoire
payoffLbPut= np.maximum(K-Smin, 0)

#moyenne des payoff pr estimer prix de l'option

prixEstimeLbPut=np.mean(payoffLbPut)

#prix actualisé
prixActuLbPut=prixEstimeLbPut*np.exp(-r*T)

print(f"Prix estimé de l'option lookback (put) : {prixActuLbPut:.2f}")

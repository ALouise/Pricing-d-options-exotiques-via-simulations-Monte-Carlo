Projet : Pricing d’options exotiques et simulations Monte Carlo
Objectif principal :
Étendre le pricer initial pour inclure des options exotiques.
Utiliser des simulations Monte Carlo pour pricer des options complexes qui ne peuvent pas être évaluées analytiquement.
Étapes du projet :
1. Comprendre les options exotiques
Barrière (Knock-in/Knock-out) :

L’option n’existe ou ne disparaît que si le sous-jacent atteint une barrière prédéfinie 
𝐻
H.
Exemple : une option call knock-out est annulée si le prix dépasse 
𝐻
H.
Lookback :

Le payoff dépend du prix minimum ou maximum atteint par le sous-jacent.
Exemple : 
max
⁡
(
𝑆
max
−
𝐾
,
0
)
max(S 
max
​
 −K,0) pour un call lookback.
Asiatiques (prix moyen) :

Le payoff dépend de la moyenne des prix du sous-jacent sur une période donnée :
max
⁡
(
1
𝑛
∑
𝑖
=
1
𝑛
𝑆
𝑖
−
𝐾
,
0
)
max( 
n
1
​
  
i=1
∑
n
​
 S 
i
​
 −K,0)
2. Implémentation des options exotiques avec Monte Carlo
A. Simuler des chemins pour le sous-jacent
Équation à simuler :
𝑆
𝑡
+
Δ
𝑡
=
𝑆
𝑡
⋅
𝑒
(
𝑟
−
𝜎
2
2
)
Δ
𝑡
+
𝜎
Δ
𝑡
⋅
𝑍
S 
t+Δt
​
 =S 
t
​
 ⋅e 
(r− 
2
σ 
2
 
​
 )Δt+σ 
Δt
​
 ⋅Z
 
Où 
𝑍
∼
𝑁
(
0
,
1
)
Z∼N(0,1).
Points-clés :
Créez une grille de temps avec un pas 
Δ
𝑡
=
𝑇
𝑛
Δt= 
n
T
​
 .
Simulez 
𝑁
N chemins indépendants.
B. Pricing des options
Option asiatique :

Calculez la moyenne des prix simulés pour chaque chemin.
Appliquez le payoff : 
max
⁡
(
moyenne
−
𝐾
,
0
)
max(moyenne−K,0) pour un call.
Option lookback :

Enregistrez le maximum (ou minimum) atteint par chaque chemin.
Appliquez le payoff : 
max
⁡
(
𝑆
max
−
𝐾
,
0
)
max(S 
max
​
 −K,0) pour un call.
Option barrière :

Vérifiez si le chemin atteint la barrière 
𝐻
H.
Appliquez le payoff uniquement pour les chemins éligibles.
C. Calculer le prix de l’option
Moyennez les payoffs sur tous les chemins simulés.
Actualisez le résultat en utilisant le facteur d’escompte : 
𝑒
−
𝑟
𝑇
e 
−rT
 .
3. Ajout de fonctionnalités avancées
Convergence des simulations :

Étudiez comment le nombre de chemins 
𝑁
N affecte la précision du prix.
Tracez la convergence du résultat.
Visualisation :

Représentez quelques trajectoires simulées du sous-jacent.
Visualisez l’impact des paramètres 
𝜎
,
𝑇
,
𝐾
,
𝐻
σ,T,K,H sur le prix.
Optimisation :

Implémentez des méthodes de réduction de variance comme l’échantillonnage antithétique ou les variables de contrôle.
Plan de démarrage :
Étape 1 : Simuler des trajectoires du sous-jacent

Générer 
𝑁
N chemins à partir d’un point 
𝑆
0
S 
0
​
 .
Visualiser les trajectoires pour vérifier leur cohérence.
Étape 2 : Implémenter un type d’option exotique (ex. : asiatique).

Ajouter les conditions spécifiques pour calculer le payoff.
Tester avec des paramètres simples (ex. : 
𝑆
0
=
100
,
𝐾
=
110
,
𝜎
=
0.2
,
𝑇
=
1
,
𝑟
=
0.05
S 
0
​
 =100,K=110,σ=0.2,T=1,r=0.05).
Étape 3 : Étendre à d’autres options exotiques.

Ajouter les barrières ou lookbacks.

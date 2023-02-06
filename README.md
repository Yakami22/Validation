# Projet de Validation
Ce projet a été réalisé par **Yassine KARMOUNI**, **Souhaila NOUINOU** et **Sam NZONGANI** dans le cadre du cours de validation à l'ENSTA Bretagne en filière CSN.

L'objectif est de faire du model checking, c'est à dire de vérifier si le modèle d'un système satisfait une propriété. Par exemple, on souhaite vérifier qu'un programme ne se bloque pas, qu'une variable n'est jamais nulle, etc.

## Description
### Parcours de graphe
La première étape est le parcours de graphe. En théorie des graphes, un parcours de graphe est un algorithme consistant à explorer les sommets d'un graphe de proche en proche à partir d'un sommet initial. Nous avons commencé par un parcours en largeur (breach first algorithm).

<p align="center">
    <img src="https://user-images.githubusercontent.com/91531132/216988989-38f0a732-4e5e-4c60-ad4c-2f0c50367b0e.png" width=300 height=300>
</p>

Pour le graphe ci-dessus l'ordre de parcours est le suivant: **1, 2, 3, 5, 6, 4**

Afin de déterminer l'état possible après un état donné nous avons implémenter pour chaque système une méthode prenant un état en paramètre et renvoyant la liste des suivants possibles. Ceci est illustré dans la suite.

### Transitions
#### N bits
Cette classe prend deux entiers en argument qui correspondent respectivement à un nombre ``n`` et à un nombre de bit sur lequel il sera représenté.
La transition vers un état possible consiste à modifier un seul des ``n`` bits.

*Exemple: Pour le nombre 3 codé sur 3 bits* 
<p align="center">
    <img src="https://user-images.githubusercontent.com/91531132/217005243-3e8e3ac7-9596-4bb0-8c2f-eb03acad7bcf.png" width=350 height=200>
</p>


#### Tours de Hanoi
Nous avons ensuite implémenter les tours de Hanoi. Il est important de noter qu'il ne s'agit pas de l'implémentation du jeu mais d'une configuration souhaitée.
La méthode décrite précédemment renvoie les configurations possibles au prochain tour (en comptant celui qui consiste à ne pas jouer).

<p align="center">
    <img src="https://user-images.githubusercontent.com/91531132/216992112-f8cc8ac9-1819-42ec-ae02-ec32db4b4347.png" width=550 height=250>
</p>

Pour la configuration ci-dessus les états suivants sont montrés ci-dessous.
![image](https://user-images.githubusercontent.com/91531132/217007086-8d0c2a2a-8d13-4fa4-ac6e-722917f0d489.png)


Séance 2 :

      Créer la classe abstraite TransitionRelation, qui contient les méthode abstraites get_roots  et next:
        Get_roots retourne les racines d'une structure.
        Next retourne toutes les configurations suivantes d'une structure.

```python

             class TransitionRelation:

                 @abstractmethod
                 def getRoots(self):
                     pass

                 @abstractmethod
                 def next(self, source):
                     pass
```

      Créer les classes Nbits, DictGraph et HanoiRules qui héritent de la classes TransitionRelation.

      Les testes :

      Nbits :
        Pour la méthode next, prend une liste binaire par exemple [0 ,0, 1] et renvoie la liste de toutes les configurations possibles en modifiant un bit à la fois.
        Résultat : list of neighbours in binary [[1, 0, 1], [0, 1, 1], [0, 0, 0]]

       HanoiRules:
        Pour la méthode next, on prend une liste d'une configuration donnée par exemple [[3, 1], [2], []] . Et renvoie la liste de toutes les configurations possibles de l'étape prochaine, en respectant les régles des tours de hanoi.
           Attention on ne cherche pas à résoudre le probleme de la tour de hanoi.
           Et donc dans ce cas la fonction retourne:
            [  [[3, 1], [2], []],
               [[3], [2, 1], []],
               [[3], [2], [1]],
               [[3, 1], [], [2]]  ]


              En gros, on parcours notre liste d'entrée ( la configuration donnée), et on parcours cette configuration
              en comparant le dernier élément de chaque tour

```python
               for i in range(len(lista)):
                     # len(lista) = num des tours
                     resultat = copy.deepcopy(lista)
                     if resultat[i]:
                         disk = resultat[i].pop()
                         for j in range(len(lista)):

                             if i!=j and (not resultat[j]) :
                                 temp = copy.deepcopy(resultat)
                                 temp[j].append(disk)
                                 next_states.append(temp)

                             elif i!=j and resultat[j][-1]> disk:
                                 temp = copy.deepcopy(resultat)
                                 temp[j].append(disk)
                                 next_states.append(temp)

```

     Remarque: Dans ces méthodes on se sert des deepcopy de nos listes.

Séance 3 :

       L'objective de cette séance est la Géneration de trace du graphe.
       On cherche à construire le graphe des parents en se servant des methodes next() et roots().
       On crée la classes Identity Proxy.

```python
       class IdentityProxy :

            def __init__(self,operand):
                self.operand = operand

            def __getattr__(self, item):
                return getattr(self.operand,item)
```

        On crée également la classe ParentTraceProxy qui hérite de la classe IdentityProxy.
        Et là ou l'on implemente les méthodes roots() et next().

        La méthode roots() retourne les racines des graphes.

```python
            def roots(self):
                neighbours = self.operand.roots()
                for n in neighbours:
                    self.dict[n] = n
                return neighbours

```

         La méthode next() retourne les prochaines noeuds des graphes.

```python
            def next(self, source):
                neighbours = self.operand.next(source)
                for n in neighbours:
                    if n not in self.dict:
                        self.dict[n] = source
                return neighbours

```

        Remarque; À cette étape on a également séparé les classes dans les packages pour faciliter la modularité.

Séance 4 :
notre propre langage + alice et bob
create configuartion Aconfig
create class copy class c1 def init

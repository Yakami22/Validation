# Validation

Séance 1 :

    Algorithme de parcours en largeur (bfs).

    Méthode itérative et récursive.
    Le principe est de commencer à partir d'un nœud source. Puis lister tous les voisins de la source, pour ensuite les explorer un par un.
    Les testes.
         Pour un graphe , graph2 = {
                              1 : [2,3],
                              2 : [5,6],
                              3 : [],
                              4 : [4,6],
                              5 : [4],
                              6 : [6]
                          }


         Le résultat est :  [1, 2, 3, 5, 6, 4]

     Ajouter les call-backs : on_entry , on_known , on_entry.



        bool on_entry(source, neighbour, accumulateur) pour arreter la progression dans le graph si neighbour in not in known .

        bool on_known(source, neighbour, accumulateur)  à chaque fois qu'on tombe sur un noeud connu on retourne acc et known.

        bool on_exit(source, accumulateur) avant d exiter la fonction bfs.

        Il faut placer ces fonctions dans le bon endroit dans la fonction bfs.

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

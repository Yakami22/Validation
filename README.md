# Validation

Scéance 1 : 

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
         
         
Scéance 2 : 

      Créer la classe abstraite TransitionRelation, qui contient les méthode abstraites get_roots  et next:
        Get_roots retourne les racines d'une structure.
        Next retourne toutes les configurations suivantes d'une structure. 
      
      Créer les classes Nbits, DictGraph et HanoiRules qui héritent de la classes TransitionRelation.
      
      Les testes : 
      
      Nbits : 
        Pour la méthode next, prend une liste binaire par exemple [0 ,0, 1] et renvoie la liste de toutes les configurations possibles en modifiant un bit à la fois.
        Résultat : list of neighbours in binary [[1, 0, 1], [0, 1, 1], [0, 0, 0]]
     
       HanoiRules:
     
Scéance 3 : 


       Géneration de trace

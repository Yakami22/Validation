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

## Guardes et trace
Jusque là, les régles spécifiques à chaque modèle (n bits, Hanoi, etc.) étaient définie dans la méthode indiquant les états suivants possibles.
Afin d'améliorer le code nous avons créé des **gardes** qui correspondent à des régles. Si une garde n'est pas respectée, l'action n'est pas effectué.

Pour faciliter le suivi, nous avons créé des **traces* qui indiquent les actions effectuées.

## Alice et Bob

## Tests

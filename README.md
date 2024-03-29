# Densidées

Le logiciel libre Densidées estime la densité des idées d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977, c'est à dire le nombre moyen d'idées exprimées en 10 mots), utile en particulier pour l'analyse des discours de patients atteint de la maladie d'Alzheimer.

Un texte étiqueté par TreeTagger doit lui être fourni en entrée. La performance du logiciel a été évaluée dans l'article indiqué ci-dessous (Lee et al., RECITAL 2010) sur un corpus oral retranscrit de 13939 mots dont 5747 propositions. Les résultats de la version 1.2 présentent 2,7% de faux négatifs et 3,1% de faux positifs, soit un taux d'erreur de 0,5% sur le nombre de prédicats.

Densidées adapte à la langue française le calcul de densité d'idées implémenté pour la langue anglaise dans le logiciel CPIDR (http://www.ai.uga.edu/caspr/), détaillé dans la publication suivante :
Cati Brown, Tony Snodgrass, Susan J. Kemper, Ruth Herman, et Michael A. Covington (2008) [Automatic measurement of propositional idea density from part-of-speech tagging](http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf). Behavior Research Methods 40 (2) 540-545.

Il a été créé dans le cadre d'une collaboration issue de la journée OSIDMESH (http://www.lirmm.fr/~semindoc/Osidmesh.html) d'octobre 2009, par [Hyeran Lee](http://www.praxiling.fr/lee-hyeran.html) et [Philippe Gambette](http://igm.univ-mlv.fr/~gambette), à l'époque doctorants des laboratoires [Praxiling](http://www.univ-montp3.fr/praxiling/) et [LIRMM](http://www.lirmm.fr) de Montpellier. [Melissa Barkat-Defradas](https://isem-evolution.fr/membre/barkat-defradas/), [Elsa Maillé](https://www.annuaire-audition.com/orthophoniste/vaulx-en-velin-69120/elsa-maille-5131-practice-6159.html) et [Constance Thuillier](https://www.annuaire-audition.com/orthophoniste/vaulx-en-velin-69120/constance-thuillier-8768-practice-6159.html) ont également contribué à la conception de ce logiciel, qui a donné lieu aux publications suivantes :
* Hyeran Lee, Philippe Gambette, Constance Thuillier et Elsa Maillé (2010) [Densidées : calcul automatique de la densité des idées dans un corpus oral](http://halshs.archives-ouvertes.fr/halshs-00495768/fr/). Actes de RECITAL 2010.
* Hyeran Lee, Philippe Gambette et Melissa Barkat-Defradas (2010) [Utilisation de l'analyse textuelle automatique dans la recherche sur la maladie d'Alzheimer](http://www.lirmm.fr/~gambette/2010LeeGambetteBarkat.pdf). Poster à CEDIL 2010 (http://www.lirmm.fr/~gambette/2010LeeGambetteBarkatPoster.pdf).


## Installation et utilisation

Densidées est écrit en Python, il faut donc commencer par [télécharger Python 3](https://www.python.org/downloads/) et l'installer (par exemple sous Windows) dans C:\Python39.

Puis, pour installer Densidées, téléchargez l'archive ZIP de la dernière version en utilisant le bouton vert "Code" puis "Download ZIP" ci-dessus, puis décompressez-la dans un répertoire quelconque de votre ordinateur.

Elle contient en particulier :
* Densidees.exe, le programme avec interface graphique à exécuter sous Windows (déconseillé avec la version 1.4)
* Densidees.py, le code du programme, à lancer avec Python
* ManuelDensidees.pdf, le manuel d'utilisateur, qui explique comment utiliser Densidées

Si vous voulez utiliser TreeTagger depuis le logiciel Densidées, il faudra également installer :
* TreeTagger
* Perl (par exemple sous Windows installer Strawberry Perl http://strawberryperl.com, puis redémarrer l'ordinateur)

Mais vous pouvez aussi utiliser la version de TreeTagger en ligne proposée par le Cental : https://cental.uclouvain.be/treetagger/

Nous conseillons d'utiliser Densidées en ligne de commande.
Pour cela, commencez par ouvrir une fenêtre de ligne de commande en allant dans le menu Démarrer, Exécuter, en tapant alors `cmd` puis en appuyant sur Entrée.
Il faut alors taper une ligne de commande de ce type : `"C:\Python39\python.exe" "C:\Densidees\Densidees.py" "C:\Densidees\treetagger_output.tsv"`
Cette commande signifie qu’on va appeler le logiciel Python.exe pour lui demander de lancer le programme Densidees.py sur le fichier texte `treetagger_output.tsv` qui contient le résultat de l’étiquetage TreeTagger d’un texte en français. On obtiendra alors le résultat dans le fichier `treetagger_output.tsv.di.txt`.
Vous pouvez utiliser l’option `oral=1` pour utiliser le calcul de densité des idées en mode oral (traitement des répétitions).


## Citation

Bien que Densidées soit un logiciel libre sous licence GPL, nous aimerions que vous fassiez référence à l'article suivant si vous l'utilisez dans une publication :
* Hyeran Lee, Philippe Gambette, Constance Thuillier et Elsa Maillé. [Densidées : calcul automatique de la densité des idées dans un corpus oral](http://halshs.archives-ouvertes.fr/halshs-00495768/fr/). RECITAL 2010.


## Versions

Version 1.4 (2021/04/06) :
* passage du code à Python 3 et à l'encodage Unicode

Version 1.3 (2010/06/30) :
* appel automatique de TreeTagger depuis Densidées
* mode "invisible" permettant de n'afficher que le résultat, en ligne de commande
* calcul de la densité des idées comme ratio pour 10 mots selon la formule traditionnelle
* amélioration des règles 208 et 701

Version 1.2 (2010/03/07) :
* prétraitement des auxiliaires si pas fait par TreeTagger
* 35 règles 001, 002, 020, 023, 024, 101, 102, 200, 054, 201, 202, 203, 204, 206, 207, 208, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 509, 510, 512, 600, 601, 602, 701, 702, 703

Version 1.1 (2009/12/12) :
* interface graphique
* mode oral
* affichage final du nombre de chacune des règles utilisées
* 27 règles : 002, 020, 023, 024, 200, 054, 201, 202, 203, 204, 206, 207, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 512, 600, 601, 602, 701
 
Version 1.0 (2009/11/21) :
* texte étiqueté par TreeTagger en entrée du programme
* 7 règles : 002, 003, 200, 201, 301, 302, 402
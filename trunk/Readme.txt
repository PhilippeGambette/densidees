Le programme Densidees calcule la densité d'idées d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977).

Il adapte à la langue française le calcul implémenté pour la langue anglaise dans le logiciel CPIDR (http://www.ai.uga.edu/caspr/), détaillé dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) Automatic measurement of propositional idea density from part-of-speech tagging. Behavior Research Methods 40 (2) 540-545 (http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf).

** Installation et utilisation **

Densidees est écrit en Python (version 2.6), il faut donc commencer par télécharger Python sur http://www.python.org/download/releases/2.6/ et l'installer (par exemple sous Windows) dans C:\Python26.

Il faut alors ajouter des étiquettes morpho-syntaxiques au texte en français dont on veut calculer la densité d'idées (obtenu par exemple grâce à l'interface web http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php). Le texte étiqueté morpho-syntaxiquement doit alors être enregistré dans un fichier texte, par exemple C:\Densidees\Test.txt

On appelle alors le programme depuis la ligne de commande. Par exemple, sous Windows, dans le menu Démarrer, choisir Exécuter, taper cmd pour ouvrir la ligne de commande, puis taper :
C:\Python26\Python.exe C:\Densidees.py C:\Densidees\Test.txt
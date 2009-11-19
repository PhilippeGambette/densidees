Le programme Densidees calcule la densit� d'id�es d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977).

Il adapte � la langue fran�aise le calcul impl�ment� pour la langue anglaise dans le logiciel CPIDR (http://www.ai.uga.edu/caspr/), d�taill� dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) Automatic measurement of propositional idea density from part-of-speech tagging. Behavior Research Methods 40 (2) 540-545 (http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf).

** Installation et utilisation **

Densidees est �crit en Python (version 2.6), il faut donc commencer par t�l�charger Python sur http://www.python.org/download/releases/2.6/ et l'installer (par exemple sous Windows) dans C:\Python26.

Il faut alors ajouter des �tiquettes morpho-syntaxiques au texte en fran�ais dont on veut calculer la densit� d'id�es (obtenu par exemple gr�ce � l'interface web http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php). Le texte �tiquet� morpho-syntaxiquement doit alors �tre enregistr� dans un fichier texte, par exemple C:\Densidees\Test.txt

On appelle alors le programme depuis la ligne de commande. Par exemple, sous Windows, dans le menu D�marrer, choisir Ex�cuter, taper cmd pour ouvrir la ligne de commande, puis taper :
C:\Python26\Python.exe C:\Densidees.py C:\Densidees\Test.txt
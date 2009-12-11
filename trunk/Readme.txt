Le programme Densidees calcule la densité des idées d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977).

Il adapte à la langue française le calcul de densité d'idées implémenté pour la langue anglaise dans le logiciel [http://www.ai.uga.edu/caspr/ CPIDR], détaillé dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) [http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf Automatic measurement of propositional idea density from part-of-speech tagging]. Behavior Research Methods 40 (2) 540-545 .

== Installation et utilisation ==

Densidees est écrit en Python (version 2.6), il faut donc commencer par [http://www.python.org/download/releases/2.6/ télécharger Python] sur  et l'installer (par exemple sous Windows) dans C:\Python26.

Il faut alors ajouter des étiquettes morpho-syntaxiques au texte en français dont on veut calculer la densité d'idées (obtenu par exemple grâce à l'interface web http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php). Le texte étiqueté morpho-syntaxiquement doit alors être enregistré dans un fichier texte, par exemple C:\Densidees\Test.txt

== Citation ==

Bien que Densidees soit un logiciel libre sous licence GPL, nous aimerions que vous fassiez référence à l'article suivant si vous l'utilisez dans une publication :
 * Hye Ran Lee & Philippe Gambette. Utilisation de l'analyse textuelle automatique dans la recherche sur la maladie d'Alzheimer. Soumis au _Colloque international des jeunes chercheurs en Didactique des Langues et en Linguistique_ ([http://w3.u-grenoble3.fr/lidilem/colloque-ec/cedil2010/ CEDIL2010]).


== Versions ==

Version 1.1 (2009/12/12) :
 * interface graphique
 * mode oral
 * affichage final du nombre de chacune des règles utilisées
 * 27 règles : 002, 020, 023, 024, 200, 054, 201, 202, 203, 204, 206, 207, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 512, 600, 601, 602, 701
 
Version 1.0 (2009/11/21) :
 * texte étiqueté par TreeTagger en entrée du programme
 * 7 règles : 002, 003, 200, 201, 301, 302, 402
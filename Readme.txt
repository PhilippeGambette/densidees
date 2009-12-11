Le programme Densidees calcule la densit� des id�es d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977).

Il adapte � la langue fran�aise le calcul de densit� d'id�es impl�ment� pour la langue anglaise dans le logiciel [http://www.ai.uga.edu/caspr/ CPIDR], d�taill� dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) [http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf Automatic measurement of propositional idea density from part-of-speech tagging]. Behavior Research Methods 40 (2) 540-545 .

== Installation et utilisation ==

Densidees est �crit en Python (version 2.6), il faut donc commencer par [http://www.python.org/download/releases/2.6/ t�l�charger Python] sur  et l'installer (par exemple sous Windows) dans C:\Python26.

Il faut alors ajouter des �tiquettes morpho-syntaxiques au texte en fran�ais dont on veut calculer la densit� d'id�es (obtenu par exemple gr�ce � l'interface web http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php). Le texte �tiquet� morpho-syntaxiquement doit alors �tre enregistr� dans un fichier texte, par exemple C:\Densidees\Test.txt

== Citation ==

Bien que Densidees soit un logiciel libre sous licence GPL, nous aimerions que vous fassiez r�f�rence � l'article suivant si vous l'utilisez dans une publication :
 * Hye Ran Lee & Philippe Gambette. Utilisation de l'analyse textuelle automatique dans la recherche sur la maladie d'Alzheimer. Soumis au _Colloque international des jeunes chercheurs en Didactique des Langues et en Linguistique_ ([http://w3.u-grenoble3.fr/lidilem/colloque-ec/cedil2010/ CEDIL2010]).


== Versions ==

Version 1.1 (2009/12/12) :
 * interface graphique
 * mode oral
 * affichage final du nombre de chacune des r�gles utilis�es
 * 27 r�gles : 002, 020, 023, 024, 200, 054, 201, 202, 203, 204, 206, 207, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 512, 600, 601, 602, 701
 
Version 1.0 (2009/11/21) :
 * texte �tiquet� par TreeTagger en entr�e du programme
 * 7 r�gles : 002, 003, 200, 201, 301, 302, 402
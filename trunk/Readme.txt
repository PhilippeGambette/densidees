****** README DENSIDEES ******

Le programme Densidées calcule la densité des idées d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977). *Attention, il ne fournit qu'une approximation du score de densité des idées, une évaluation est actuellement en cours pour mesurer son taux d'erreur. Un texte étiqueté par TreeTagger doit lui être fourni en entrée, de préférence avec étiquetage des auxiliaires par le tag "VER:aux".*

Densidées adapte à la langue française le calcul de densité d'idées implémenté pour la langue anglaise dans le logiciel [http://www.ai.uga.edu/caspr/ CPIDR], détaillé dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) [http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf Automatic measurement of propositional idea density from part-of-speech tagging]. Behavior Research Methods 40 (2) 540-545.

Il a été créé dans le cadre d'une collaboration issue de la [http://www.lirmm.fr/~semindoc/Osidmesh.html journée OSIDMESH] d'octobre 2009, par [http://www.univ-montp3.fr/praxiling/spip.php?article229 Hye-Ran Lee] et [http://www.lirmm.fr/~gambette Philippe Gambette], doctorants des laboratoires [http://www.univ-montp3.fr/praxiling/ Praxiling] et [http://www.lirmm.fr LIRMM] de Montpellier. Mélissa Barkat-Defradas, Elsa Maillé et Constance Thuillier ont également contribué à la conception de ce logiciel.

== Installation et utilisation ==

Densidées est écrit en Python (version 2.6), il faut donc commencer par [http://www.python.org/download/releases/2.6/ télécharger Python] et l'installer (par exemple sous Windows) dans C:\Python26.

Puis, pour installer Densidées, téléchargez l'archive ZIP de la dernière version [http://code.google.com/p/densidees/downloads/list sur la page des téléchargements], puis décompressez-la dans un répertoire quelconque de votre ordinateur.

Elle contient en particulier :
 * Densidees.exe, le programme à exécuter sous Windows
 * Densidees.py, le code du programme
 * ManuelDensidees.pdf, le manuel d'utilisateur, qui explique comment utiliser Densidées


== Citation ==

Bien que Densidées soit un logiciel libre sous licence GPL, nous aimerions que vous fassiez référence à l'article suivant si vous l'utilisez dans une publication :
 * Hye Ran Lee, Philippe Gambette et Melissa Barkat-Defradas. Utilisation de l'analyse textuelle automatique dans la recherche sur la maladie d'Alzheimer. Poster au _Colloque international des jeunes chercheurs en Didactique des Langues et en Linguistique_ ([http://w3.u-grenoble3.fr/lidilem/colloque-ec/cedil2010/ CEDIL2010], [http://www.lirmm.fr/~gambette/2009LeeGambette.pdf résumé ici]).


== Versions ==

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
****** README DENSIDEES ******

Le programme Densid�es calcule la densit� des id�es d'un texte (au sens de Kintsch 1974 et Turner & Greene 1977). *Attention, il ne fournit qu'une approximation du score de densit� des id�es, une �valuation est actuellement en cours pour mesurer son taux d'erreur. Un texte �tiquet� par TreeTagger doit lui �tre fourni en entr�e, de pr�f�rence avec �tiquetage des auxiliaires par le tag "VER:aux".*

Densid�es adapte � la langue fran�aise le calcul de densit� d'id�es impl�ment� pour la langue anglaise dans le logiciel [http://www.ai.uga.edu/caspr/ CPIDR], d�taill� dans la publication suivante :
Brown, Cati; Snodgrass, Tony; Kemper, Susan J.; Herman, Ruth; and Covington, Michael A. (2008) [http://www.ai.uga.edu/caspr/BrownSnodgrassKemperHermanCovington2008.pdf Automatic measurement of propositional idea density from part-of-speech tagging]. Behavior Research Methods 40 (2) 540-545.

Il a �t� cr�� dans le cadre d'une collaboration issue de la [http://www.lirmm.fr/~semindoc/Osidmesh.html journ�e OSIDMESH] d'octobre 2009, par [http://www.univ-montp3.fr/praxiling/spip.php?article229 Hye-Ran Lee] et [http://www.lirmm.fr/~gambette Philippe Gambette], doctorants des laboratoires [http://www.univ-montp3.fr/praxiling/ Praxiling] et [http://www.lirmm.fr LIRMM] de Montpellier. M�lissa Barkat-Defradas, Elsa Maill� et Constance Thuillier ont �galement contribu� � la conception de ce logiciel.

== Installation et utilisation ==

Densid�es est �crit en Python (version 2.6), il faut donc commencer par [http://www.python.org/download/releases/2.6/ t�l�charger Python] et l'installer (par exemple sous Windows) dans C:\Python26.

Puis, pour installer Densid�es, t�l�chargez l'archive ZIP de la derni�re version [http://code.google.com/p/densidees/downloads/list sur la page des t�l�chargements], puis d�compressez-la dans un r�pertoire quelconque de votre ordinateur.

Elle contient en particulier :
 * Densidees.exe, le programme � ex�cuter sous Windows
 * Densidees.py, le code du programme
 * ManuelDensidees.pdf, le manuel d'utilisateur, qui explique comment utiliser Densid�es


== Citation ==

Bien que Densid�es soit un logiciel libre sous licence GPL, nous aimerions que vous fassiez r�f�rence � l'article suivant si vous l'utilisez dans une publication :
 * Hye Ran Lee, Philippe Gambette et Melissa Barkat-Defradas. Utilisation de l'analyse textuelle automatique dans la recherche sur la maladie d'Alzheimer. Poster au _Colloque international des jeunes chercheurs en Didactique des Langues et en Linguistique_ ([http://w3.u-grenoble3.fr/lidilem/colloque-ec/cedil2010/ CEDIL2010], [http://www.lirmm.fr/~gambette/2009LeeGambette.pdf r�sum� ici]).


== Versions ==

Version 1.2 (2010/03/07) :
 * pr�traitement des auxiliaires si pas fait par TreeTagger
 * 35 r�gles 001, 002, 020, 023, 024, 101, 102, 200, 054, 201, 202, 203, 204, 206, 207, 208, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 509, 510, 512, 600, 601, 602, 701, 702, 703

Version 1.1 (2009/12/12) :
 * interface graphique
 * mode oral
 * affichage final du nombre de chacune des r�gles utilis�es
 * 27 r�gles : 002, 020, 023, 024, 200, 054, 201, 202, 203, 204, 206, 207, 210, 211, 212, 213, 214, 301, 302, 402, 405, 500, 512, 600, 601, 602, 701
 
Version 1.0 (2009/11/21) :
 * texte �tiquet� par TreeTagger en entr�e du programme
 * 7 r�gles : 002, 003, 200, 201, 301, 302, 402
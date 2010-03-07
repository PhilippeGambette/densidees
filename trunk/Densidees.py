#!/usr/sfw/bin/python
# -*- coding: iso-8859-15 -*-
#C:\Python26\Python.exe C:\These\2009Densidees\densidees\Densidees.py C:\These\2009Densidees\densidees\Test.txt

#######################################################################
# Copyright 2010 Philippe Gambette, Hye-Ran Lee
# 
# Densidees v1.2 (07/03/2010).
#
# Densidees is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Densidees is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Densidees.  If not, see <http://www.gnu.org/licenses/>.
# 
# For more information:
# http://code.google.com/p/densidees
#######################################################################


import sys, os, re, string, time
from math import *



#------------------------------
# Chargement des paramètres
#------------------------------
args={}
i=1;
thefile="";
while i<len(sys.argv):
        res=re.search("(.*)[=](.*)",sys.argv[i])
        if res:
                args[res.group(1)]=res.group(2)
        else:
                thefile=sys.argv[i]
        i+=1

# oral=1 si mode oral
if not(args.has_key("oral")):
        args["oral"]=0
oral=int(args["oral"]);

# tag=treetagger par défaut
if not(args.has_key("tag")):
        args["tag"]="treetagger"
tagger=args["tag"];



#------------------------------
# Ouverture du texte
#------------------------------

# Open a text file and put into a 2-element table:
# -> a table containing the sequence of all words in the text
# -> a dict containing all distinct words of the text with associated nb of occurrences
# * filename: string
# * sepchar: string, used to separate cooccurrence windows, will not be added to wordlist
def openText(filename,tagger):
        fd = open(filename,"r")
        lines = fd.readlines()
        text=[]
        i=0
        
        #------------------------------
        #go through the text to extract the words, store them in dict "wordlist" with frequencies
        #and in table "text" in the order they appear
        #------------------------------
        for line in lines: 
                i+=1
                if tagger=="treetagger":                       
                        res=re.search("^([^	]+)	([^	]+)	([^	\n]+)[\n]*",line)
                        if res:
                                item={}
                                item["word"]=res.group(1).lower()
                                item["tag"]=res.group(2)
                                item["lemma"]=res.group(3)
                                item["rule"]="000"
                                item["isWord"]=" "
                                item["isProp"]=" "
                                #print item
                                text.append(item)
                        else:
                                print "Ligne",i,"non traitée :",line
                                item={}
                                item["word"]=" "
                                item["tag"]="INT"
                                item["lemma"]=" "
                                item["rule"]="000"
                                item["isWord"]=" "
                                item["isProp"]=" "
                                #print item
                                text.append(item)
                else:
                        res=re.search("^([0-9]+)	([0-9]+)	([0-9]+)		([^	]+)	([^	]+)	([^	]*)	([0-9]+)	([^	]+)	([^	]+).*",line)
                        #print line
                        #res=re.search("^([0-9]+)	([0-9]+)	([0-9]+)		([^	]+)	([^	]+)	([^	]*)	([0-9]+)	([^	]+)	([^	]+).*[\n]*",line)
                        if res:
                                item={}
                                item["word"]=res.group(4).lower()
                                item["lemma"]=res.group(5)
                                item["tag"]=res.group(9)
                                item["rule"]="000"
                                item["isWord"]=" "
                                item["isProp"]=" "
                                #print item
                                text.append(item)
                        else:
                                print "Ligne",i,"non traitée :",line
        fd.close()
        return text


#------------------------------
# Fonctions 
#------------------------------

def isTreetaggerPropTag(tag):
        result=False
        if tag=="KON" or tag=="NUM":
                result=True
        if re.search("^DET.*",tag):
                result=True        
        if re.search("^PRP.*",tag):
                result=True       
        if tag=="ADJ" or tag=="ADV":
        #enlevé par rapport à CPIDR : tag=="PRO:POS" or tag=="PRO:IND" 
                result=True
        if re.search("^VER.*",tag):
                result=True
        #if tag=="PRO:REL":
        #        result=True
        return result

def isCordialPropTag(tag):
        result=False
        if tag[0]=="C" or tag[0]=="M":
                result=True
        if tag[0]=="D":
                result=True        
        if tag[0]=="S":
                result=True
        if tag[0]=="A":
                result=True
        if tag[0]=="R":
                result=True
        if tag[0]=="V":
                result=True
        if tag[0]=="P" and tag[1]!="p":
                result=True
        return result

def isLink(lemma):
        result=False
        if lemma=="apparaître" or lemma=="suivre|être" or lemma=="être" or lemma=="sembler" or lemma=="devenir" or lemma=="paraître" or lemma=="rester" or lemma=="demeurer" or lemma=="faire":
                result=True
        return result

if os.path.isfile(thefile):
        print "Chargement du fichier texte..."
        output = open(thefile+".di.txt","w")

        
        # Open the text
        text=openText(thefile,tagger)
        i=0
        mode="normal"

        # Prétraitement auxiliaire si TreeTagger ne le fait pas
        while i < len(text):
                if (tagger=="treetagger" and ((text[i-1]["lemma"]=="être") or (text[i-1]["lemma"]=="suivre|être") or (text[i-1]["lemma"]=="avoir")) and (text[i]["tag"]=="VER:pper")):
                        text[i-1]["tag"]="VER:aux"
                if (tagger=="treetagger" and ((text[i-2]["lemma"]=="être") or (text[i-2]["lemma"]=="suivre|être") or (text[i-2]["lemma"]=="avoir")) and text[i-1]["tag"]=="ADV" and text[i]["tag"]=="VER:pper"):
                        text[i-2]["tag"]="VER:aux"
                #if (tagger=="treetagger" and ((text[i-3]["lemma"]=="être") or (text[i-2]["lemma"]=="suivre|être") or (text[i-2]["lemma"]=="avoir")) and text[i]["tag"]=="VER:pper"):
                #        text[i-3]["tag"]="VER:aux"
                if (tagger=="treetagger" and text[i]["lemma"]=="oui"):
                        text[i]["tag"]="ADV"
                i+=1

        i=0
        # Application des règles
        while i < len(text):
                #print text[i]["word"]
                if text[i]["word"]=="(":
                        mode="noprop"
                if text[i]["word"]==")":
                        mode="normal"
                if text[i]["word"]=="[":
                        mode="noword"
                if text[i]["word"]=="]":
                        mode="normal"
                        
                # 001 Interjections (mode oral)
                # Interjections non reconnues par TreeTagger => pas mot, pas proposition
                if (oral==1 and tagger=="treetagger" and (text[i]["word"]=="tiens" or text[i]["word"]=="heu")):
                        text[i]["tag"]="INT"
                        text[i]["rule"]="001"                        
                if (tagger=="treetagger" and text[i]["tag"]=="ADV" and text[i]["word"]=="ben"):
                        text[i]["tag"]="INT"
                        text[i]["rule"]="001"                
                if text[i]["word"]=="parce":
                        text[i]["tag"]="INT"
                        text[i]["rule"]="001"

                # 002 Ponctuation et symboles (mode oral)
                # Signe de ponctuation, symbole => pas mot
                #if re.search("^[a-zA-Zéèçàùêîôûäëïöü0-9]",text[i]["word"]) and text[i]["tag"]!="SYM":
                if (tagger=="treetagger" and (text[i]["tag"]!="SYM" and text[i]["tag"]!="PUN" and text[i]["tag"]!="SENT" and text[i]["tag"]!="INT")) or (tagger=="cordial" and (text[i]["tag"][0]!="Y")):
                        text[i]["isWord"]="W"
                        text[i]["rule"]="002"
                
                
                # 003 Succession de deux entiers regroupés en 1
                # géré par TreeTagger et 
                # Two cardinal numbers in immediate succession are combined into one
                # (Uncommon situation; the next one is much more common)
                # -> done by TreeTagger                
                #if text[i-1]["tag"]=="NUM" and text[i]["tag"]=="NUM":
                #        i=i-1
                #        text[i]["word"]=text[i]["word"]+" "+text[i+1]["word"]
                #        text[i]["rule"]="003"
                #        del text[i+1]

                # 004
                # Cardinal + nonalphanumeric + cardinal are combined into one token
                # (Common situation, for handling fractions, decimals, etc.
                # -> done by TreeTagger


                        
                
                # 020 Répétition ou correction d'un mot (mode oral)
                # A A ou préfixe-de-A A => premier A : pas mot, pas proposition
                if ((oral==1 and text[i]["word"].find(text[i-1]["word"])==0)):
                        text[i-1]["isWord"]=" "
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="020"
                
                # 021 022 ?
                
                # 023 Répétition ou correction de 2 mots (mode oral)
                # A B A B ou préfixe-de-A préfixe-de-B A B => premier A et premier B : pas mot, pas proposition
                # CHECK Vérifier que la règle du préfixe est pertinente ou la remplacer par []
                if ((oral==1 and text[i]["word"].find(text[i-2]["word"])==0 and text[i-1]["word"].find(text[i-3]["word"])==0)):
                        text[i-3]["isWord"]=" "
                        text[i-3]["isProp"]=" "
                        text[i-3]["rule"]="023"
                        text[i-2]["isWord"]=" "
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="023"
                
                
                # 024  Répétition ou correction de 3 mots (mode oral)
                # A B C A B C ou préfixe-de-A préfixe-de-B préfixe-de-C A B C => premier A, premier B et premier C : pas mot, pas proposition
                if ((oral==1 and text[i]["word"].find(text[i-3]["word"])==0 and text[i-1]["word"].find(text[i-4]["word"])==0 and text[i-2]["word"].find(text[i-5]["word"].lower())==0)):
                        text[i-5]["isWord"]=" "
                        text[i-5]["isProp"]=" "
                        text[i-5]["rule"]="024"
                        text[i-4]["isWord"]=" "
                        text[i-4]["isProp"]=" "
                        text[i-4]["rule"]="024"
                        text[i-3]["isWord"]=" "
                        text[i-3]["isProp"]=" "
                        text[i-3]["rule"]="024"

                        
                
                # passif : problème de "par" ? Ne pas le compter si précédé d'un verbe au passif ?
                
                # 101 est-ce que ...
                # Ne pas compter comme proposition en mode oral
                if ((oral==1) and (text[i-2]["lemma"]=="être") and (text[i-1]["lemma"]=="ce") and (text[i]["lemma"]=="que")):
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="101"
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="101"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="101"


                # 102 Clivages
                # C'est + (au plus 5 mots) + "que" ou "qui" : "est" non compté comme proposition
                if ((text[i]["lemma"]=="que") or (text[i]["lemma"]=="qui")):
                        if ((text[i-2]["lemma"]=="ce") and (text[i-1]["lemma"]=="être")):
                                text[i-1]["isProp"]=" "
                                text[i-1]["rule"]="102"
                        if ((text[i-3]["lemma"]=="ce") and (text[i-2]["lemma"]=="être")):
                                text[i-2]["isProp"]=" "
                                text[i-2]["rule"]="102"
                        if ((text[i-4]["lemma"]=="ce") and (text[i-3]["lemma"]=="être")):
                                text[i-3]["isProp"]=" "
                                text[i-3]["rule"]="102"
                        if ((text[i-5]["lemma"]=="ce") and (text[i-4]["lemma"]=="être")):
                                text[i-4]["isProp"]=" "
                                text[i-4]["rule"]="102"

          
                # 200 Etiquetage basique des propositions
                # Les tags correspondant à des propositions sont marqués comme propositions
                # KON,NUM,DET*,PRP*,ADJ,PRO:POS,PRO:IND,ADV,VER*,PRO:REL
                if (tagger=="treetagger" and isTreetaggerPropTag(text[i]["tag"])) or (tagger=="cordial" and isCordialPropTag(text[i]["tag"])):

                        text[i]["isProp"]="P"
                        text[i]["rule"]="200"

                # 054 Déterminants démonstratifs (étiquetés pronoms démonstratifs) comptés comme proposition
                # "cet", "cette", "ces" -> comptés comme proposition
                # "ça" pas compté comme proposition
                # celle, celui, ceux ?
                # CHECK déf densité d'idées
                # CHECK 
                if (tagger=="treetagger" and text[i]["lemma"]=="ce" and text[i]["tag"]!="PRO:DEM") :
                        text[i]["isProp"]="P"
                        text[i]["rule"]="054"
                if (text[i]["word"]=="cet" or text[i]["word"]=="cette" or text[i]["word"]=="ces") :
                        text[i]["isProp"]="P"
                        text[i]["rule"]="054"
                if (tagger=="treetagger" and text[i]["word"]=="Ca") :
                        text[i]["isProp"]=" "
                        text[i]["rule"]="054"
                if (tagger=="treetagger" and (text[i-1]["lemma"]=="celui") and (text[i]["lemma"]=="là" or text[i]["lemma"]=="ci")) :
                        text[i]["isProp"]=" "
                        text[i]["rule"]="054"
                          
                # 201 Déterminants non propositions
                # lemme = "un" ou "le" ou "du" => pas proposition
                # Attention à "du" = "de le", voir règle 202
                # CHECK liste de déterminants qui ne sont pas propositions
                if (((text[i]["lemma"]=="un" or text[i]["lemma"]=="le" or text[i]["lemma"]=="du"))):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="201"

                # 202 Complément du nom introduit par "du"
                # NOM du NOM => "du" est une proposition
                if (tagger=="treetagger" and (text[i-1]["lemma"]=="du" and text[i]["tag"]=="NOM" and (text[i-2]["tag"]=="ADJ" or text[i-2]["tag"]=="NOM" or (text[i-3]["tag"]=="NOM" and text[i-2]["tag"]=="ADJ")))):
                        text[i-1]["isProp"]="P"
                        text[i-1]["rule"]="202"
                
                # 203 Soit soit
                # soit + 1 à 3 mots + soit : seul le premier "soit" est compré comme proposition
                if (text[i-2]["word"]=="soit" or text[i-3]["word"]=="soit" or text[i-4]["word"]=="soit") and text[i]["word"]=="soit":
                        text[i]["isProp"]=" "
                        text[i]["rule"]="203"
                
                # 204
                # !Conjonctions "ou" ou "et" superflues avant adverbe
                # adverbes après "et" : "puis", "alors", "donc", "ensuite", "finalement" => "et" pas proposition
                # adverbes après "ou" : "alors" "bien" => "ou" pas proposition
                # CHECK à compléter
                if (tagger=="treetagger" and ((text[i]["lemma"]=="puis" or text[i]["lemma"]=="alors" or text[i]["lemma"]=="donc" or text[i]["lemma"]=="ensuite" or text[i]["lemma"]=="finalement") and  text[i-1]["lemma"]=="et")):
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-1]["rule"]="204"
                        text[i]["rule"]="204"
                if (tagger=="treetagger" and ((text[i]["lemma"]=="bien" or text[i]["lemma"]=="alors") and  text[i-1]["lemma"]=="ou")):
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-1]["rule"]="204"
                        text[i]["rule"]="204"
                
                
                # 205
                # !Verbe intransitif
                # pas compter "à" et "de" comme une proposition
                # CHECK étiquetage treetagger des verbes intransitifs ? Non
                

                # 206 "de" non proposition
                # "de" n'est pas proposition après "falloir", "agir", "arriver", "paraître"
                if text[i]["lemma"]=="de" and (text[i-1]["lemma"]=="agir" or text[i-1]["lemma"]=="arriver" or text[i-1]["lemma"]=="falloir" or text[i-1]["lemma"]=="paraître"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"
                if text[i]["lemma"]=="de" and (text[i-1]["word"]=="envie" or text[i-1]["word"]=="lieu" or text[i-1]["word"]=="pitié" or text[i-1]["word"]=="soin") and (text[i-2]["lemma"]=="avoir" or text[i-3]["lemma"]=="avoir"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"
                if text[i]["lemma"]=="de" and (text[i-1]["lemma"]=="près" or text[i-1]["lemma"]=="auprès"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"
                if text[i]["lemma"]=="de" and (text[i-1]["lemma"]=="beaucoup" or text[i-1]["lemma"]=="plein" or text[i-1]["lemma"]=="énormément"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"
                if text[i-2]["word"]=="à" and (text[i-1]["word"]=="côté" and text[i]["lemma"]=="de"): 
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"
                if text[i-2]["word"]=="en" and (text[i-1]["word"]=="face" and text[i]["lemma"]=="de"): 
                        text[i]["isProp"]=" "
                        text[i]["rule"]="206"    


                # 207 "que" non proposition
                # "que" n'est pas proposition après "falloir", "sembler", "arriver", "paraître"
                if text[i]["lemma"]=="que" and (text[i-1]["lemma"]=="falloir" or text[i-1]["lemma"]=="sembler" or text[i-1]["lemma"]=="arriver" or text[i-1]["lemma"]=="paraître"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="207"
                if oral==1 and (text[i-2]["word"]=="est" and text[i-1]["word"]=="vrai" and text[i]["lemma"]=="que"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="207"


                # 208 Comparatif
                # "que" n'est pas proposition après "autant", "moins", "pire", "plus"
                if text[i]["lemma"]=="que" and (text[i-1]["lemma"]=="autant" or text[i-1]["lemma"]=="plus" or text[i-1]["lemma"]=="moins") and (text[i-2]["lemma"]=="autant" or text[i-2]["lemma"]=="plus" or text[i-2]["lemma"]=="moins")  and (text[i-3]["lemma"]=="autant" or text[i-3]["lemma"]=="plus" or text[i-3]["lemma"]=="moins"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="207"

                
                                        
                # 210 Oui et non (mode oral)
                # oui et non : pas proposition
                if oral==1 and (text[i]["word"]=="oui" or text[i]["word"]=="non"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="210"
                        

                # 211 Négation
                # "aucun" "guère" "jamais" "nul" "pas" "plus" "point" "que" "rien" précédé (à distance 1, 2 ou 3) par "ne" : seul "ne" proposition
                if (tagger=="treetagger" and ((text[i]["lemma"]=="aucun"  or text[i]["word"]=="guère" or text[i]["word"]=="jamais" or text[i]["lemma"]=="nul" or text[i]["word"]=="pas" or text[i]["word"]=="plus" or text[i]["word"]=="point" or text[i]["lemma"]=="que" or text[i]["word"]=="rien") and (text[i-1]["lemma"]=="ne" or text[i-2]["lemma"]=="ne" or text[i-3]["lemma"]=="ne"))):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="211"

                        
                # 212 Négation suivie de "de"
                # "de" n'est pas une proposition si précédée par négation
                # CHECK pas du tout
                if (tagger=="treetagger" and (text[i]["lemma"]=="de" and (text[i-1]["word"]=="pas" or text[i-1]["word"]=="plus" or text[i-1]["word"]=="guère" or text[i-1]["word"]=="point" or text[i-1]["word"]=="jamais" or text[i-1]["word"]=="rien"))):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="212"


                # 213 Futur proche
                # lemme="aller" + infinitif = futur proche : aller n'est pas une proposition
                if (tagger=="treetagger" and (text[i-1]["lemma"]=="aller" and text[i]["tag"]=="VER:infi")):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="213"
                        

                # 214 Si ... alors
                # "si" + 1 à 9 mots + "alors" : ne pas compter "alors" comme proposition, seulement "si".
                if (text[i]["lemma"]=="alors" and (text[i-1]["lemma"]=="si" or text[i-2]["lemma"]=="si" or text[i-3]["lemma"]=="si" or text[i-4]["lemma"]=="si" or text[i-5]["lemma"]=="si" or text[i-6]["lemma"]=="si" or text[i-7]["lemma"]=="si" or text[i-8]["lemma"]=="si" or text[i-9]["lemma"]=="si")):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="214"


                # 301 Verbes de liaison
                # Verbe de liaison pas proposition si suivi d'un adjectif ou d'un adverbe
                if (tagger=="treetagger" and ((text[i]["tag"]=="ADJ" or (text[i]["tag"]=="ADV" and text[i]["word"]!="pas")) and isLink(text[i-1]["lemma"]))) or (tagger=="cordial" and ((text[i]["tag"][0]=="A" or text[i]["tag"][0]=="R") and isLink(text[i-1]["lemma"]))):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="301"
                #if (tagger=="treetagger" and ((text[i]["tag"]=="ADJ") and isLink(text[i-2]["lemma"]))) or (tagger=="cordial" and ((text[i]["tag"][0]=="A" or text[i]["tag"][0]=="R") and isLink(text[i-2]["lemma"]))):
                #        text[i-2]["isProp"]=" "
                #        text[i-2]["rule"]="301"
                if (text[i-2]["lemma"]=="avoir" and text[i]["lemma"]=="le" and text[i]["lemma"]=="air"):
                        text[i]["isProp"]=" "
                        text[i-1]["isProp"]=" "
                        text[i-2]["isProp"]=" "
                        text[i]["rule"]="301"
                        text[i-1]["rule"]="301"
                        text[i-2]["rule"]="301"
                                        

                # 302 Verbe être suivi d'une préposition
                # "être" non proposition si suivi d'une préposition
                if (tagger=="treetagger" and (text[i]["tag"]=="PRP" and (text[i-1]["lemma"]=="être" or text[i-1]["lemma"]=="suivre|être"))):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="302"
                if (tagger=="treetagger" and (text[i]["tag"]=="PRP" and (text[i-1]["tag"]=="ADV") and (text[i-2]["lemma"]=="être" or text[i-2]["lemma"]=="suivre|être"))):
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="302"
                        


                # 402 Auxiliaire
                # AUX + VERBE => une seule proposition
                if (tagger=="treetagger" and (re.search("^VER.*",text[i]["tag"]) and re.search("^VER:aux.*",text[i-1]["tag"]))):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="402"
                if (tagger=="cordial" and text[i]["tag"][0]=="V" and text[i]["tag"][1]=="a"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="402"


                # 405 Auxiliaire avec mot interposé
                # AUX + mot + VERBE => une seule proposition
                # check : AUX + 2 mots + verbe
                if (tagger=="treetagger" and (re.search("^VER.*",text[i]["tag"]) and re.search("^VER:aux.*",text[i-2]["tag"]))):
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="405"


                # 500 Passif
                # participe passé + "par" => "par" non proposition
                if (tagger=="treetagger" and (text[i-1]["tag"]=="VER:pper" and text[i]["word"]=="par")):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="500"
                

                # 509 "à" + infinitif
                # "à" + infinitif => "à" non proposition
                if (tagger=="treetagger" and (text[i]["tag"]=="VER:infi" and text[i-1]["word"]=="à")):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="509"
                        
                        
                # 510 Gérondif
                # "en" + "participe présent" => "en" non proposition
                if (tagger=="treetagger" and (text[i]["tag"]=="VER:ppre" and text[i-1]["word"]=="en")):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="510"
                

                # 512 Verbes suivis d'une préposition naturelle
                # "à" non prop si précédé de aller, voyager ... CHECK corpus
                # "de" non prop si précédé de venir
                if (tagger=="treetagger" and (text[i-1]["lemma"]=="aller" or text[i-1]["lemma"]=="sortir" or text[i-1]["lemma"]=="rentrer" or text[i-1]["lemma"]=="entrer" or text[i-1]["lemma"]=="rendre") and (text[i]["word"]=="à" or text[i]["word"]=="au")):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="512"
                if (tagger=="treetagger" and (text[i-1]["lemma"]=="arriver" or text[i-1]["lemma"]=="entrer" or text[i-1]["lemma"]=="rentrer" or text[i-1]["lemma"]=="revenir" or text[i-1]["lemma"]=="venir") and text[i]["lemma"]=="de"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="512"
                        

                # 600 Marqueurs discursifs
                # expressions qui ne sont pas proposition
                # je crois bien
                # comment te dirais-je ?/ comment je vous dirais-je ?,  je dirais, direais-je, comment je pourrais dire, comme on dit, comme qui dirait, dit-on, je te dis/ je vous dis, si on peut dire/ si je puis dire, tu m?en diras tant, dis-moi donc, tu me dis pas/ vous me dites pas/ dis-moi pas/ dites-moi pas, je dis pas, c?est ben pour dire, cela va sans dire, c?est le cas de le dire, à qui le dis-tu/ à qui le dites-vous, c?est tout dire, c?est le cas de le dire, à qui le dis-tu/ à qui le dites-vous, c?est tout dire, ce n?est pas peu dire, c?est moi qui te le dis, c?est moi qui vous le dis, il n?y a pas à dire
                # Entendre : entendons-nous, s?entend, tu entend/ vous m?entendez, entends-tu/ m?entendez-vous, ce qu?il faut pas entendre/ qu?est-ce qu?il faut pas entendre
                # Falloir : il s?en faut, tant s?en faut
                # Faire : fais-toi-z-en pas/ faites-vous-z-en pas
                # Inquiéter : inquiète-toi pas/ inquiétez-vous pas
                #  mets-en/ mettez-en 
                # Paraître : paraît-il, il paraît, à ce qu?il paraît 
                # Parler : tu parles, parle-moi de/ parlez-moi de, parle-moi-z-en pas/ parlez-moi-z-en pas, parlons-en
                # Pense-z-y pas/ pensez-y pas
                # regarde-moi ça/ regardez-moi ça, regarde donc
                # CHECK 
                
                # or text[i]["word"]=="va" or text[i]["word"]=="dis"
                if oral==1 and (text[i]["word"]=="admettons" or text[i]["word"]=="allez" or text[i]["word"]=="allons" or text[i]["word"]=="attends" or text[i]["word"]=="attendez" or text[i]["word"]=="comprenez" or text[i]["word"]=="disons" or text[i]["word"]=="écoute" or text[i]["word"]=="écoutez" or text[i]["word"]=="mettons" or text[i]["word"]=="mettez" or text[i]["word"]=="regarde" or text[i]["word"]=="regardez" or text[i]["word"]=="voyons" or text[i]["word"]=="enfin" or text[i]["word"]=="voilà"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="600"
                if oral==1 and ((text[i-1]["word"]=="va" and text[i]["word"]=="donc") or (text[i-1]["word"]=="ça" and text[i]["word"]=="va") or (text[i-1]["word"]=="attends" and text[i]["word"]=="voir") or (text[i-1]["word"]=="attendez" and text[i]["word"]=="voir") or (text[i-1]["word"]=="tu" and text[i]["word"]=="comprends") or (text[i-1]["word"]=="vous" and text[i]["word"]=="comprenez") or (text[i-1]["word"]=="comprends" and text[i]["word"]=="tu") or (text[i-1]["word"]=="comprenez" and text[i]["word"]=="vous") or (text[i-1]["word"]=="dis" and text[i]["word"]=="donc") or (text[i-1]["word"]=="tu" and text[i]["word"]=="vois") or (text[i-1]["word"]=="vous" and text[i]["word"]=="voyez") or (text[i-1]["word"]=="figure" and text[i]["word"]=="toi") or (text[i-1]["word"]=="figurez" and text[i]["word"]=="vous") or (text[i-1]["word"]=="je" and text[i]["word"]=="imagine")):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="600"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="600"
                        
                        
                # 601 bien comme marqueur discursif
                # "bien" n'est alors pas proposition
                if oral==1 and text[i]["word"]=="bien" and (text[i-1]["lemma"]=="penser" or text[i-1]["lemma"]=="regarder" or text[i-1]["lemma"]=="écouter" or text[i-1]["lemma"]=="voir"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="601"
                
                # 602 donc comme marqueur discursif
                # "donc" n'est alors pas proposition
                if oral==1 and text[i]["word"]=="donc" and (text[i-1]["lemma"]=="dire" or text[i-1]["lemma"]=="comprendre" or text[i-1]["lemma"]=="aller"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="602"                        
                
                # Expressions à vérifier (compter une seule fois) : à moins que, à côté de, tout à coup, tout de suite
                
                                
                # 634
                # "figurez-vous que" "vous voyez" -> 1 mot 0 prop dans CPIDR
                # CHECK trouver les marqueurs du discours -> "dis donc", "écoutez", "écoute", "voyons", "tiens", "mettons", "admettons", "disons", "réfléchissons", "figure-toi", "comment dirais-je"
                
                # 701 Mots composés
                # Compter comme une seule proposition
                # copule -> "passer pour"
                # adverbe -> "tout à coup", "tout de suite", "de temps en temps", "par ailleurs", "par conséquent", "tout de même", "par contre", "par bonheur", "par malheur"
                # causalité -> "parce que"
                # location -> "à côté de", "en face de"
                if text[i-1]["word"]=="bien" and text[i]["word"]=="sûr":
                        text[i-1]["isProp"]="P"
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if text[i-1]["word"]=="bien" and text[i]["word"]=="sûr":
                        text[i-1]["isProp"]="P"
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if ((text[i-1]["word"]=="de") or (text[i-1]["word"]=="en")) and text[i]["word"]=="plus":
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"
                if text[i-1]["lemma"]=="parce" and text[i]["word"]=="que":
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"
                if text[i-1]["lemma"]=="tant" and (text[i]["word"]=="pis" or text[i]["word"]=="mieux"):
                        text[i-1]["isProp"]="P"
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if text[i-2]["lemma"]=="passer" and (text[i-1]["word"]=="pour" and text[i]["tag"]=="NOM"):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701" 
                if (text[i-2]["lemma"]=="petit" and text[i-1]["lemma"]=="à" and text[i]["lemma"]=="petit"):
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="701" 
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701" 
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"
                if text[i-1]["word"]=="tout" and (text[i]["word"]=="à" or text[i]["word"]=="de"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if text[i-1]["word"]=="quand" and ((text[i]["word"]=="-même") or (text[i]["word"]=="même")):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if text[i-1]["lemma"]=="entre" and (text[i]["lemma"]=="autre"):
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if text[i-2]["word"]=="tout" and (text[i-1]["word"]=="de" and text[i]["word"]=="même"):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701" 
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701" 
                if text[i-2]["word"]=="à" and text[i-1]["word"]=="peu" and text[i]["word"]=="près":
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="701" 
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701" 
                if (text[i-1]["word"]=="alors" or text[i-1]["word"]=="bien" or text[i-1]["word"]=="dès" or text[i-1]["word"]=="pendant") and (text[i]["lemma"]=="que"): 
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"
                if (((text[i-2]["word"]=="du" and text[i-1]["word"]=="fait") or (text[i-2]["word"]=="en" and text[i-1]["word"]=="tant")) and text[i]["lemma"]=="que"): 
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="701"
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"
                if (text[i-3]["word"]=="vis" and text[i-2]["word"]=="à" and text[i-1]["word"]=="vis" and text[i]["lemma"]=="de"): 
                        text[i-3]["isProp"]=" "
                        text[i-3]["isWord"]=" "
                        text[i-3]["rule"]="701"
                        text[i-2]["isProp"]=" "
                        text[i-2]["isWord"]=" "
                        text[i-2]["rule"]="701"
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"                        
                if (text[i-3]["word"]=="de" and text[i-2]["word"]=="temps" and text[i-1]["word"]=="en" and text[i]["lemma"]=="temps"): 
                        text[i-3]["isProp"]="P"
                        text[i-3]["rule"]="701"
                        text[i-2]["isProp"]=" "
                        text[i-2]["rule"]="701"
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]=" "
                        text[i]["rule"]="701"                        
                if (text[i-1]["word"]=="vis-à-vis" and text[i]["lemma"]=="de"): 
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="701"
                        text[i]["isProp"]="P"
                        text[i]["rule"]="701"                        
                                        
                # 702 Mots composés avec "par"
                # expressions qui ne correspondent qu'à une seule proposition
                if text[i-1]["word"]=="par" and (text[i]["word"]=="ailleurs" or text[i]["word"]=="après" or text[i]["word"]=="avance" or text[i]["word"]=="bonheur" or text[i]["word"]=="chance" or text[i]["word"]=="conséquent" or text[i]["word"]=="contre" or text[i]["word"]=="derrière" or text[i]["word"]=="ici" or text[i]["word"]=="là" or text[i]["word"]=="là-bas" or text[i]["word"]=="malheur" or text[i]["word"]=="suite"):
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-1]["rule"]="702"
                        text[i]["rule"]="702"
                if (text[i-1]["word"]=="de" and text[i]["word"]=="par"):
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-1]["rule"]="702"
                        text[i]["rule"]="702"
                if (text[i-2]["word"]=="par" and (text[i-1]["word"]=="rapport" and text[i]["word"]=="à") or (text[i-1]["word"]=="la" and text[i]["word"]=="suite")):
                        text[i-2]["isProp"]=" "
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-2]["rule"]="702"
                        text[i-1]["rule"]="702"
                        text[i]["rule"]="702"

                # 703 Mots composés avec "avoir"
                # expressions qui ne correspondent qu'à une seule proposition
                if text[i-2]["lemma"]=="en" and text[i-1]["lemma"]=="avoir" and (text[i]["word"]=="après" or text[i]["word"]=="contre"):
                        text[i-2]["isProp"]=" "
                        text[i-1]["isProp"]=" "
                        text[i]["isProp"]="P"
                        text[i-2]["rule"]="703"
                        text[i-1]["rule"]="703"
                        text[i]["rule"]="703"
                        
                
                if oral==1 and mode=="noprop":
                        text[i]["isProp"]=" "
                        
                if oral==1 and mode=="noword":
                        text[i]["isProp"]=" "
                        text[i]["isWord"]=" "


                        
                i+=1

        # Display information about the words
        nbProps=0
        nbWords=0
        bilanRegles={}
        i=0
        while i < len(text):
                item=text[i]
                if item["isWord"]=="W":
                        nbWords+=1;
                if item["isProp"]=="P":
                        nbProps+=1;
                tag=item["tag"]
                while len(tag)<12:
                       tag=tag+" "
                if bilanRegles.has_key(item["rule"]):
                       bilanRegles[item["rule"]]+=1
                else:
                       bilanRegles[item["rule"]]=1
                
                output.writelines(item["rule"]+" "+tag+" "+item["isWord"]+" "+item["isProp"]+" "+item["word"]+"\n")
                print item["rule"],tag,item["isWord"],item["isProp"],item["word"]
                i+=1

        # Display final information
        print nbWords,"mots."
        output.writelines("\n"+str(nbWords)+" mots.\n")
        print nbProps,"propositions."
        output.writelines(str(nbProps)+" propositions.\n")
        print "Densite des idees :",round((nbProps+0.00000001)/(nbWords+0.00000001),4)
        output.writelines("Densité des idées : "+str(round((nbProps+0.00000001)/(nbWords+0.00000001),4))+"\n")
        numRegles=bilanRegles.keys();
        numRegles.sort()
        for item in numRegles:
                output.writelines(str(bilanRegles[item])+" fois la règle "+item+"\n")
                print (str(bilanRegles[item])+" fois la regle "+item)
        output.close()
else:
        if thefile=="help":
                print ""
                print "==== HELP ON DENSIDEES ===="
                print "densidees [options] <filename>"
                print ""
                print "<filename> contains an output file from the French TreeTagger"
                print "(or a CNR file output by Cordial if you use option tag=cordial)."
                print "Use for example the online version of TreeTagger on"
                print "http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php"                
                print ""
                print "***OPTIONS:***"
                print ""
                print "oral=1: to activate speech mode"
                print ""
                print "tag=<tagger> where <tagger> is treetagger or cordial:"
                print "  to choose the POS-tagger"
                print "  !! the Cordial rules are in beta version"

        else:   
                
                print filename," - file does not exist!"
                print "Please use option help to display the possible parameters."

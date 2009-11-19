#!/usr/sfw/bin/python
# -*- coding: iso-8859-15 -*-
#C:\Python26\Python.exe C:\These\2009Densidees\densidees\Densidees.py C:\These\2009Densidees\densidees\Test.txt

#####################################################
# Copyright 2009 Philippe Gambette
# 
# This file is part of Densidees v1.0 (19/11/2009).
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
#####################################################


import sys, os, re, string, time
from DensideesFunctions import *
from math import *



#------------------------------
# analyze and load parameters
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

if not(args.has_key("parameter")):
        args["parameter"]=0
parameter=int(args["parameter"]);



def isPropTag(tag):
        result=0
        if tag=="KON" or tag=="NUM":
                result=1
        if re.search("^DET.*",tag):
                result=1        
        if re.search("^PRP.*",tag):
                result=1        
        if tag=="ADJ" or tag=="PRO:POS" or tag=="PRO:IND" or tag=="ADV":
                result=1
        if re.search("^VER.*",tag):
                result=1
        if tag=="PRO:REL":
                result=1
        return result

def isLink(lemma):
        result=0
        if re.search("^|être.*",lemma):
                result=1
        if lemma=="sembler" or lemma=="devenir":
                result=1
        return result

if os.path.isfile(thefile):
        print "Chargement du fichier texte..."
        
        # Open the text
        text=openText(thefile)
        i=0
        
        # Treat each word of the text
        while i < len(text):
                                
                # Preprocess tags
                if text[i]["tag"]=="PUN" or text[i]["tag"]=="SEN":
                        text[i]["tag"]="SYM"
                                
                # 002
                # The item is a word if its token starts with a letter or digit
                # and its tag is not SYM (symbol).
                if re.search("^[a-zA-Zéèçàùêîôûäëïöü]",text[i]["word"]) and text[i]["tag"]!="SYM":
                        text[i]["isWord"]="W"
                        text[i]["rule"]="002"
                
                # 003
                # Two cardinal numbers in immediate succession are combined into one
                # (Uncommon situation; the next one is much more common)
                if text[i-1]["tag"]=="NUM" and text[i]["tag"]=="NUM":
                        i=i-1
                        text[i]["word"]=text[i]["word"]+" "+text[i+1]["word"]
                        text[i]["rule"]="003"
                        del text[i+1]

                # 200
                # The tags which correspond to propositions are taken to indicate propositions.
                if isPropTag(text[i]["tag"]):
                        text[i]["isProp"]="P"
                        text[i]["rule"]="200"

                # 201
                # The tags which correspond to propositions are taken to indicate propositions.
                if text[i]["word"].lower()=="un" or text[i]["word"].lower()=="une" or text[i]["word"].lower()=="le" or text[i]["word"].lower()=="la" or text[i]["word"].lower()=="des" or text[i]["word"].lower()=="les" or text[i]["word"].lower()=="l":
                        text[i]["isProp"]=" "
                        text[i]["rule"]="201"

                # 301
                # Linking verb is not a proposition if followed by adj. or adv.
                if (text[i]["tag"]=="ADJ" or text[i]["tag"]=="ADV") and isLink(text[i-1]["lemma"]):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="301"

                # 302
                # "Be" is not a proposition when followed by a preposition.
                # (May want to modify this to allow an intervening adverb.)
                if text[i]["tag"]=="PRP" and re.search("^.*être.*",text[i-1]["lemma"]):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="302"

                # 402
                # Aux Verb is one proposition, not two
                if re.search("^VER.*",text[i]["tag"]) and re.search("^VER:aux.*",text[i-1]["tag"]):
                        text[i-1]["isProp"]=" "
                        text[i-1]["rule"]="402"

                i+=1

        # Display information about the words
        nbWords=0
        nbProps=0
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
                print item["rule"],tag,item["isWord"],item["isProp"],item["word"]
                i+=1

        # Display final information
        print nbWords,"mots."
        print nbProps,"propositions."
        print "Densite d'idees :",round((nbProps+0.00000001)/(nbWords+0.00000001),4)
else:
        if re.search("help",thefile):
                print ""
                print "==== HELP ON DENSIDEES ===="
                print "densidees [options] <filename>"
                print ""
                print "<filename> contains an output file from the French TreeTagger."
                print "For example the online version on"
                print "http://www.cele.nottingham.ac.uk/~ccztk/treetagger.php"                
                print ""
                print "***OPTIONS:***"
                print ""
                print "No options yet"

        else:   
                
                print filename," - file does not exist!"
                print "Please use option help to display the possible parameters."
                
                
                
                


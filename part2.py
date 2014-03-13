#Document Tagger Part 2!
#Welcome back kiddies. This time we will be parsing through the metadata of 15 documents extracted from our beloved
#Project Gutenberg. Unlike last time however, we will be using the os.listdir() function. This will iterate between 
#our directory with the files stored in it and bring back the Title, Author, Illustrator & Translator for each file. It will
#also display any keywords required.

import sys
import os
import re

directory = "c:/python27/projects/document_tagger/part2"


# Below are the keywords we will be searching for

keywords = ["up", "down", "happy", "sad", "sun", "moon", "Earth"]
kws =  {kw: re.compile(r'\b' + kw + r'\b') for kw in keywords[2:]}
 
title_search = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
 
for fl in (os.listdir(directory)): 
    if fl.endswith('.txt'):       
        fl_path = os.path.join(directory, fl)
        with open(fl_path, 'r') as f:
            full_text = f.read()
        author = re.search(author_search, full_text)
        if author:
            author = author.group('author')
        translator = re.search(translator_search, full_text)
        if translator:
            translator = translator.group('translator')
        illustrator = re.search(illustrator_search, full_text)
        if illustrator:
            illustrator = illustrator.group('illustrator')
        title = re.search(title_search, full_text).group('title')
        print "***" * 25
        print "Here's the info for {}:".format(fl)
        print "Title:  {}".format(author)
        print "Author(s): {}".format(title)
        print "Translator(s): {}".format(translator)
        print "Illustrator(s): {}".format(illustrator)
        print "\n****KEYWORD REPORT****\n\n"
        for kw in kws:
            print "\"{0}\": {1}".format(kw, len(re.findall(kws[kw], full_text)))
        print '\n\n'

raw_input("Press any key to exit...")
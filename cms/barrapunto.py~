#!/usr/bin/python
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib

def get_barrapunto():
    class CounterHandler(ContentHandler):

        def __init__ (self):
            self.inItem = False
            self.inContent = False
            self.theContent = ""
            self.salida = "<h1><u>Barrapunto</u></h1></br>"

        def startElement (self, name, attrs):
            if name == 'item':
                self.inItem = True
            elif self.inItem:
                if name == 'title':
                    self.inContent = True
                elif name == 'link':
                    self.inContent = True
                
        def endElement (self, name):
            if name == 'item':
                self.inItem = False
            elif self.inItem:
                if name == 'title':
                    self.salida+= "<b>Titulo: </b>" + self.theContent + "."
                    self.salida+= "</br>"
                    self.inContent = False
                    self.theContent = ""
                elif name == 'link':
                    self.salida+= "<b>Link: </b>" + "<a href=" + self.theContent
                    self.salida+= ">" + self.theContent + "</a></br></br>"
                    self.inContent = False
                    self.theContent = ""

        def characters (self, chars):
            if self.inContent:
                self.theContent = self.theContent + chars
                
        
    # Load parser and driver

    theParser = make_parser()
    theHandler = CounterHandler()
    theParser.setContentHandler(theHandler)

    # Ready, set, go!

    File = urllib.urlopen("http://barrapunto.com/index.rss")
    theParser.parse(File)

    return theHandler.salida

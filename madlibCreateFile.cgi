#!/usr/bin/env python3

import cgi   

def main(): 
    form = cgi.FieldStorage()      
    madlibText = form.getfirst('formText', "")
    madlibName = form.getfirst('fileName', "default.txt")
    createUserMadlib(madlibName, madlibText)
    addToList(madlibName)
    contents = processInput()
    print(contents)
    

def createUserMadlib(name, text):
    outFile = open(name, 'w')
    outFile.write(text)
    outFile.close

def processInput():
    '''Process input parameters and return the final page as a string.'''
    return fileToStr('madlibCreateOwn.html')

def addToList(madlibName):
    '''adds the file name to a list so that can make a list of all user madlib names'''
    editFile = open('madlibList.txt', 'a')
    editFile.write(madlibName + "\n")
    editFile.close

    
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:
    print("Content-type: text/html\n\n")
    main() 
except:
    cgi.print_exception()

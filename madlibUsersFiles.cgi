#!/usr/bin/env python3

import cgi   

def main():
    form = cgi.FieldStorage()
    fileList = makeFileList('madlibList.txt')
    finalcontents = createTemplate(fileList)
    print(finalcontents)

def makeFileList(listFile):
    lines = [line.rstrip('\n') for line in open(listFile)]
    return lines

    
def createTemplate(fileList):
    '''Loop through the collection of cue keys and create a template'''
    madlibTemplate = '''<input name="files"
 value="{file}" type="radio">{file}<br>
'''
    madlibOptions = ''
    for file in fileList:
        madlibOptions +=  madlibTemplate.format(**locals())
    return fileToStr('Madlib3.html').format(**locals())
    
def processInput():  
    '''Process input parameters and return the final page as a string.'''

    return fileToStr('Madlib2.html').format(**locals())
    

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors

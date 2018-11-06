#!/usr/bin/env python3

import cgi   

def main():
    form = cgi.FieldStorage()
    userFileList = form.getlist('files')
    userFile = ''.join(userFileList)
    inFile = open(userFile, 'r')
    contents = inFile.read()    
    cues = getKeys(contents)
    finalcontents = createTemplate(cues, userFile)
    print(finalcontents)

def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set

def addPick(cue, dictionary): # from madlibDict.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    form = cgi.FieldStorage()
    response = form.getfirst(cue, cue)
    dictionary[cue] = response                                                             


def createTemplate(cues, userFile):
    '''Loop through the collection of cue keys and create a template'''
    cueTemplate = '''Enter an example for {cue} <input maxlength="30" size="30"
 name="{cue}"><br>
  <br>
'''
    cueOptions = ''
    for cue in cues:
        cueOptions +=  cueTemplate.format(**locals())
    madlibName = userFile
    return fileToStr('Madlib2.html').format(**locals())
    
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



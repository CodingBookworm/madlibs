#!/usr/bin/env python3

import cgi   

def main():
    form = cgi.FieldStorage()
    userFile = form.getfirst('pageID', 'jungle.txt')
    inFile = open(userFile, 'r')
    contents = inFile.read()    
    cues = getKeys(contents)
    userPicks = getUserPicks(cues, form)
    finalcontents = processInput(userPicks, userFile, contents)
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

def addPick(cue, dictionary, form): # from madlibDict.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    response = form.getfirst(cue, cue)
    dictionary[cue] = response                                                             


def getUserPicks(cues, form):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks, form)
    return userPicks   
    
def processInput(dictionary, userFile, contents):  
    '''Process input parameters and return the final page as a string.'''
    if userFile == 'jungle.txt':
        image = "http://blogs.discovermagazine.com/d-brief/files/2017/08/shutterstock_244338682.jpg"
    elif userFile == 'Home Alone.txt':
        image = "https://cn.pling.com/img/f/c/2/7/026c18b8da5fd20734e179b3a01a83bf3962.jpg"
    elif userFile == 'Mirror.txt':
        image = "https://images6.alphacoders.com/403/thumb-1920-403376.jpg"
    elif userFile == 'Time Travel.txt':
        image = "https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/yRF5c-O/videoblocks-infinity-clock-version-1-purple-pink-red-infinite-zoom-in-of-cosmic-clock-with-roman-numerals-abstract-time-travel-conceptual-spiral-sci-fi-fantasy-video-background_st_wk0gpg_thumbnail-full01.png"
    else:
        image = "https://images7.alphacoders.com/376/376037.jpg"
    text = contents
    title = userFile.replace('.txt', '')
    title = title.capitalize()
    page = fileToStr('madlibTemplate.html').format(**locals())
    return page.format(**dictionary)

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



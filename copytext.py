#! /usr/bin/python3
#
# @(!--#) @(#) copynpaste.py, version 001, 19-december-2021
#
# copy text to a internal clipboard "storage"
#

#################################################################

#
# imports
#

import sys
import os
import argparse
import html
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

#################################################################

def unixbasename(filename, extension):
    lenfilename = len(filename)

    lenext = len(extension)

    if lenext < lenfilename:
        if filename[-lenext:] == extension:
            filename = filename[0:lenfilename-lenext]

    return filename

#################################################################

def savetext2clipboard(text):
    global progname

    clipfilename  = unixbasename(progname, '.py') + '.clip'

    try:
        clipfile = open(clipfilename, 'w', encoding='utf-8')
    except IOError:
        return

    clipfile.write(text)

    
    clipfile.flush()

    clipfile.close()

    return
    
#################################################################

def main():
    global progname

    title = 'Copy Text'

    form = cgi.FieldStorage(encoding='utf-8')
   
    enteredtext = form.getfirst('enteredtext', '')

    copybutton = form.getfirst('copybutton', '')

    print('Content-type: text/html; charset=utf-8')
    print('')

    print('<!doctype html>')

    print('<html>')

    print('<head>');

    print('<title>{}</title>'.format(html.escape(title)))

    print('<meta charset="utf-8">')

    print('</head>');

    print('<body>')

    print('<h1>{}</h1>'.format(html.escape(title)))

    print('<p>')
    print('Enter text below and click on the "Copy" button')
    print('</p>')

    print('<form accept-charset="UTF-8" method="post" action="{}">'.format(progname))

    print('<textarea name="enteredtext" rows="24" cols="80">', end='')

    if len(enteredtext) != 0:
        print(html.escape(enteredtext), end='')

    print('</textarea>')

    print('<br>')

    print('<input type="submit" name="copybutton" value="-- Copy --">')

    print('</form>')

    if copybutton != '':
        if len(enteredtext) != 0:
            savetext2clipboard(enteredtext)

    print('<hr>')

    print('</body>')

    print('</html>')

    return 0

#################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file

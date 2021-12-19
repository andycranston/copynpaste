#! /usr/bin/python3
#
# @(!--#) @(#) pastetext.py, version 001, 19-december-2021
#
# display (paste) the text in the internal clipboard "storage" to the web page
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

def readclipboard():
    global progname

    clipfilename  = 'copytext.clip'

    try:
        clipfile = open(clipfilename, 'r', encoding='utf-8')
    except IOError:
        return ''

    text = clipfile.read()

    clipfile.close()

    return text
    
#################################################################

def main():
    global progname

    title = 'Paste Text'

    form = cgi.FieldStorage(encoding='utf-8')
   
    pastebutton = form.getfirst('pastebutton', '')

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
    print('Click the "Paste" button')
    print('</p>')

    print('<form accept-charset="UTF-8" method="post" action="{}">'.format(progname))

    print('<textarea name="enteredtext" rows="24" cols="80">', end='')

    if pastebutton != '':
        text = html.escape(readclipboard())

        if len(text) != '':
            print('{}'.format(text), end='')

    print('</textarea>')

    print('<br>')

    print('<input type="submit" name="pastebutton" value="  ----  Paste  ----  ">')

    print('</form>')

    print('<hr>')

    print('</body>')

    print('</html>')

    return 0

#################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file

#! /bin/bash

PATH=/bin:/usr/bin
export PATH

progname=`basename $0`

if [ "$CGIBIN" == '' ]
then
  echo "$progname: CGIBIN needs to set to the cgi-bin directory of the web server" 1>&2
  exit 1
fi

if [ ! -d $CGIBIN ]
then
  echo "$progname: CGIBIN is \"$CGIBIN\" does not exist or is not a directory" 1>&2
  exit 1
fi

if [ ! -d $CGIBIN ]
then
  echo "$progname: CGIBIN is \"$CGIBIN\" is not writable" 1>&2
  exit 1
fi

SCRIPTS="copytext.py pastetext.py"

cp -p $SCRIPTS $CGIBIN

if [ $? -ne 0 ]
then
  echo "$progname: problem copying scripts to \"$CGIBIN\" - see previous error(s)" 1>&2
  exit 1
fi

for script in $SCRIPTS
do
  chmod a+rx $CGIBIN/$script

  if [ $? -ne 0 ]
  then
    echo "$progname: problem changing mode on script \"$CGIBIN/$script\" - see previous error(s)" 1>&2
    exit 1
  fi
done

exit 0

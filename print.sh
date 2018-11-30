#!/bin/bash
# this is a only intended boot the generated pdfs into the UC printers
# it is not particularly resilient and should be treated with skepticism

# The user is expected to provide a dir of files that will be all printed

for file in $1/*.pdf; do
    lpr -o StapleLocation=UpperLeft "$file"
done

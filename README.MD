## Programs Use
Will take a document and print it the given number of times, each with instance with a unique identifier.
This was created to unambiguously identify students exams as all the pages must be separated during scanning.

## Use
````bash
python3 id_testpaper.py paper_to_print.pdf number_to_print
````
It can be useful to print another set, but to avoid colissions you provide a third argument, the total printed so far.

## Dependancy's
* Python3
* pdfTeX: 
Generates the page that overlays the document to be printed
* pdftk: 
Overlays pages of the file to be printed and the UID page

## Note of Shame
There is an ugly snipit of bash in print.sh that sends off the files in .build/pdf to be printed. It should work out of the box for any CSSE staff that are sending jobs to the resource room, but I imagine that this is all very spesific to that set of printers. 

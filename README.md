# AVT-Wikipedia
Scripts to select untranslated Wikipedia pages and create translation projects in XLIFF format.

## Data files

To run the scripts you need to download the following files with data. They are gzip compressed text files. You don't need to decompress them, as the scripts read directly the compressed files. Later on this tutorial, you'll learn how to create these files.

* http://lpg.uoc.edu/AVT-Wikipedia/CategoryRelations.txt.gz
* http://lpg.uoc.edu/AVT-Wikipedia/enwiki-info-ll.txt.gz


## 1st step: Create the list of pages to translate

Use the script 

For example:

python3 createToTranslate.py "Depression (psychology)" 2 Featured,Good,Refular es 5 5000 totranslate-depression-eng-spa.txt

Will create the list of Englis Wikipedia pages of Endocrinology (and 2 levels under it) untranslated into Spanish, that are already in 5 other languages with a minimum length of 5000 characters. The pages to translate will be stored in the file totranslate-endocrinology-eng-spa.txt 

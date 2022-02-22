# AVT-Wikipedia
Scripts to select untranslated Wikipedia pages and create translation projects in XLIFF format.

## 1st step: Create the list of pages to translate

Use the script 

For example:

python3 createToTranslate.py Endocrinology 2 Featured,Good,Refular es 5 5000 totranslate-endocrinology-eng-spa.txt

Will create the list of Englis Wikipedia pages of Endocrinology (and 2 levels under it) untranslated into Spanish, that are already in 5 other languages with a minimum length of 5000 characters. The pages to translate will be stored in the file totranslate-endocrinology-eng-spa.txt 

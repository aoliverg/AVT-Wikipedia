# AVT-Wikipedia

Scripts to select untranslated Wikipedia pages and create translation projects in XLIFF format. The scripts works under Linux terminal (WSL in Windows can be used).

## Data files

To run the scripts you need to download the following files with data. They are gzip compressed text files. You don't need to decompress them, as the scripts read directly the compressed files. Later on this tutorial, you'll learn how to create these files.

* http://lpg.uoc.edu/AVT-Wikipedia/CategoryRelations.txt.gz
* http://lpg.uoc.edu/AVT-Wikipedia/enwiki-info-ll.txt.gz


## 1st step: Create the list of articles to translate

Use the script 

For example:

python3 createToTranslate.py Endocrinology 2 Featured,Good,Regular es 5 5000 totranslate-endocrinology-eng-spa.txt

Will create the list of Englis Wikipedia pages of Endocrinology (and 2 levels under it) untranslated into Spanish, that are already in 5 other languages with a minimum length of 5000 characters. The pages to translate will be stored in the file totranslate-endocrinology-eng-spa.txt 

## 2nd step: Download the text of the selected articles

We create a directory to store the files:

mkdir wikipedia-endicronology-eng-spa

And download the texts using the getArticleText.py script, indicating the list of articles created in step 1 and the directory:

python3 getArticleTexts.py totranslate-endocrinology-eng-spa.txt wikipedia-endicronology-eng-spa/

During the download process the titles of the articles is shown:

TITLE: Protein phosphatase
TITLE: 5α-Reductase 2 deficiency
TITLE: Congenital hypothyroidism
...

## 3rd step: Crete the script for tikal

For this step, tikal, one component of the Okapi Tools project should be installed in the system. To download and install tikal follow these steps:

* Download the binaries for your operating system from: https://okapiframework.org/binaries/main/1.42.0/
* Unzip the file in a convenient directory (remember the path to the directory).

The to create the script for TRAnslation projects, script createScriptTikal-TRAD.py is used. The parameters are: the directory where the article texts are located, the source language, the target language and the directory there tikal is located. We run the script:

python3 createScriptTikal-TRAD.py ./wikipedia-endicronology-eng-spa/ en es ./okapi/

Ans the processTRAD.sh bash script contains all the commands to create the XLIFF with tikal:

./okapi//tikal.sh -x -sl en -tl es -seg segment.srx -nocopy ./wikipedia-endicronology-eng-spa/14-3-3_protein-en.txt
./okapi//tikal.sh -x -sl en -tl es -seg segment.srx -nocopy ./wikipedia-endicronology-eng-spa/1D-chiro-Inositol-en.txt
....

We should give execution permissions to the processTRAD.sh script:

chmod +x processTRAD.sh

And run the script:
./processTRAD.sh

The XLIFF files will be created in the same directory.

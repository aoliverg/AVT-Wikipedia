import wikipedia
import sys
import codecs


filetotranslate=sys.argv[1]
directory=sys.argv[2]

entrada=codecs.open(filetotranslate,"r",encoding="utf-8")

for linia in entrada:
    if not linia.startswith("#"):
        linia=linia.rstrip()
        camps=linia.split("\t")
        title=camps[1]
        print("TITLE:",title)
        lang="en"
        try:
            wikipedia.set_lang(lang)
            page = wikipedia.page(title)
            fsortida="./"+directory+"/"+title.replace(" ","_").replace("'","").replace("(","").replace(")","")+"-"+lang+".txt"
            sortida=codecs.open(fsortida,"w",encoding="utf-8")
            sortida.write(page.content+"\n")
        except:
            pass




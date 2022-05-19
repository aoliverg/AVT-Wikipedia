import sys
import codecs
import os

sortida=codecs.open("processPED.sh","w",encoding="utf-8")
path=sys.argv[1]
sl=sys.argv[2]
tl=sys.argv[3]
tikalpath=sys.argv[4]

llista=os.listdir(path)
llista.sort()
for f in llista:
    if path.endswith("/"):
        ff=path+f
    else:
        ff=path+"/"+f
    ffout="".join(ff.split(".")[:-1])+".xlf"
    print(ff)
    print(ffout)
    cadena=tikalpath+"/tikal.sh -x -sl "+sl+" -tl "+tl+" -seg segment.srx "+ff+" -mmt http://192.168.1.45:8000"
    print(cadena)
    sortida.write(cadena+"\n")
  
    
    

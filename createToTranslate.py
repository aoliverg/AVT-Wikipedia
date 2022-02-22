#    createToTranslate
#    Copyright (C) 2022  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import codecs
import sys
import gzip

print(sys.argv)
category=sys.argv[1]
level=int(sys.argv[2])
qualityD=sys.argv[3].split(",") #Featured,Good,Regular
lang=sys.argv[4]
minlangs=int(sys.argv[5])
minlength=int(sys.argv[6])
outfile=sys.argv[7]

relation={}
tempCategories=[]
selectedCategories=[]
entrada=gzip.open("CategoryRelations.txt.gz", 'rb')
for linia in entrada:
    linia=linia.decode().rstrip()
    camps=linia.split("\t")
    try:
        if not camps[0] in relation:
            relation[camps[0]]=[camps[1]]
        else:
            relation[camps[0]].append(camps[1])
    except:
        pass

selectedCategories.extend(relation[category])
tempCategories.extend(relation[category])


for i in range(level-1):
    temp=[]
    for cat in tempCategories:
        if cat in relation: temp.extend(relation[cat])
    temp=list(set(temp))
    tempCategories=temp
    selectedCategories.extend(temp)


selectedCategories=list(set(selectedCategories))
print("Total categories",len(selectedCategories))

entrada=gzip.open("enwiki-info-ll.txt.gz", 'rb')
sortida=codecs.open(outfile,"w",encoding="utf-8")
cadena="#"+str(sys.argv)
sortida.write(cadena+"\n")
for linia in entrada:
    try:
        linia=linia.decode().rstrip()
        camps=linia.split("\t")
        
        id=camps[0]
        title=camps[1]
        quality=camps[2]
        length=int(camps[3])
        subjects=eval(camps[4])
        langs=eval(camps[5])
        
        commonCategories=list(set(selectedCategories).intersection(set(subjects)))
                
        if not lang in langs and len(langs)>=minlangs and length>=minlength and len(commonCategories)>=1 and quality in qualityD:
            
            print(linia)
            sortida.write(linia+"\n")
    except:
        print("ERROR:",sys.exc_info(),linia)
        print(camps)

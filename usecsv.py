import csv, re

def opencsv(filename):
    f = open(filename, 'r', encoding='cp949')
    n = csv.reader(f)
    return list(n)

def writecsv(filename, data):
    f = open(filename,'w', newline='', encoding='cp949')
    n = csv.writer(f)
    n.writerows(data)
    f.close()

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listName


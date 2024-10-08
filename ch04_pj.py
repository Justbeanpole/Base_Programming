import usecsv, re



total = usecsv.opencsv('20240411.csv')

newlst = []
for i in total:
    newlst.append([i[1], i[6], i[9]])

newlst = switch(newlst)

resultlst = []
for j in newlst:
    try:
        if j[1] >= 70 and j[2] >= 50000:
            resultlst.append(j)
    except:
        resultlst.append(j)

usecsv.writecsv('new.csv', resultlst)
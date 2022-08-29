import csv
import os
from pathlib import Path
import time


#CHANGE BELOW TO THE PATH TO THE FOLDER OF VOTER INFO FILE(S) U DOWNLOADED
os.chdir(r'C:\Users\path\voter\folder_name')
dir=Path.cwd()

#CHANGE BELOW TO THE PATH + WHATEVER YOU WANT TO CALL THE SUMMARY DATAFILE. YOU DON'T NEED TO CREATE THIS AHEAD OF TIME IT WILL DO IT AUTOMATICALLY :)
nf=Path(r'C:\Users\path\to\voting\newdataset.csv')



#---------DONT MODIFY PAST THIS POINT

vfiles=list(Path(dir).rglob('*.csv'))

fieldnames1=['County', 'Democratic', 'Republican', 'Other_not_unaf',
             'Libertarian', 'Unaffiliated', 'White', 'Black' , 'Asian',
             'American_indian', 'Other', 'Hispanic/Latino', 'Not_Hispanic/Latino', 'Male', 'Female', 'Total']
fieldnames_1=list(fieldnames1)
fieldnames2=list(range(0,80))


def hr(fieldnames_1, nf):
    with open(nf, "a+", encoding='UTF-8', newline="") as h:
        hwrite=csv.DictWriter(h, fieldnames=fieldnames_1)
        hwrite.writeheader()
        pass


def pr(fieldnames_1, nf, a1, t1, a2, a3, a5, a6,
          b1, b2, b3, b4, b5,
          c1, c2, d1, d2, y2):
    #csvwriter for new files

    with open(nf, "a+", encoding='UTF-8', newline="") as u:
        uwrite=csv.DictWriter(u, fieldnames=fieldnames_1)
        uwrite.writerow({'County': t1, 'Democratic': a1, 'Republican': a2, 'Other_not_unaf': a3,
               'Libertarian': a5, 'Unaffiliated': a6, 'White': b1, 'Black': b2, 'Asian': b5,
               'American_indian': b3, 'Other': b4, 'Hispanic/Latino': d1, 'Not_Hispanic/Latino': d2, 'Male': c1,
               'Female': c2, 'Total': y2})

        prtm = time.process_time()
        print(prtm, "(process tm)")
        #tot = ['County', t1, 'Democratic', a1, 'Republican', a2, 'Green', a3, 'Constitution', a4,
         #      'Libertarian', a5, 'Unaffiliated', a6, 'White', b1, 'Black', b2, 'Asian', b5,
          #     'American_indian', b3, 'Other', b4, 'Hispanic/Latino', d1, 'Not Hispanic/Latino', d2, 'Male', c1,
           #    'Female', c2, 'Total', y2]
        #print(tot)
#......


hr(fieldnames_1, nf)
for file in vfiles:
    a1 = 0
    a2 = 0
    a3 = 0
    a5 = 0
    a6 = 0

    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0

    c1 = 0
    c2 = 0

    d1 = 0
    d2 = 0

    y2 = 0

    #---------

    with open(file, "r", newline="") as k:
        kread=csv.DictReader(k, fieldnames=fieldnames2)
        print(file)
        for row in kread:

            t=[row[fieldnames2[1]], row[fieldnames2[3]], row[fieldnames2[25]], row[fieldnames2[26]], row[fieldnames2[27]], row[fieldnames2[28]]]
            tr=list(t)
            t1=str(tr[0])
            for item in tr[1]:
                if item=="A":
                    y2=y2+1
                    i = str(tr[4])
                    i.split(",", maxsplit=1)

                    if i.__contains__("DEM"):
                        a1 = a1 + 1
                        pass
                    elif i.__contains__("REP"):
                        a2 = a2 + 1
                        pass
                    elif i.__contains__("UNA"):
                        a6 = a6 + 1
                        pass
                    elif i.__contains__("LIB"):
                        a5 = a5 + 1
                        pass
                    else:
                        a3 = a3 + 1
                        pass

                    i2 = str(tr[3])
                    i2.split(",", maxsplit=1)

                    if i2 == "HL":
                        d1 = d1 + 1
                        pass
                    if i2 == "NL":
                        d2 = d2 + 1
                        pass
                    else:
                        pass

                    for item in tr[2]:
                        if item in tr[2] == "W":
                            b1 = b1 + 1
                            continue
                        elif item in tr[2] == "B":
                            b2 = b2 + 1
                            continue
                        elif item in tr[2] == "I":
                            b3 = b3 + 1
                            continue
                        elif item in tr[2] == "A":
                            b5=b5+1
                            continue
                        else:
                            b4 = b4 + 1
                            continue

                    for item in tr[5]:
                        if item in tr[5] == "M":
                            c1 = c1 + 1
                            continue
                        if item in tr[5] == "F":
                            c2 = c2 + 1
                            continue
                        else:
                            continue
                else:

                    continue
            continue

        pr(fieldnames_1, nf, a1, t1, a2, a3, a5, a6,
           b1, b2, b3, b4, b5,
           c1, c2, d1, d2, y2)

import csv


scoreALL={}

def printResult():
    global scoreALL
    global currentUser

    if scoreALL == {}:
        return

    result = ""
    # print scoreALL
    for qn in range(1,17):
        count = 0
        qn = str(qn)
        for score in scoreALL[qn]:
            count += scoreALL[qn][score]
        tmp = []
        for score in range(1,6):
            if not str(score) in scoreALL[qn]:
                tmp.append(str(score) + "," + str(round(0.0,2)))
            else:
                tmp.append(str(score) + "," + str(round(float(scoreALL[qn][str(score)])/count,3)))

    
        result += "\t" + ",".join(tmp)
    # print scoreALL
    print currentUser.decode('utf-8').encode('utf-8') + "\t" + result
    scoreALL = {}

f = open('data.csv', 'r')
currentUser = ""

for row in csv.reader(f):
    if currentUser != row[0]:
        printResult()
        currentUser = row[0]

    for i in range(1,17):
        
        qn = str(i)
        score = str(row[i])

        if not qn in scoreALL:
            scoreALL[qn] = {}

        if not score in scoreALL[qn]:
            scoreALL[qn][score]=1
        else:
            scoreALL[qn][score]+=1
f.close()
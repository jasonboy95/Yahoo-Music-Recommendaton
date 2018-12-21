SUM_FILE = "/Users/shiyaoli/Data/Ranking3.txt"
OUT_FILE = "/Users/shiyaoli/Data/Compare7.txt"
with open(OUT_FILE,'w') as output:
    with open(SUM_FILE) as score:
        cur=0
        vec={}
        for line in score:
            if cur<6:
                vec[line.strip("\n").split("|")[0]+"_"+line.strip("\n").split("|")[1]]=line.strip("\n").split("|")[2]
                cur+=1
            else:
                l=sorted(vec.items(), key=lambda item: item[1])
                for i in range(3):
                    output.write(l[i][0] + "," + '0' + "\n")
                for j in range(3,6):
                    output.write(l[j][0] + "," + '1' + "\n")
                vec={}
                vec[line.strip("\n").split("|")[0]+"_"+line.strip("\n").split("|")[1]]=line.strip("\n").split("|")[2]
                cur=1
    l = sorted(vec.items(), key=lambda item: item[1])
    for i in range(3):
        output.write(l[i][0] + "," + '0' + "\n")
    for j in range(3, 6):
        output.write(l[j][0] + "," + '1' + "\n")


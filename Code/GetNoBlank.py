SCORE_FILE = "/Users/shiyaoli/Data/Ranking3.txt"
OUT_FILE = "/Users/shiyaoli/Data/NoBlank1.txt"
import time
user_rate={}
start_time = time.time()
def my_sum(l):
    sum=0
    for i in l:
        sum=sum+int(i)
    return sum
with open(OUT_FILE,'w') as output:
    with open(SCORE_FILE) as score:
        for line in score:
            if float(line.strip("\n").split("|")[2]) != 0.0:
                output.write(line.strip("\n").split("|")[0] + "|" + line.strip("\n").split("|")[1] +"|"+line.strip("\n").split("|")[2]+"\n")
            else:
                output.write(line)


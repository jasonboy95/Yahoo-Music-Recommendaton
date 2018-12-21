SCORE_FILE = "/Users/shiyaoli/Data/Ranking2.txt"
OUT_FILE = "/Users/shiyaoli/Data/Ranking3.txt"
import time
user_rate={}
start_time = time.time()
def my_sum(l):
    sum=0
    count = 0
    for i in l:
        if int(i) != 0:
            count+=1
        sum=sum+int(i)
    if count != 0:
        return sum/count
    else:
        return sum
with open(OUT_FILE,'w') as output:
    with open(SCORE_FILE) as score:
        for line in score:
            try:
                user_id,track_id,sum_score=line.strip("\n").split("|")[0],line.strip("\n").split("|")[1],(1*int(line.strip().split("|")[2])+0.01*int(line.strip("\n").split("|")[3])+0.00007*my_sum(line.strip("\n").split("|")[4:]))/3
            except IndexError:
                user_id,track_id,sum_score = line.strip("\n").split("|")[0], line.strip("\n").split("|")[1], (1*int(line.strip("\n").split("|")[2]) + 0.01*int(line.strip("\n").split("|")[3]))/2
            output.write(user_id+"|"+track_id+"|"+str(sum_score)+"\n")


from __future__ import print_function
import time
import sys

OUTPUT_FILE = "/Users/shiyaoli/Data/Rankingf.txt"
H_FILE = "/Users/shiyaoli/Data/testTrack_hierarchy.txt"
TRAIN_FILE = "/Users/shiyaoli/Data/trainItem2.txt"

user_rate = {}
start_time = time.time()
with open(TRAIN_FILE) as train:
    for line in train:
        if "|" in line:
            cur_user = line.strip("\n").split("|")[0]
            user_rate[cur_user]={}
            continue
        item_id,item_score=line.strip("\n").split()
        user_rate[cur_user][item_id]=item_score

with open(OUTPUT_FILE, "w") as output:
    with open(H_FILE) as record:
        for line in record:
            gen_out=""
            user,track=line.strip("\n").split("|")[0],line.strip("\n").split("|")[1]
            items=line.strip("\n").split("|")[2:]
            if len(items)==0:
                album_score='None'
                artist_score='None'
            if len(items)==1:
                album=items[0]
                try:
                    album_score=user_rate[user][album]
                except KeyError:
                    album_score='None'
                artist_score='None'
            if len(items)==2:
                album = items[0]
                artist = items[1]
                try:
                    album_score=user_rate[user][album]
                except KeyError:
                    album_score='None'
                try:
                    artist_score=user_rate[user][artist]
                except KeyError:
                    artist_score='None'
            if len(items)>2:
                try:
                    album_score=user_rate[user][items[0]]
                except KeyError:
                    album_score='None'
                try:
                    artist_score=user_rate[user][items[1]]
                except KeyError:
                    artist_score='None'
                genr=items[2:]
                for g in genr:
                    try:
                        gen_out=gen_out+"|"+user_rate[user][g]
                    except KeyError:
                        pass
            output.write(user + "|" + track + "|" + album_score + "|"+artist_score+gen_out+"\n")



print("Finished, Spend %.2f s" % (time.time() - start_time))
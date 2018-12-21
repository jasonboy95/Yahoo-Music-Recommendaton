from __future__ import print_function
import time
import sys

TRACK_DATA_FILE = "/Users/shiyaoli/Data/trackData2.txt"
TRACK_HIERARCHY_FILE = "/Users/shiyaoli/Data/testTrack_hierarchy.txt"
TEST_DATA_FILE = "/Users/shiyaoli/Data/testItem2.txt"

lib_trackData = {}
start_time = time.time()

with open(TRACK_DATA_FILE) as trackData:
    for line in trackData:
        [track_Id, track_detail] = line.strip("\n").split("|", maxsplit=1)
        lib_trackData[track_Id] = track_detail
with open(TRACK_HIERARCHY_FILE, "w") as testHierarchy:
    with open(TEST_DATA_FILE) as testData:
        for line in testData:
            if "|" in line:
                cur_user = line.strip("\n").split("|")[0]
                continue
            cur_track = line.strip("\n")
            testHierarchy.write(cur_user + "|" + cur_track + "|" + lib_trackData[cur_track] + "\n")
print(cur_user)
print("Finished, Spend %.2f s" % (time.time() - start_time))
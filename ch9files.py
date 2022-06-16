import os
import csv


list = [["one", "two", "three"], ["yellow", "red", "black"], ["star", "planet", "galaxy"]]

fpath = os.path.join("D:\\", "Temp", "ch9test.csv")
with open(fpath, "w+") as f:
    w = csv.writer(f, delimiter=",")
    for j in range(len(list)):
        w.writerow(list[j])




with open(fpath, "r") as f:
    r = csv.reader(f)
    for row in r:
        print(",".join(row))








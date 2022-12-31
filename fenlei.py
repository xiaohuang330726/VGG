import os
import csv
import shutil

with open('train.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        if row[1]=='-1':
            shutil.copyfile('data/trainimage/'+row[0],'data_pre/woman/'+row[0])
        else:
            shutil.copyfile('data/trainimage/'+row[0], 'data_pre/man/' + row[0])
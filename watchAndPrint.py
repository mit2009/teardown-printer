import os
import time

cwd = os.getcwd()
files = os.listdir(cwd)

printers = ['athena', 'cadlab']
i = 0
switch = {0: 1, 1: 0}

for f in files:
    parts = f.split('.')
    if parts[-1] == 'txt':
        i = int(parts[0])

dryrun = True

while 1:
    files = os.listdir(cwd)
    for f in files:
        parts = f.split('.')
        if parts[-1] == 'jpg':
            if dryrun:
                print('lpr -P ' + printers[i] + ' ' + f)
                print('mv ' + f + ' ' + f + '.done')
            else:
                os.system('lpr -P ' + printers[i] + ' ' + f)
                os.system('mv ' + f + ' ' + f + '.done')
            newi = switch[i]
            os.system("mv " + str(i) + '.txt ' + str(newi) + '.txt')
            i = newi
    time.sleep(1)

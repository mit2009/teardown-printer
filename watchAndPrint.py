import os
import time

cwd = os.getcwd()
files = os.listdir(cwd)

printers = ['HP_Color_LaserJet_MFP_M277dw', 'HP_Color_LaserJet_Pro_M252dw']
i = 0

#to make this work properly, make sure to have a 0.txt file in the same directory as a script.
# for f in files:
#     parts = f.split('.')
#     if parts[-1] == 'txt':
#         i = int(parts[0])

#set this to True to do a run through of what the teardown printer will produce. During teardown, set to False.
dryrun = True 
photo_lookalikes = ['jpg', 'jpeg', 'png', 'dng']


files = os.listdir(cwd)

#os.rename(f,f.replace(" ", "_"))
while 1: 
    for f in files:
        os.rename(f,f.replace(" ", "_"))
        #splits the files into their name and extension
        parts = f.split('.')

        #check if original file has spaces. if it does, replace them with underscores

        if parts[-1].lower() in photo_lookalikes:
            if dryrun:
                print('lpr -P ' + printers[i] + ' -o media=Custom.4x6 ' + f)
                print('mv ' + f + ' ' + f + '.done')
            else:
                 os.system('lpr -P ' + printers[i] + ' -o media=Custom.4x6 ' + f)
                 os.system('mv ' + f + ' ' + f + '.done')
            #update the i so we can switch between the printers. In 2018, we're using 2 printers. 
            print('printed photo number '+ str(i+1) + ': '+str(f))
            newi = (i + 1) % len(printers)
            print(newi)
            os.system("mv " + str(i) + '.txt ' + str(newi) + '.txt')
            i = newi
    time.sleep(1)

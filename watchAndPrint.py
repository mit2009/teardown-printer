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
dryrun = False 

photo_lookalikes = ['jpg', 'jpeg', 'png', 'dng']
files = os.listdir(cwd)


while 1: 
    files = os.listdir(cwd)
    for f in files:

        #check if file has spaces. if it does, replace them with underscores
        if ' ' in f:
            print(f)
            os.rename(f,f.replace(" ", "_"))

        #splits the files into their name and extension
        parts = f.split('.')


        if parts[-1].lower() in photo_lookalikes:

            if dryrun:
                print('lpr -P ' + printers[i] + '  -o PageSize=4x6 -o InputSlot=tray-2 ' + f)
                print('mv ' + f + ' ' + f + '.done')
            else:
                os.system('lpr -P ' + printers[i] + '  -o PageSize=4x6 -o InputSlot=tray-2 ' + f)
                # if i == 1:
                #     os.system('lpr -P ' + printers[i] + '  -o PageSize=4x6 -o InputSlot=Tray2 ' + f)
                # else:
                #     os.system('lpr -P ' + printers[i] + '  -o PageSize=4x6 -o InputSlot=tray-2 ' + f)
                os.system('mv ' + f + ' ' + f + '.done')
            #update the i so we can switch between the printers. In 2018, we're using 2 printers. 
            newi = (i + 1) % len(printers)
            print(printers[i])
            os.system("mv " + str(i) + '.txt ' + str(newi) + '.txt')
            i = newi
        time.sleep(2)

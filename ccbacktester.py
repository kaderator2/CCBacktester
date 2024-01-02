import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
import time

style.use('fivethirtyeight')

fig, axs = plt.subplots(2)
fig.suptitle('CCBacktester')
axs[1].title.set_text("Correlation Coefficient")
axs[0].title.set_text("Normalized Currency Pairs")


'''Parsing EUR/USD Data'''
#EURUSD.FX15.csv
eurusd = np.array([])
tse = np.array([])
f1 = open("EURUSD.csv")
data = list(csv.reader(f1, delimiter=','))
for x in range (0, len(data)):
    eurusd = np.append(eurusd, data[x][5])
    tse = np.append(tse, data[x][0:2])
eurusd = np.array(eurusd, dtype=np.float32)

'''Parsing GBP/USD Data'''
#GBPUSD.FX15.csv
gbpusd = np.array([])
tsg = np.array([])
f2 = open("GBPUSD.csv")
data2 = list(csv.reader(f2, delimiter=','))
for x in range (0, len(data2)):
    gbpusd = np.append(gbpusd, data2[x][5])
    tsg = np.append(tsg, data2[x][0:2])
gbpusd = np.array(gbpusd, dtype=np.float32)

'''Parsing new file data EUR/USD'''
f = open('newdataeurusd.txt', 'r')
tempeurusd = f.readlines()
f.close()
tempeurusd = np.array(tempeurusd, dtype=np.float32)

'''Parsing new file data GBP/USD'''
f = open('newdatagbpusd.txt', 'r')
tempgbpusd = f.readlines()
f.close()
tempgbpusd = np.array(tempgbpusd, dtype=np.float32)

'''Checking data validity'''
if tsg[0] != tse[0]:
    shift = 0
    print("array timestamp mismatched! Fixing now")
    x = 0
    while x < len(tse):
        if tse[0] == tsg[x] and tse[1] == tsg[x+1]:
            shift = x
            x = len(tse)
        x = x + 1
    if shift == 0:
        while x < len(tsg):
            if tsg[0] == tse[x] and tsg[1] == tse[x+1]:
                shift = x
                x = len(tsg)
            x = x + 1
    shift = int(shift / 2)
    tsg = tsg[shift:]
    gbpusd = gbpusd[shift:]

#checking to see if new temp data matches front of data set
print(tempeurusd[0])
print(eurusd[len(eurusd) - 1])
if tempeurusd[0] != eurusd[len(eurusd) - 1] or tempgbpusd[0] != gbpusd[len(eurusd) - 1]:
    print('Print temp data sets mismatched\nRestart both programs!')
    exit()

'''Making data sets even length'''
if len(gbpusd) > len(eurusd):
    gbpusd = np.resize(gbpusd, (len(eurusd)))
    tsg = np.resize(tsg, (len(tse)))
else:
    eurusd = np.resize(eurusd, (len(gbpusd)))
    tse = np.resize(tse, (len(tsg)))

'''resizing datasets'''
eurusd = np.flip(eurusd)
gbpusd = np.flip(gbpusd)
eurusd = np.resize(eurusd, 250 - (len(tempeurusd) - 1))
gbpusd = np.resize(gbpusd, 250 - (len(tempgbpusd) - 1))
eurusd = np.flip(eurusd)
gbpusd = np.flip(gbpusd)

'''adding new data to arrays'''
for x in range (1, len(tempeurusd)):
    eurusd = np.append(eurusd, tempeurusd[x])
for x in range (1, len(tempgbpusd)):
    gbpusd = np.append(gbpusd, tempgbpusd[x])

dummy = []
for x in range (0, len(eurusd)):
    dummy.append(x)

'''getting corrcoef'''
CORDIV = int(len(eurusd) * 0.06)
corlist = np.array([])
counter = int(len(eurusd)/CORDIV)
while counter != len(gbpusd):
    cor2 = np.corrcoef(eurusd[counter-int((len(eurusd)/CORDIV)):counter],gbpusd[counter-int((len(eurusd)/CORDIV)):counter])
    corlist = np.append(corlist, cor2[0][1])
    counter = counter + 1

def animate(i):
    global eurusd
    global gbpusd
    global axs
    with open('newdataeurusd.txt') as f:
        for line in f:
            pass
        elast_line = line
        f.close()
    with open('newdatagbpusd.txt') as h:
        for line in h:
            pass
        glast_line = line
        h.close()
    if elast_line != eurusd[len(eurusd) - 1] and glast_line != gbpusd[len(gbpusd) - 1]:
        print('UPDATING GRAPHS')
        eurusd = np.roll(eurusd, -1)
        gbpusd = np.roll(gbpusd, -1)
        eurusd[len(eurusd) - 1] = float(elast_line)
        gbpusd[len(gbpusd) - 1] = float(glast_line)
        CORDIV = int(len(eurusd) * 0.06)
        corlist = np.array([])
        counter = int(len(eurusd)/CORDIV)
        while counter != len(gbpusd):
            cor2 = np.corrcoef(eurusd[counter-int((len(eurusd)/CORDIV)):counter],gbpusd[counter-int((len(eurusd)/CORDIV)):counter])
            corlist = np.append(corlist, cor2[0][1])
            counter = counter + 1
        '''Normalizing gbpusd afer changes'''
        ngbpusd = np.array([])
        s1 = np.std(gbpusd)
        s2 = np.std(eurusd)
        m1 = np.mean(gbpusd)
        m2 = np.mean(eurusd)
        for x in range (0, len(gbpusd)):
            ngbpusd = np.append(ngbpusd, m2 + (gbpusd[x] - m1) * (s2/s1))
        axs[0].clear()
        axs[1].clear()
        axs[1].title.set_text("Correlation Coefficient")
        axs[0].title.set_text("Normalized Currency Pairs")

        axs[0].plot(dummy,eurusd, label="eurusd")
        axs[0].plot(dummy,ngbpusd, label="gbpusd")
        axs[0].legend(loc="upper left")
        axs[1].plot(dummy[int((len(eurusd)/CORDIV)):], corlist)
        axs[1].axhline(0, color='black',linestyle='--')
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()


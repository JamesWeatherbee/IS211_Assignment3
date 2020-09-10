# the url is: 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
# path to file, datetime accessed, browser, status of request, request size in bytes
import csv
import urllib.request
import codecs
import re
import datetime

from io import StringIO
import logging

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

def downloadData(url):
    content = urllib.request.urlopen(url).read().decode('utf-8')
    return content

# print(downloadData(url))

# THIS IS THE CODE THAT PUTS THE CSV IN SEPARATE LISTS!!!!!
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
# *********************************************************



data = csvfile
browserCount = 0
imageCount = 0

zeroHour = oneHour = twoHour = threeHour = fourHour = fiveHour = sixHour = 0
sevenHour = eightHour = nineHour = tenHour = elevenHour = twelveHour = 0
thirteenHour = fourteenHour = fifteenHour = sixteenHour = seventeenHour = eighteenHour = 0
nineteenHour = twentyHour = twentyoneHour = twentytwoHour = twentythreeHour = twentyfourHour = 0

firefox = ['Firefox', 0]
safari = ['Safari', 0]
explorer = ['Internet Explorer', 0]
chrome = ['Chrome', 0]
for line in csvfile:
    browserCount += 1
    if re.search(r'Firefox', line[2], re.I):
        firefox[1] += 1
    elif re.search(r'MSIE', line[2]):
        safari[1] += 1
    elif re.search(r'Chrome', line[2]):
        explorer[1] += 1
    elif re.search(r'Safari', line[2]) and not re.search('Chrome', line[2]):
        chrome[1] += 1
    if re.search('jpe?g|JPE?G|png|PNG|gif|GIF', line[0]):
        imageCount += 1



# Here is an attempt at counting the hourly activity.



    if re.search(r'[0][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
        oneHour += 1
    if re.search(r'[0][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twoHour += 1
    if re.search(r'[0][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twoHour += 1
    if re.search(r'[0][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
        threeHour += 1
    if re.search(r'[0][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
        fourHour += 1
    if re.search(r'[0][5]:[0-9][0-9]:[0-9][0-9]', line[1]):
        fiveHour += 1
    if re.search(r'[0][6]:[0-9][0-9]:[0-9][0-9]', line[1]):
        sixHour += 1
    if re.search(r'[0][7]:[0-9][0-9]:[0-9][0-9]', line[1]):
        sevenHour += 1
    if re.search(r'[0][8]:[0-9][0-9]:[0-9][0-9]', line[1]):
        eightHour += 1
    if re.search(r'[0][9]:[0-9][0-9]:[0-9][0-9]', line[1]):
        nineHour += 1
    if re.search(r'[1][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
        tenHour += 1
    if re.search(r'[1][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
        elevenHour += 1
    if re.search(r'[1][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twelveHour += 1
    if re.search(r'[1][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
        thirteenHour += 1
    if re.search(r'[1][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
        fourteenHour += 1
    if re.search(r'[1][5]:[0-9][0-9]:[0-9][0-9]', line[1]):
        fifteenHour += 1
    if re.search(r'[1][6]:[0-9][0-9]:[0-9][0-9]', line[1]):
        sixteenHour += 1
    if re.search(r'[1][7]:[0-9][0-9]:[0-9][0-9]', line[1]):
        seventeenHour += 1
    if re.search(r'[1][8]:[0-9][0-9]:[0-9][0-9]', line[1]):
        eighteenHour += 1
    if re.search(r'[1][9]:[0-9][0-9]:[0-9][0-9]', line[1]):
        nineteenHour += 1
    if re.search(r'[2][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twentyHour += 1
    if re.search(r'[2][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twentyoneHour += 1
    if re.search(r'[2][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twentytwoHour += 1
    if re.search(r'[2][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twentythreeHour += 1
    if re.search(r'[2][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
        twentyfourHour += 1
        


browsers = [firefox, safari, explorer, chrome]
imagePercent = (imageCount / browserCount) * 100
mostPopularBrowser = max(browsers)

output = 'Of {} hits, {} ({}%) are images. The most popular browser is {}.'.format(browserCount, imageCount, imagePercent, mostPopularBrowser[0])
# print(output)
allHours = (oneHour, twoHour, threeHour, fourHour, fiveHour, sixHour, sevenHour, eightHour, nineHour, tenHour,
            elevenHour, twelveHour, thirteenHour, fourteenHour, fifteenHour, sixteenHour, seventeenHour, eighteenHour,
            nineteenHour, twentyHour, twentyoneHour, twentytwoHour, twentythreeHour, twentyfourHour)
print(allHours)

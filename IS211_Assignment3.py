# the url is: 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
# path to file, datetime accessed, browser, status of request, request size in bytes
import csv
import urllib.request
import codecs
import re

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'


def downloadData(url):
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    return csvfile


def processUrl(csvfile):

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
        if re.search('Firefox', line[2], re.I):
            firefox[1] += 1
        elif re.search(r'MSIE', line[2]):
            safari[1] += 1
        elif re.search(r'Chrome', line[2]):
            explorer[1] += 1
        elif re.search(r'Safari', line[2]) and not re.search('Chrome', line[2]):
            chrome[1] += 1
        if re.search('jpe?g|JPE?G|png|PNG|gif|GIF', line[0]):
            imageCount += 1

        browsers = [firefox, safari, explorer, chrome]
        imagePercent = (imageCount / browserCount) * 100
        mostPopularBrowser = max(browsers)

        output = 'Of {} hits, {} ({}%) are images. The most popular browser is {}.'.format(browserCount, imageCount,
                                                                                           imagePercent,
                                                                                           mostPopularBrowser[0])
        print(output)

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

        print('Hour 1 had {} hits.'.format(oneHour))
        print('Hour 2 had {} hits.'.format(twoHour))
        print('Hour 3 had {} hits.'.format(threeHour))
        print('Hour 4 had {} hits.'.format(fourHour))
        print('Hour 5 had {} hits.'.format(fiveHour))
        print('Hour 6 had {} hits.'.format(sixHour))
        print('Hour 7 had {} hits.'.format(sevenHour))
        print('Hour 8 had {} hits.'.format(eightHour))
        print('Hour 9 had {} hits.'.format(nineHour))
        print('Hour 10 had {} hits.'.format(tenHour))
        print('Hour 11 had {} hits.'.format(elevenHour))
        print('Hour 12 had {} hits.'.format(twelveHour))
        print('Hour 13 had {} hits.'.format(thirteenHour))
        print('Hour 14 had {} hits.'.format(fourteenHour))
        print('Hour 15 had {} hits.'.format(fifteenHour))
        print('Hour 16 had {} hits.'.format(sixteenHour))
        print('Hour 17 had {} hits.'.format(seventeenHour))
        print('Hour 18 had {} hits.'.format(eighteenHour))
        print('Hour 19 had {} hits.'.format(nineteenHour))
        print('Hour 20 had {} hits.'.format(twentyHour))
        print('Hour 21 had {} hits.'.format(twentyoneHour))
        print('Hour 22 had {} hits.'.format(twentytwoHour))
        print('Hour 23 had {} hits.'.format(twentythreeHour))
        print('Hour 24 had {} hits.'.format(twentyfourHour))


def main():
    downloadData(url)
    processUrl(csvfile)


if __name__ == '__main__':
    main()



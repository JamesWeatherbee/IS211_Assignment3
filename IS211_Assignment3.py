#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import urllib.request
import codecs
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-url', help='Enter a URL')
args = parser.parse_args()


def downloadData(url):
    '''Open a user provided URL.

    Args:
        url(str): The url for a website that should contain a .csv file.

    Returns:
        csvfile(file): The .csv file from the provided URL.
    '''
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    return csvfile


def processUrl(csvfile):
    '''Processes the user provided .csv file from the URL.

    Args:
        csvfile(file): The .csv file from the URL opened with downloadData function.

    Returns:
        output(str): A string that the number of hits, the number of images and percentage
        of the hits that are images, and the browser that used the most.
        hourOutput(list): A list that lists the number of hits per hour.
    '''
    browserCount = 0
    imageCount = 0

    oneHour = twoHour = threeHour = fourHour = fiveHour = sixHour = 0
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
        if re.search(r'[0][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
            oneHour += 1
        elif re.search(r'[0][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twoHour += 1
        elif re.search(r'[0][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twoHour += 1
        elif re.search(r'[0][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
            threeHour += 1
        elif re.search(r'[0][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
            fourHour += 1
        elif re.search(r'[0][5]:[0-9][0-9]:[0-9][0-9]', line[1]):
            fiveHour += 1
        elif re.search(r'[0][6]:[0-9][0-9]:[0-9][0-9]', line[1]):
            sixHour += 1
        elif re.search(r'[0][7]:[0-9][0-9]:[0-9][0-9]', line[1]):
            sevenHour += 1
        elif re.search(r'[0][8]:[0-9][0-9]:[0-9][0-9]', line[1]):
            eightHour += 1
        elif re.search(r'[0][9]:[0-9][0-9]:[0-9][0-9]', line[1]):
            nineHour += 1
        elif re.search(r'[1][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
            tenHour += 1
        elif re.search(r'[1][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
            elevenHour += 1
        elif re.search(r'[1][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twelveHour += 1
        elif re.search(r'[1][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
            thirteenHour += 1
        elif re.search(r'[1][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
            fourteenHour += 1
        elif re.search(r'[1][5]:[0-9][0-9]:[0-9][0-9]', line[1]):
            fifteenHour += 1
        elif re.search(r'[1][6]:[0-9][0-9]:[0-9][0-9]', line[1]):
            sixteenHour += 1
        elif re.search(r'[1][7]:[0-9][0-9]:[0-9][0-9]', line[1]):
            seventeenHour += 1
        elif re.search(r'[1][8]:[0-9][0-9]:[0-9][0-9]', line[1]):
            eighteenHour += 1
        elif re.search(r'[1][9]:[0-9][0-9]:[0-9][0-9]', line[1]):
            nineteenHour += 1
        elif re.search(r'[2][0]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twentyHour += 1
        elif re.search(r'[2][1]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twentyoneHour += 1
        elif re.search(r'[2][2]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twentytwoHour += 1
        elif re.search(r'[2][3]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twentythreeHour += 1
        elif re.search(r'[2][4]:[0-9][0-9]:[0-9][0-9]', line[1]):
            twentyfourHour += 1

    hourOutput = ['Hour 1 had {} hits.'.format(oneHour),
                  'Hour 2 had {} hits.'.format(twoHour),
                  'Hour 3 had {} hits.'.format(threeHour),
                  'Hour 5 had {} hits.'.format(fiveHour),
                  'Hour 6 had {} hits.'.format(sixHour),
                  'Hour 7 had {} hits.'.format(sevenHour),
                  'Hour 8 had {} hits.'.format(eightHour),
                  'Hour 9 had {} hits.'.format(nineHour),
                  'Hour 10 had {} hits.'.format(tenHour),
                  'Hour 11 had {} hits.'.format(elevenHour),
                  'Hour 12 had {} hits.'.format(twelveHour),
                  'Hour 13 had {} hits.'.format(thirteenHour),
                  'Hour 14 had {} hits.'.format(fourteenHour),
                  'Hour 15 had {} hits.'.format(fifteenHour),
                  'Hour 16 had {} hits.'.format(sixteenHour),
                  'Hour 17 had {} hits.'.format(seventeenHour),
                  'Hour 18 had {} hits.'.format(eighteenHour),
                  'Hour 19 had {} hits.'.format(nineteenHour),
                  'Hour 20 had {} hits.'.format(twentyHour),
                  'Hour 21 had {} hits.'.format(twentyoneHour),
                  'Hour 22 had {} hits.'.format(twentytwoHour),
                  'Hour 23 had {} hits.'.format(twentythreeHour),
                  'Hour 24 had {} hits.'.format(twentyfourHour)]

    print(output)
    for i in hourOutput:
        print(i)


def main():
    '''Runs the functions downloadData and processUrl if url is valid.  Returns error message if not.'''
    if not args.url:
        exit()
    try:
        csv_data = downloadData(args.url)
    except urllib.error.URLError:
        print('Not a valid URL.')
    else:
        processUrl(csv_data)


if __name__ == '__main__':
    main()



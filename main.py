#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
import thingspeak

#### Paramaters ####
## ThingSpeak (leave blank if you don't want to use)
thgspkChannelId  = '144852'           # Channel ID
thngspkWriteKey  = 'BJIXS84NDQ0HA3V7' # Write ID

## Twitter
twitterAccessToken       = '764221380950953984-MSCdmOogNOIH00bUiDE3wQfHGPleNKL'
twitterAccessTokenSecret = 'ODSbNoDfBGluzkXtSFwphcOT8Ah0QyFIXFexa7L5s7wFn'
twitterConsumerKey       = 'iD6FTsTOtz0d31R0WW81Jmz0m'
twitterConsumerKeySecret = 'FIZdbevu0nrhNhpoL18bq0ysv8Air3HraJ6TvWopumzsJIRFkX'

## Handle
#handleMain  = '@Comcast' # replace with your ISP
#handleExtra = '@ComcastCares @xfinity' # any other handles you want
#tags        = '#speedtest' # any tags you want
#location    = 'Bloomington, MN' # city and state
handleMain = ''
handleExtra = ''
tags = '#speedtest'
location = 'Space'

## SYPF (Speed You Pay For)
targetDownload = 75
targetUpload   = 10

## Threshold (at what decrease in speed will the tweet trigger?)
threshold = 20


#### Alright, here we go! Not recomended to change anything after this. ####
def test():
    # Init ThingSpeak if key is given
	if (thgspkChannelId != '' and thngspkWriteKey != ''):
		thingspeakLog = thingspeak.Channel(id = thgspkChannelId, write_key = thngspkWriteKey)

        # run speedtest-cli
        print 'running test'
        a = os.popen('speedtest-cli --simple').read()
        print 'ran'

        # split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        if 'Cannot' in a: # if we can't connect to the internet no point in tweeting
            return false

        # extract the values for ping down and up values
        ping = lines[0][6:11]
        download = lines[1][10:14]
        upload = lines[2][8:12]

        print date, ping, download, upload

        # log to ThingSpeak if enabled
        if (thingspeakLog):
            thingspeakLog.update({1:ping, 2:download, 3:upload})

        # tweet if down speed is less than threshold
        if (int(float(download)) < targetDownload - threshold):
            # connect to Twitter
            my_auth = twitter.OAuth(twitterAccessToken, twitterAccessTokenSecret, twitterConsumerKey, twitterConsumerKeySecret)
            twit = twitter.Twitter(auth=my_auth)

            print 'trying to tweet'
            try:
                tweet = 'Hey ' + handleMain + ' why is my internet speed ' + str(int(float(download))) + 'down\\' + str(int(float(upload))) + 'up when I pay for ' + str(targetDownload) + 'down\\' + str(targetUpload) + 'up in ' + location + '? ' + handleExtra + ' ' + tags
                twit.statuses.update(status=tweet)
            except Exception,e:
                print str(e)
                pass
        return

if __name__ == '__main__':
        test()
        print 'completed'

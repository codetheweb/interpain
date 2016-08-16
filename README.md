# interpain

Automatically complain to your ISP (Comcast, CenturyLink, etc) about your internet speed and/or automatically log it to ThingSpeak.

More polished version of [pastebin.com/WMEh802V](http://pastebin.com/WMEh802V).

## Install

It's super easy to get started. Clone this repository in `pi`'s home folder:

```
git clone https://github.com/codetheweb/interpain.git
```

Then

```
cd interpain
sh setup
```
Add ThingSpeak and/or Twitter credentials (see below section) to `main.py` with `nano main.py` (don't forget to update the speeds you pay for too!). If you don't want to use Twitter, set the `threshold` to `targetDownload`.

## Credentials

*Both* ThingSpeak and Twitter credentials are optional.  (Although your Raspberry Pi isn't going to do much if you don't fill in either.)

The easiest setup would be an automated logging device by just pasting in the required keys for ThingSpeak.

### ThingSpeak
The keys for ThingSpeak are easiest to obtain.  Go to [thingspeak.com](http://thingspeak.com) and sign up for an account.  Create a channel, marking the fields as follows:

* Field1: '**Ping (ms)**'
* Field2: '**Download (MB/s)**'
* Field3: '**Upload (MB/s)**'
* URL: if you're in a giving mood, you can link to this repo: github.com/codetheweb/interpain


### Twitter
Twitter is a bit tricker.  You can either create a new account just for interpain or use your personal account.  Either way, go to [apps.twitter.com](https://apps.twitter.com) and create a new app get the keys.

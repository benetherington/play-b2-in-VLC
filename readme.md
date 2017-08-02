# Play B2 in VLC
My SO has a tiny harddrive, but a large digital media collection. When I realized I had 10 gb worth of BackBlaze's B2 cloud storage, I started uploading her files to the cloud and having her stream them using VLC. Organizing the URLs got a bit out of hand. Luckily, B2 has a [Python module!](https://github.com/mtingers/backblaze-b2)

This is a super stripped down application that displays all the files on a B2 server and makes it easy to stream them in VLC or delete them. It would be pretty easy to add an upload function as well, but I don't mind using the command line utility.

## Dependencies
(BackBlazeB2)[https://github.com/mtingers/backblaze-b2]

## Setup
Create a document called private.py in the same folder play-b2-in-VLC.py is in. Add the following text, substituting with your own values.

```
B2_ACCOUNT = "i6wqssqn5xml"
B2_APPLICATION_KEY = "zeprdktc6vp65kbeknjvzeprdktc6vp65kbeknjv32"
B2_SERVER = "f001"
```

Your account and application keys can be found in your B2 bucket management page. Use the command `b2 make-url` to find your server number. This will be collected automatically in a future version.

## Packaging
If you want to run this from the command line every time, that's totally fine! However, included is a `setup.py` file that will allow you to use [py2app](https://py2app.readthedocs.io/en/latest/) or [py2exe](http://www.py2exe.org/) to build a little executable app for yourself. Just be sure to put the folder `backblaze-b2-master` in the same directory, or otherwise specify its location in `setup.py`.

Enjoy!
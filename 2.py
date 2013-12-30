import urllib

inchar = "abcdefghijklmnopqrstuvwxyz"
remaining = []
web = "http://www.pythonchallenge.com/pc/def/ocr.html"
web3 = "http://www.pythonchallenge.com/pc/def/equality.html"

def pleasework(url):
    doclocation = urllib.urlopen(url)
    openfile = doclocation.read()
    comment = openfile.split('<!--')[2]
    for s in comment:
        if s in inchar:
            remaining.append(s)
    print remaining

answer = pleasework(web)
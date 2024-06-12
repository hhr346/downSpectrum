'''
This script aims to use wget to download the spectrum automatically
'''
import subprocess

# Read the url of downloading
urls = []
f = open('./url.txt', 'r')
for line in f:
    line = line.rstrip('\n')
    urls.append(line)

for i in range(0, len(urls)):
    file = urls[i]
    file = 'http://xxxxxxxx:xxxxxxxx@218.247.138.126:90/xxxxxxxx/' + file + '.tar'
    print('Downloading ', file)
    command = ["wget", "-P", "./download", "-nc", file]
    try:
        subprocess.run(command, check=True)
    except Exception as error:
        print(error)

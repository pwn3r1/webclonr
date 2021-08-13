import urllib.request

print('pwn3r1`s HTML Downloader')

url = input('Whats the URL for the website?: ')

print('thank you for using my tool')
print('the file should appear on your desktop/directory you are in')

urllib.request.urlretrieve(url, 'webpage.html')

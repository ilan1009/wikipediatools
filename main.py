import wikipedia
import requests
import shutil
from os import makedirs


def downloadImages(activepage):
    makedirs('downloads\\' + activepage.title)
    pageImages = page.images
    for image in pageImages:
        filename = ("downloads\\" + page.title + "\\" + image.split('/')[-1])
        r = requests.get(image, headers={'User-agent': 'Mozilla/5.0'}, stream=True)

        if r.status_code == 200:
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retrieved')


def summary(activepage):
    sum = activepage.summary
    print('\n' + sum.replace('\n', '') + '\n')


query = input("Query or page: ")

if "page" not in query:
    search = wikipedia.search(query)
    print(search)

    pageSelect = input("Page (CaSe): ")
    page = wikipedia.page(pageSelect)

else:
    pageSelect = query.replace('page ', '')
    page = wikipedia.page(pageSelect)

print(page.title + ' <= Active page')

quitCommand = False
while not quitCommand:
    commandInput = input('Command: ')

    if commandInput.lower() == 'help':
        print('Commands: help, images, summary, url')

    elif commandInput.lower() == 'images':
        downloadImages(page)

    elif commandInput == 'quit':
        quitCommand = True

    elif commandInput == 'summary':
        summary(page)

    elif commandInput == 'url':
        print(page.url)

    elif commandInput == 'references':
        print(*page.references, sep='\n')

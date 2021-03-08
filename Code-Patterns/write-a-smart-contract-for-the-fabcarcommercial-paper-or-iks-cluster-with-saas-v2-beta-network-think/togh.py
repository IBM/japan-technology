import os
my_meta =[]
my_list =[]
try:
    f = open("index.md", "r", encoding="utf-8")
except:
    quit()

datalist =f.readlines()

myPath = "English version: https://developer.ibm.com/patterns/"+os.getcwd().replace('/Users/oniak3/github/japan-technology/Code-Patterns/','')

isMeta = False
for data in datalist:
    nGit = data.find("---")
    if nGit != -1:
        if isMeta == False:
            isMeta = True
        else:
            isMeta = False
            data = " "

    if isMeta == True:
        my_meta.append(data)
    else:
        # my_list.append(data.rstrip('\n'))
        my_list.append(data)

f.close()

isGit = False
for metadata in my_meta:
    if isGit == True:
        nUrl = metadata.find('- url')
        if nUrl != -1:
            sGit = metadata.replace('- url',"ソースコード")
            sGit = sGit.replace('"', '')
            isGit = False

    nSubTitle = metadata.find('subtitle: ')
    if nSubTitle != -1:
        sSubTitle = metadata.replace('subtitle: ', "### ")
        sSubTitle = sSubTitle.replace('"', '')
    nTitle = metadata.find('title: ')
    if nTitle != -1:
        sTitle = metadata.replace('title: ', "# ")
        sTitle = sTitle.replace('"', '')

    nGit = metadata.find('github:')
    if nGit != -1:
        isGit = True
        continue
    
    nLastUpdate = metadata.find('last_updated')
    if nLastUpdate!=-1:
        sLastUpdate = metadata.replace('"', '')

print(sTitle)
print (sSubTitle)
print (myPath)
print (sGit)
print("###### 最新の英語版コンテンツは上記URLを参照してください。")
print(sLastUpdate)
#print(my_meta)
for sText in my_list:
    print(sText.rstrip('\n'))



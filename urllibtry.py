import urllib 
myurl=urllib.urlopen("http://www.yahoo.com")
print myurl
contents=myurl.readlines()
print contents
#print 

headerinfo=myurl.info()
headerinfo.getheader("date")
headerinfo.getheader("content-type")
urllib.urlretrieve("http://www.yahoo.com",filename="urlcontent")


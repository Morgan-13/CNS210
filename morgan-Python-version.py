from bs4 import BeautifulSoup
import urllib
import urllib2

soup = BeautifulSoup()
url = "https://www.python.org/downloads/"
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
soup = BeautifulSoup(handle.read(), 'html.parser')
downloadlist = soup.select(".download-list-widget li")
for item in downloadlist:
	if item.select_one(".release-date").text.strip() != "April 6, 2013":
		continue
	if item.select_one(".release-number").text.strip()[7:10] != "2.7":
		continue
	version = item.select_one(".release-number").text.strip()[7:]
	#retrieve and download python 2.7.4
	print("Begin download")
	urllib.urlretrieve("https://www.python.org/ftp/python/" + version + "/python-" + version + ".msi", "morgan-python-" + version + ".msi")

print("Completed")
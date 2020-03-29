#Import de request URl from the urllib library.
from urllib import request
#URl (address) of the desired page
sample_url = 'http://AlanSimpson.me/python/sample.html'
print("Request the page and put it in a variable named the page")
thepage = request.urlopen(sample_url)
print("Put the response code in a variable name status")
status = thepage.code
print("What is the data type of the page?")
print(type(thepage))
print("What is the status code?")
print(status)


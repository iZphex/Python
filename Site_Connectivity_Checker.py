# import urllib
# use urllib.request to get data from URL
# write a func that takes the UR, returns a response
import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker")
input_url = input("Input the URL of the site you want to check: ")

main(input_url)

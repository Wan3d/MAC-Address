'''
1. Get MAC Address and convert it to the required format
2. Split MAC Address to only get the ID vendor
3. Access to the URL through the HTML requests
4. Convert the content page to an string and then a list of substrings
5. Algorithm to get manufacturer's name
6. Some stuff to show the final input correctly
'''

import requests
from bs4 import BeautifulSoup
from getmac import get_mac_address
import time

url = 'https://standards-oui.ieee.org/oui/oui.txt'
headers = {"User-Agent": "Mozilla/5.0"}

def getResponse():
    # Get the HTML from page and parse it to text
    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    listText = content.split()
    return listText

def getIndex(list, ID):
    return list.index(ID)

def getVendorName(listContent, index):
    word = ""
    manufacturerList = []

    while word != "(base":
        word = listContent[index + 2]
        manufacturerList.append(word)
        index += 1

    # Now we got the name, we will need to delete the last 2 elements of the list 
    # They will never be part of the manufacturer name

    manufacturerList = manufacturerList[:len(manufacturerList) - 2]

    # Finally, we have to convert the list to a string and return it
    nameManufacturer = ' '.join(manufacturerList)
    return nameManufacturer

def showData(macAddress, vendorNumber, nameManufacturer):
    print("--------------------------------")
    print(f"-> MAC Address: {macAddress}")
    print(f"-> MAC OUI: {vendorNumber}")
    print(f"-> Manufacturer name: {nameManufacturer}")
    print("--------------------------------")

def main():
    # Get the MAC Address
    macAddress = get_mac_address()
    macAddress = macAddress.replace(':', '-')
    macAddress = macAddress.upper()

    # Split manufacturer part
    vendorNumber = macAddress[:8]

    # Set the content of the page in a list of substrings and get the ID index from list
    listContent = getResponse()
    index = getIndex(listContent, vendorNumber)

    # Get the name of the manufacturer
    nameManufacturer = getVendorName(listContent, index)

    # User experience
    print("Your info is being proccesed... Wait some seconds!")
    time.sleep(3)

    # Show final output
    showData(macAddress, vendorNumber, nameManufacturer)
    

if __name__ == "__main__":
    main()
    input("Press any key to exit...")
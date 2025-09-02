import os
import requests
from bs4 import BeautifulSoup
from getmac import get_mac_address

# Get the MAC Address
macAddress = get_mac_address()
macAddress = macAddress.replace(':', '-')
macAddress = macAddress.upper()

# Split manufacturer part
vendorNumber = macAddress[:8]

# Get the HTML from page and parse it to text
response = requests.get('https://standards-oui.ieee.org/oui/oui.txt', timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.get_text()
listText = content.split()

# Get vendor index from list
index = listText.index(vendorNumber)

# Once you we got the index where is located our ID, we will need to get the information about the manufacturer
# As we know, we have a list of substrings of the page content. The name of a manufacturer could be one or many
# substrings in the list, so we will need to be sure that we load the name of the manufacturer in a list with
# the substrings

word = ""
manufacturerList = []
while word != "(base":
    word = listText[index + 2]
    manufacturerList.append(word)
    index += 1

# Now we got the name, we will need to delete the last 2 elements of the list 
# They will never be part of the manufacturer name

manufacturerList = manufacturerList[:len(manufacturerList) - 2]

# Finally, we have to convert the list to a string
nameManufacturer = ' '.join(manufacturerList)

# Final output

print("--------------------------------")
print(f"-> MAC Address: {macAddress}")
print(f"-> MAC OUI: {vendorNumber}")
print(f"-> Manufacturer name: {nameManufacturer}")
print("--------------------------------")

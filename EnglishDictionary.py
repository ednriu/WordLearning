from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore

#Constants
webUrl = 'https://dictionary.cambridge.org/dictionary/english-polish/' 


#Clear screen
os.system('cls' if os.name == 'nt' else 'clear')
#Input from user
searchedWord = input("Your Search:")
print("----------------------------")

url = webUrl + searchedWord
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
headers = {'User-Agent': user_agent}
web_request = requests.get(url, headers=headers)
soup = BeautifulSoup(web_request.text, "html.parser")
TextToFile = "\n\n-----------\n" + searchedWord + "\n"
print(Fore.BLUE+'MEANING:'+Fore.RESET)
if soup.find_all('div', class_='def ddef_d db'):
    counter = 1
    for ptag in soup.find_all('div', class_='def ddef_d db'):
        if counter>5:
            break
        wynik = ptag.text
        wynik = wynik.lstrip()        
        TextToFile = TextToFile + str(counter) +": " +wynik + "\n"
        print(str(counter) +": " +wynik)
        counter=counter+1
else:
    print("nothing found")
TextToFile = TextToFile + "\n"        
s = soup.find('div', attrs = {'class':'degs had lbt lb-cm'})
try:
    print("-----------")
    print(Fore.BLUE+'\nEXAMPLES:'+Fore.RESET)
    counter = 1
    for ptag in s.find_all('span', class_='deg'):
        if counter>5:
            break
        wynik = ptag.text
        wynik = wynik.lstrip()
        wynik = wynik.rstrip()
        wynik = wynik.replace(searchedWord, Fore.GREEN+searchedWord+Fore.RESET)
        TextToFile = TextToFile + str(counter) +": " +wynik + "\n"
        print(str(counter) +": " +wynik)
        counter=counter+1
except AttributeError as e:
    print("none")

if soup.find_all('div', class_='def ddef_d db'):    
    f = open('Printout.txt', 'a') 
    f.write(TextToFile)
    


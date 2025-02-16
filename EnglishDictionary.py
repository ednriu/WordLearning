from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore

class Translations():   
    
    def __init__(self, word):
        self.sentencesList = list()
        self.exampleList = list()
        self.word = word


    def addDefinition(self, sentence):
        sentence = sentence.lstrip()
        self.sentencesList.append(sentence)
    
    def getDefinition(self, sentenceNumber):
        sentenceNumber = sentenceNumber-1
        return self.sentencesList[sentenceNumber]
        
    def addExample(self, sentence):
        sentence = sentence.lstrip().rstrip()
        self.exampleList.append(sentence)
    
    def getExample(self, sentenceNumber):
        sentenceNumber = sentenceNumber-1
        return self.exampleList[sentenceNumber]

    def getExampleWithColoredWord(self, sentenceNumber, wordToColor):
        sentenceNumber = sentenceNumber-1
        wynik = self.exampleList[sentenceNumber]
        #wynik = wynik.replace(wordToColor+"s", Fore.GREEN+wordToColor+"s"+Fore.RESET)
        wynik = wynik.replace(wordToColor, Fore.GREEN+wordToColor+Fore.RESET)
        return wynik
        
    def max(self):
        return len(self.sentencesList)
    pass

#Constants
webUrl = 'https://dictionary.cambridge.org/dictionary/english-polish/' 


#Clear screen
os.system('cls' if os.name == 'nt' else 'clear')
#Input from user
searchedWord = input("Your Search:")
print("----------------------------")
#Object Constructor
translationInEnglish = Translations(searchedWord)

#base url + word means the WebPage target URL
url = webUrl + searchedWord

#Headers for BS4 parser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
headers = {'User-Agent': user_agent}
web_request = requests.get(url, headers=headers)
soup = BeautifulSoup(web_request.text, "html.parser")

#Header
print(Fore.BLUE+'MEANING:'+Fore.RESET)
TextToFile = "\n\n-----------\n" + searchedWord + "\n"

if soup.find_all('div', class_='def ddef_d db'):
    counter = 1
    for ptag in soup.find_all('div', class_='def ddef_d db'):
        if counter>5:
            break
        translationInEnglish.addDefinition(ptag.text)        
        print(str(counter) +": " + translationInEnglish.getDefinition(counter))
        TextToFile = TextToFile + str(counter) +": " +translationInEnglish.getDefinition(counter) + "\n"
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
        translationInEnglish.addExample(ptag.text)
        print(str(counter) +": " + translationInEnglish.getExampleWithColoredWord(counter,searchedWord))
        TextToFile = TextToFile + str(counter) +": " +translationInEnglish.getExample(counter) + "\n"
        counter=counter+1
except AttributeError as e:
   print("none")

#condition - if there is no reading error please save the file
if soup.find_all('div', class_='def ddef_d db'):    
    f = open('Printout.txt', 'a') 
    f.write(TextToFile)
    


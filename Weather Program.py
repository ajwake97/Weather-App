
import requests
import json
import time

#This is the API Key
API_KEY = "10b3ff178d347bb5e10cfee10deb2b63"

#This is the base URL 
baseUrl = "https://api.openweathermap.org/data/2.5/weather?"


#This prompts the user for the desired zipcdoe
def zipInput():
  zipCode = input("Enter the zipcode: ")

  #Sends a request to the openweathermaps.org and uses my API key and zipcode to return data

  response = requests.get((f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={API_KEY}'))
    
  #Prints the response and displays the returned data
  if response.status_code == 200:
    print('Connection Sucessful')
    time.sleep(2)
    print(json.dumps(response.json(), indent=1))
    reRun()
  if response.status_code != 200: #Displays connection issue if true
    print('Connection Unsuccessful')
    print('Zipcode Not Valid')
    try:
      zipCode() #retries zipcode function
    except:
      print('Error handling Zipcode')
      time.sleep(1)
      print('Please Rerun Program')
      time.sleep(1)
      print('Program Ending')
    exit() #closes program


def reRun(): #function allows user to rerun the program
  Y = input('\n\nWould you like to rerun this program? \nType "Yes" to input another zipcode. \ntype "Quit" to end program\n')
  while Y == "Yes":
   zipInput()
  while Y == "Quit":
      exit()

zipInput()
reRun()
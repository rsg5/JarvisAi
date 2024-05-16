import speech_recognition as sr
import os
import webbrowser
import genai
import wikipedia
import datetime
import pyttsx3
import google
import googlesearch
import requests
from bs4 import BeautifulSoup





def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        print("Please start speaking:")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"Chief said: {query}")
            return query
        except Exception as e:
            return "Sorry, I could not understand what you said"
def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        print("Good Morning, Chief!")
        say("Good Morning,Chief!")

    elif 12<=hour<17:
        print("Good Afternoon, Chief!")
        say("Good Afternoon,Chief!")

    else:
        print("Good Evening, Chief!")
        say("Good Evening,Chief!")

    print('Welcome Back! I am Jarvis! How Can I help You?')
    say("Welcome Back!  I am Jarvis! How Can I help You?")




def search_google(query):
    say("Searching Google...")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = soup.find_all("div", class_="tF2Cxc")
        if search_results:
            summary = ""
            for result in search_results:
                summary += result.find("span").text.strip() + " "
            print(f"According to Google: {summary}")

        else:
            print("Sorry, no results found.")

    else:
        print("Failed to retrieve search results from Google.")







if __name__ == '__main__':
    wishme()
    print("Listening...")
    query = takeCommand()
    if "Jarvis".lower() in query.lower():
        say("Yes?")
        continue_listening=True
        while continue_listening:
            print("Listening...")
            query = takeCommand()

            if "wikipedia".lower() in query.lower():
                say("Searching wikipedia...")
                query=query.replace("wikipedia", "")
                results=wikipedia.summary(query, sentences=3)
                print(f"According to wikipedia, {results}")
                say(f"According to wikipedia, {results}")
                continue
            if "google".lower() in query.lower():
                query = query.replace("google", "")
                search_google(query)
                continue
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["Linkedin",  "https://www.linkedin.com"],["twitter", "https://www.twitter.com"],["facebook", "https://www.facebook.com"],["instagram", "https://www.instagram.com"]]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} for you Chief...")
                    webbrowser.open(site[1])
                    continue
            songs=[["Song_1", r"Song_1_path"],["Song_2", r"Song_2_path"]]
            for song in songs:
                if f"Play {song[0]}".lower() in query.lower():
                    say(f"Playing {song[0]} for you Chief...")
                    os.system(f'start "" "{song[1]}"')
                    continue
            if "the time" in query:
                srfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Chief The time is {srfTime}")
                continue
            applications=[["app_1", r"app_1_path"],["app_2", r"app_2_path"],["app_3", r"app_3_path"],["app_4",r"app_4_path"]]
            for application in applications:
                if f"Open {application[0]}".lower() in query.lower():
                    say(f"Opening {application[0]} for you Chief...")
                    os.startfile(application[1])
                    break

            contacts=[["User_1","User_1_Phone_no."],["User_2","User_2_Phone_No."],["User_3","User_3_phone_no."],["User_4","User4_Phone_No."],["User_5","User_5_phone_no."],["User_6","User_6_Phone_no."]]
            for contact in contacts:
                if f"text {contact[0]}".lower() in query.lower():
                    say(f"Sending message to {contact[0]}")
                    try:
                        pywhatkit.sendwhatmsg_instantly(contact[1],"Message",15, True, 10)
                        print("Message was successfully sent. ")
                    except Exception as e:
                        print("Error in sending the message!")
                    break
            groups = [["grp_1", "grp_1_id"], ["grp_2","grp_2_id" ], ["grp_3","grp_3_id"]]
            for group in groups:
                if f"text {group[0]}".lower() in query.lower():
                    say(f"Sending message to {group[0]}")
                    try:
                        pywhatkit.sendwhatmsg_to_group_instantly(group[1],"Message",15, True, 10)
                        print("Message was successfully sent. ")
                    except Exception as e:
                        print("Error in sending the message!")
                    break
            mails = [["receiver_1", "receiver_1_email"], ["receiver_2", "receiver_2_email"]]
            for mail in mails:
                if f"email {mail[0]}".lower() in query.lower():
                    say(f"Sending email to {mail[0]}")
                    try:
                        pywhatkit.send_mail("sender_email","password","Subject","Message",mail[1])
                    except Exception as e:
                        print("Error in sending the mail!")
                    break
            fins=["bye","stop","end","finish"]
            for fin in fins:
                if f"ok {fin}".lower() in query.lower():
                    say("It was a pleasure working,with you Chief!")
                    continue_listening=False
                    break
    else:
        print("You would have to call JARVIS by name to wake him up!")






            #say(query)

import pywhatkit

try:
    pywhatkit.sendwhatmsg_instantly("+91 6290 965 989","This is an automated whatsapp message sent as a result of me trying a project. If you are are receiving this message then it means I was successful",15,True,10)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")
try:
    pywhatkit.sendwhatmsg_to_group_instantly("EKDHWQdG6ZWJwS7jvT1ORu","This is an automated whatsapp message sent as a result of me trying a project. If you are are receiving this message then it means I was successful",15,True,10)

except:
    print("Error in sendinThis is an automated whatsapp message sent as g the message!")
try:
    pywhatkit.sendwhats_image("EKDHWQdG6ZWJwS7jvT1ORu",r"C:\Users\RAHIL SENGUPTA\Desktop\artworks-000033841901-6m6a0u-t500x500.jpg", "Again checking if I can make Whatsapp send an image on it's own",15,True,30)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")

try:
    pywhatkit.sendwhats_image("+91 6290 965 989",r"C:\Users\RAHIL SENGUPTA\Desktop\artworks-000033841901-6m6a0u-t500x500.jpg", "Again checking if I can make Whatsapp send an image on it's own",15,True,30)
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")

try:
    pywhatkit.send_mail("rahilsengupta9@gmail.com","ysus vzhi nesr ltld","TEST","This is an automated email sent as a result of me trying a project. If you are are receiving this mail then it means I was successful","rahil.sengupta.ece24@heritageit.edu.in")
    print("Message was successfully sent. ")
except:
    print("Error in sending the message!")
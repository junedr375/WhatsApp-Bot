import tkinter as tk           
import time                    
import pandas as pd            
from selenium import webdriver 
import random as rd            
import os

#Main tkinter -- GUI
window = tk.Tk()
window.geometry('500x500')
window.title("WhatsBot-Automate WhatsApp")

 
#Function to process what happens after clicking submit.(backend)
def click():
    cnames_input=cnames_entry.get()
    m_input=messages_entry.get()
    
    fpath=fpath_entry.get()
    mpath=mpath_entry.get()
    print(fpath)
    print(mpath)
    print(var1.get())
    if(var1.get()==1):
        print("I am here A")
        if(fpath=="" and mpath==""):
            print("I am here B")
            all_names=cnames_input.split(",")
            replies=m_input.split(",")
            send_messages(all_names,replies)

        if(mpath=="" and fpath !=""):
            print("I am here C")
            df=pd.read_excel(fpath, dtype={'Numbers':str, 'Replies':str} )
            all_names = df['Numbers']    
            replies = df['Replies']
            send_messages(all_names,replies)

        else:
            print("I am here D")
            df=pd.read_excel(fpath, dtype={'Numbers':str} )
            all_names = df['Numbers']    
            replies = mpath
            send_messages_with_media(all_names,replies)
  
def send_messages(all_names,replies):
    count = int
    count = 0
    #Send message for each contact in the list
    for i in range(len(all_names)): 
        # Code to Find the Whatsapp Search Box to search contacts.
        ncicon = driver.find_element_by_xpath('//div[@title = "New chat"]')
        ncicon.click()

        search_box=driver.find_element_by_class_name('_2cLHw') 
        
        name=all_names[i]
        msg=replies[i]
        
        
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(search_box)
        actions.click()
        actions.send_keys(name)
        actions.perform()
          
        time.sleep(1)
        
        user = driver.find_element_by_class_name('_2FBdJ')
        user.click()
        
        #Finding Message box to enter message
        msg_box = driver.find_element_by_class_name('_1Plpp')
        
        #Typing the message
        msg_box.send_keys(msg)
        
        #Clicking the Send button 
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        count = count + 1
    msg = ""
    print("Total number of message sent is: {}".format(count))

def send_messages_with_media(all_names,replies):
    #Send message for each contact in the list
    count = int
    count = 0
    for i in range(len(all_names)): 
        
        #Code to Find the Whatsapp Search Box to search contacts.
        ncicon = driver.find_element_by_xpath('//div[@title = "New chat"]')
        ncicon.click()
        search_box=driver.find_element_by_class_name('_2cLHw') 
        
        name=all_names[i]
        msg=replies
        
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(search_box)
        actions.click()
        actions.send_keys(name)
        actions.perform()
          
        time.sleep(1)
        user = driver.find_element_by_class_name('_2FBdJ')
        user.click()
        
        #Finding Message box to enter message
        micon = driver.find_element_by_xpath('//div[@title = "Attach"]')
        micon.click()

        ivcon = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        ivcon.send_keys(msg)
        time.sleep(3)
        #Clicking the Send button 
        button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
        
        button.click()
        time.sleep(1)
        user = ""
        count = count + 1
    print("Total number of message sent is: {}".format(count))



#-----------MAIN--------------

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')



tk.Label(window, text="WhatsBot",width=25,font=("bold", 20)).place(x=80,y=53)

tk.Label(window, text="Contact Name(s)",width=20,font=("bold", 10)).place(x=80,y=150)
cnames_entry = tk.Entry(window)
cnames_entry.place(x=240,y=150)

tk.Label(window, text="Message(s)",width=20,font=("bold", 10)).place(x=68,y=200)

messages_entry = tk.Entry(window)
messages_entry.place(x=240,y=200)

tk.Label(window, text="(OR)",width=20,font=("bold", 13)).place(x=150,y=225)


tk.Label(window, text="Copy/Paste excel filepath",width=20,font=("bold", 10)).place(x=70,y=260)

fpath_entry = tk.Entry(window)
fpath_entry.place(x=240,y=260)

tk.Label(window, text="Copy/Paste Media filepath",width=20,font=("bold", 10)).place(x=70,y=290)

mpath_entry = tk.Entry(window)
mpath_entry.place(x=240,y=290)

var1 = tk.IntVar()
check=tk.Checkbutton(window, text="I have scanned the QR code and read the instructions.",width=43,font=("bold", 10),variable=var1).place(x=68,y=340)

tk.Button(window, text='Submit', command=click, width=20,bg='green',fg='white').place(x=180,y=380)

window.mainloop()
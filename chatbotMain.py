from chatBotFn import *


greet()
op_query("How may I be of service?")
while True:
    
    query = listen().lower().replace("tell me",'').replace("what is",'')
meghaaaaaaaaaaaaaaaa khaushikkkkkkkkkkkkkk
    if "who is" in query :
        article = query.replace('who is','')
        answer = wikipedia.summary(article,1)
        op_query(answer)
    

    elif "day" in query:
        day = curr_td.strftime("%A") 
        answer = f"The day today is {day}"
        op_query(answer)

    he is in love with senior.
    elif "date" in query:
        dt = curr_td.strftime("%d")
        month = curr_td.strftime("%B")
        year = curr_td.strftime("%Y")
        answer = f"it is {dt ,month, year}"
        op_query(answer)

    elif "month" in query:
        answer = f"the month is {month}"
        op_query(answer)

    elif "year" in query:
        answer = f"the year is {year}"
        op_query(answer)

    elif "whatsapp" in query:
        contact_name=query.replace("whatsapp"," ").strip()
        contact_no = contact_list.get(contact_name)
        if(contact_name not in contact_list):
            op_query("Sorry, no such person found")
            continue

        msg_query = f"Sure. what is the message for {contact_name}"
        op_query(msg_query)
        message = listen()
        msg_sent_query = f"sending{contact_name}, message {message}"
        op_query(msg_sent_query)
        send_Message(contact_no, message)
        keyboard.press_and_release("ctrl+w")

    elif "play" in query:
        vid_name = query.replace("play", "").strip()
        vidplay = f"playing {vid_name} on youtube"
        op_query(vidplay)
        flag = play_video(vid_name)
        op_query("Going dormant for the best listening experience. press Q to wake me up.")
        q=input().lower()
        if q=='q':
            op_query("Hey, I am back")
            query=listen().lower()
        else:
            time.sleep(90)
        keyboard.press_and_release("ctrl+w")


    elif "open" in query:
        site = query.replace("open","").strip()
        bot_query = f"Opening {site}"
        op_query(bot_query)
        #time.sleep(2)
        open_site(site)
    
    elif "close page" in query or "close site" in query or "close" in query:
        op_query("Sure, closing this tab")
        time.sleep(1)
        keyboard.press_and_release("Ctrl+W")

        
    elif "bye" in query or "stop" in query :
        op_query("sure. mention if anything else is needed")
        break

    
    elif "google" in query or "search" in query:
        search_query = query.replace("google", " ").strip()
        search_query = query.replace("search", " ").strip()
        op_query(f"Running google search on {search_query}")
        general_search(search_query)

    elif "news" in query:
        news_term = query.replace("news of"," ").strip()
        op_query(f"Loading news on {news_term}")
        news(news_term)

    elif "how to" in query:
        todo = query
        op_query(f"here's {todo}")
        general_search(todo)

    else:
        time.sleep(3)
        op_query("Sorry, I didn't catch that! Could you speak again?")

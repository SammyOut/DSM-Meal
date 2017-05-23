import fbchat
import parsing
import time


class MealBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        meal = 0
        t = time.localtime()
        dayn = t.tm_mday
        if(not('당진' in message or '호서' in message or '서야'in message or '정보' in message)) :
            if str(author_id) != str(self.uid) :
                if ('의견' in message or '아침' in message or '점심'in message or '저녁' in message or '조식' in message or '중식' in message or '석식' in message or '모레' in message or '내일' in message or '밥' in message or '급식' in message) : 
    
                    if ('의견' in message) :
                        f = open("opinion.txt", 'a')
                        f.write(message+'\n')
                        f.close()
                        self.send(100004765026222, "의견이 추가됨.")
                        self.send(author_id, "의견이 전송되었습니다.")
                    
                    else :
                        if ('아침' in message or '조식' in message) : meal = 1
                        elif ('점심'in message or '중식' in message) : meal = 2
                        elif ('저녁' in message or '석식' in message) : meal = 3
    
                        if ('모레' in message) : dayn += 2
                        elif('내일' in message) : dayn += 1
                        
                        elif ('일' in message) :
                            index = message.find('일')
                            if (message[index-1]>='0' and message[index-1]<='9') : n = int(message[index-1])
                            if (message[index-2]>='0' and message[index-2]<'9') : n += int(message[index-2])*10
                            if (n < 32) : dayn = n

                        self.send(author_id, parsing.bab(dayn, meal)+'meal')

                message = ''

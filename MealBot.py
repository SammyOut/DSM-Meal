import fbchat
import parsing
import time

t = time.localtime()

class MealBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        meal = 0
        dayn = t.tm_mday

        if str(author_id) != str(self.uid) :
            if ('의견' in message or '아침' in message or '점심'in message or '저녁' in message or '모레' in message or '내일' in message or '밥' in messageor or '급식' in message) : 

                if ('의견' in message) :
                    f = open("opinion.txt", 'a')
                    f.write(message+'\n')
                    f.close()
                    self.send(100004765026222, "의견이 추가됨")
                    self.send(author_id, "의견이 전송되었습니다.")
                    
                else :
                    if ('아침' in message) : meal = 1
                    elif ('점심'in message) : meal = 2
                    elif ('저녁' in message) : meal = 3
                    if ('모레' in message) : dayn += 2
                    elif('내일' in message) : dayn += 1
                    self.send(author_id, parsing.bab(dayn, meal))

            message = ''

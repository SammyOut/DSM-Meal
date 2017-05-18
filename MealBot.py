import fbchat
import parsing

command = '모레 : 내일모레 하루 급식 메뉴 출력\n내일 : 내일 하루 급식 메뉴 출력\n아침 : 오늘 아침 급식 메뉴 출력\n점심 : 오늘 점심 급식 메뉴 출력\n저녁 : 오늘 저녁 급식 메뉴 출력\n급식, 밥 : 오늘 하루 급식 메뉴 출력'
class MealBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        if str(author_id) != str(self.uid) :
            if ('호서'in message) :
                if('내일' in message) :
                    self.send(author_id, parsing.htomo())
                elif ('밥' in message or '급식' in message) :
                    self.send(author_id,parsing.htoday())
                    
            elif('당진' in message) :
                if('내일' in message) :
                    self.send(author_id, parsing.dtomo())
                elif ('밥' in message or '급식' in message) :
                    self.send(author_id,parsing.dtoday())

            elif ('모레'in message) :
                    self.send(author_id, parsing.day2())    
            elif('내일' in message) :
                    self.send(author_id, parsing.tomorrow())
            elif ('아침' in message) :
                self.send(author_id, parsing.breakfast())
            elif ('점심' in message) :
                self.send(author_id, parsing.lunch())
            elif ('저녁' in message) :
                self.send(author_id, parsing.dinner())
            elif ('밥' in message or '급식' in message) :
                self.send(author_id,parsing.breakfast()+parsing.lunch()+parsing.dinner())
            elif ('명령어' in message) :
                self.send(author_id,command)
        message = ''

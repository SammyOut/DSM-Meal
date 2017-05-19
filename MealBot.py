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
            if ('모레'in message) : self.send(author_id, parsing.tt())
            
            elif('내일' in message) :
                if ('아침' in message) : self.send(author_id, parsing.tb())
                elif ('점심' in message) : self.send(author_id, parsing.tl())
                elif ('저녁' in message) : self.send(author_id, parsing.td())
                else : self.send(author_id,parsing.tom())

            elif ('아침' in message) : self.send(author_id, parsing.br())
            elif ('점심' in message) : self.send(author_id, parsing.lu())
            elif ('저녁' in message) : self.send(author_id, parsing.di())
            elif ('오늘' in message or'밥' in message or '급식' in message) :self.send(author_id,parsing.tod())

            elif ('명령어' in message) :self.send(author_id,command)

        message = ''

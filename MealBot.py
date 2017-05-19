import fbchat
import parsing

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

            elif ('오늘' in message ) :
                if ('아침' in message) : self.send(author_id, parsing.br())
                elif ('점심' in message) : self.send(author_id, parsing.lu())
                elif ('저녁' in message) : self.send(author_id, parsing.di())
                else : self.send(author_id,parsing.tod())
                
            elif ('아침' in message) : self.send(author_id, parsing.br())
            elif ('점심' in message) : self.send(author_id, parsing.lu())
            elif ('저녁' in message) : self.send(author_id, parsing.di())

        message = ''

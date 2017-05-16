import fbchat
import parsing

class MealBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        if (message.find('아침')+1) :
            self.send(author_id, parsing.breakfast())
        elif (message.find('점심')+1) :
            self.send(author_id, parsing.lunch())
        elif (message.find('저녁')+1) :
            self.send(author_id, parsing.dinner())
        elif (message.find('밥')+1 or message.find('급식')+1) :
            self.send(author_id,parsing.breakfast()+'\n'+parsing.lunch()+'\n'+parsing.dinner())
        message = ''

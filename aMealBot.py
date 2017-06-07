import fbchat
import aparsing
import time
import aweather
import aClub

clublist = aClub.clublist()

class MealBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        meal = 0
        school = 0
        t = time.localtime()
        dayn = t.tm_mday
        if str(author_id) != str(self.uid) :
            if ('의견' in message or '아침' in message or '점심'in message or
                '저녁' in message or '조식' in message or '중식' in message or
                '석식' in message or '모레' in message or '내일' in message or
                '밥' in message or '급식' in message or '오늘' in message or
                '날씨' in message or '동아리' in message) : 
    
                    if ('의견' in message) :
                        f = open("opinion.txt", 'a')
                        f.write(message+'\n')
                        f.close()
                        self.send(100004765026222, "의견이 추가됨.")
                        self.send(author_id, "의견이 전송되었습니다.")
                        return 0
                    
                    elif('날씨' in message) :
                        self.send(author_id, aweather.cWeahter())

                    elif('동아리' in message) :
                        if ('목록' in message or '목록' in message) :
                            self.send(author_id, '\n'.join(clublist))
                        else :
                            for a in clublist :
                                if(a in message) :
                                    self.send(author_id, aClub.club(a))
                        
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
                            if (n < 32) :
                                dayn = n
                                return 0;
                            else : self.send(author_id, '올바른 날짜를 입력하세요')
                        if ('당진' in message) : school = 1
                        elif('호서' in message) : school = 2
                        elif('서야' in message) : school = 3
                        elif('정보' in message) :
                            school = 4
                            if ('아침' in message or'조식' in message) :
                                self.send(author_id, '조식이 제공되지 않습니다.')
                                return 0;
                            if ('점심'in message or '중식' in message) : meal = 1
                            elif ('저녁' in message or '석식' in message) : meal = 2
                        elif('면천' in message) :
                            school = 5
                            if ('아침' in message or'조식' in message) :
                                self.send(author_id, '조식이 제공되지 않습니다.')
                                return 0;
                            if ('점심' in message or '중식'in message) :meal = 1
                            if ('저녁' in message or'석식' in message) :
                                self.send(author_id, '조식이 제공되지 않습니다.')
                                return 0;

                        try :
                            self.send(author_id, aparsing.bab(school, dayn, meal))
                        except IndexError:
                            self.send(author_id, '정보가 없습니다.')
                        message = ''
        if (author_id == '100011977455211') : self.send(100011977455211, '승걸이가 체코얏~!')

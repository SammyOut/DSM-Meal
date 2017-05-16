import MealBot
import getpass

bot = MealBot.MealBot("dsmmeal@naver.com", getpass.getpass())
bot.listen()

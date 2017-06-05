import aMealBot
import getpass

bot = aMealBot.MealBot("sm372182@gmail.com", getpass.getpass())
bot.listen()

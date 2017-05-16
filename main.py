import MealBot
import getpass

bot = MealBot.MealBot("sm372182@gmail.com", getpass.getpass())
bot.listen()

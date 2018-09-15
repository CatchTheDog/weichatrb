from wxpy import *
tuling = Tuling(api_key=u'0baba7aacf934557a68b19d0984f0bef')
bot = Bot(cache_path=True)
friend_sel = bot.friends().search("蒋文丽")[0]
my_friend = ensure_one(bot.search("蒋文丽"))

@bot.register(my_friend)
def reply_my_friend(msg):
    reply = tuling.do_reply(msg)
    print("问答：", msg, reply)
bot.join()
from wxpy import *
bot = Bot(cache_path=True)
tuling = Tuling(api_key=u'0baba7aacf934557a68b19d0984f0bef')

@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    reply = tuling.do_reply(msg)
    print("问答：",msg,reply)
bot.join()
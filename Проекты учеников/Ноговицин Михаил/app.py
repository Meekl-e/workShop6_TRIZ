from telebot import TeleBot, types

bot  = TeleBot("7412069843:AAE84qnr3WCvlqtu8w5TD1CFRj1DRLAUv4Y")

messages = {}




@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот ТРИЗ. Напишите вашу задачу")
    messages[message.from_user.id] = {}


@bot.message_handler(content_types=["text"])
def func(msg):

    if messages[msg.from_user.id].get("goal") is not None:
        messages[msg.from_user.id]["roles"] = msg.text.split()
        for role in messages[msg.from_user.id]["roles"]:
            for res in messages[msg.from_user.id]["resources"]:
                buttons = types.InlineKeyboardMarkup()
                yes = types.InlineKeyboardButton("Да ✅", callback_data=f"yes_{role}_{res}")
                no = types.InlineKeyboardButton("Нет ❌", callback_data="no")
                buttons.add(yes, no)
                bot.send_message(msg.chat.id, f"Подходит ли нам {res} на роль {role}?", reply_markup=buttons)
        messages[msg.from_user.id]["all_ques"] = len(messages[msg.from_user.id]["roles"]) * len(messages[msg.from_user.id]["resources"])
        messages[msg.from_user.id]["cur_ques"] = 0
    elif messages[msg.from_user.id].get("resources") is not None:
        messages[msg.from_user.id]["goal"] = msg.text
        bot.send_message(msg.chat.id, f"Спасибо! Напишите роли в нашей задаче через пробел.")
    elif messages[msg.from_user.id].get("task") is not None:
        messages[msg.from_user.id]["resources"] = msg.text.split()
        bot.send_message(msg.chat.id, f"Спасибо! А зачем нам {messages[msg.from_user.id]['task']}?")
    elif messages[msg.from_user.id] == {}:
        messages[msg.from_user.id]["task"] = msg.text
        bot.send_message(msg.chat.id, "Спасибо! Напишите ресурсы через пробел.")





@bot.callback_query_handler(func= lambda callback:callback.data[:3] == "yes")
def yes_f(callback):
    if messages[callback.from_user.id].get("results") is None:
        messages[callback.from_user.id]["results"] = []
    _, role, res = callback.data.split("_")
    messages[callback.from_user.id]["results"].append(f"Использовать {res} на роль {role}.")
    check(callback)
    return True

@bot.callback_query_handler(func= lambda callback:callback.data == "no")
def yes_f(callback):
    check(callback)
    return True


def check(callback):

    bot.edit_message_text("Спасибо!",callback.message.chat.id, callback.message.id )
    if messages[callback.from_user.id].get("cur_ques") is None:
        bot.send_message(callback.message.chat.id, "Введите задачу")
        return True
    messages[callback.from_user.id]["cur_ques"] +=1
    if messages[callback.from_user.id]["cur_ques"] >= messages[callback.from_user.id]["all_ques"]:
        bot.send_message(callback.message.chat.id, f'{messages[callback.from_user.id]["task"]} произойдет само собой')
        bot.send_message(callback.message.chat.id, f'{messages[callback.from_user.id]["task"]} производить не надо')
        bot.send_message(callback.message.chat.id, f'{messages[callback.from_user.id]["task"]} производить не надо, а достигнуть цели {messages[callback.from_user.id]["goal"]} другим путем')
        for res in messages[callback.from_user.id]["resources"]:
            bot.send_message(callback.message.chat.id, f'{messages[callback.from_user.id]["task"]} произоизвести с помощью {res}')


        for line in messages[callback.from_user.id]["results"]:
            bot.send_message(callback.message.chat.id, line)
        messages.pop(callback.from_user.id)



if __name__ == "__main__":
    bot.infinity_polling()


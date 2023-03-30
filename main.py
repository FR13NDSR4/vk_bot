import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token = input("your token: \n")

bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def blasthack(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': random.randint(1, 9999999999)})


print("server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id

            if message == 'привет':
                blasthack(id, 'Привет, я бот!')

                blasthack(id, "название любой игры")
                answer_1 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_1["items"] == []:
                    answer_1 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_1 = answer_1["items"][0]["last_message"]["text"]

                blasthack(id, "название места")
                answer_2 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_2["items"] == []:
                    answer_2 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_2 = answer_2["items"][0]["last_message"]["text"]

                blasthack(id, "название предмета")
                answer_3 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_3["items"] == []:
                    answer_3 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_3 = answer_3["items"][0]["last_message"]["text"]

                blasthack(id, "название ещё одного предмета")
                answer_4 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_4["items"] == []:
                    answer_4 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_4 = answer_4["items"][0]["last_message"]["text"]

                blasthack(id, "название чего либо")
                answer_5 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_5["items"] == []:
                    answer_5 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_5 = answer_5["items"][0]["last_message"]["text"]

                blasthack(id, "ещё чего-нибудь")
                answer_6 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_6["items"] == []:
                    answer_6 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_6 = answer_6["items"][0]["last_message"]["text"]

                blasthack(id, "и последнее")
                answer_7 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                while answer_7["items"] == []:
                    answer_7 = bh.method('messages.getConversations', {"count": 1, "filter": "unanswered"})
                else:
                    answer_7 = answer_7["items"][0]["last_message"]["text"]

                a1 = "Жили-были старик со старухой у самого синего моря"
                a2 = "Старуха играла в  " + str(answer_1) +  " старик ловил рыбу. Однажды забросил он невод в море, вытащил его, а в нем " + str(answer_2) + " золотая рыбка."
                a3 = "Ну, что молчишь? - молвила рыбка.- Ты Герасим? Говори желание!"
                a4 = "Эх, корыто у старухи развалилось! Давай стиральную машину, что ли... Будет тебе стиральная машина! - сказала рыбка."
                a5 = "А что еще? Давай еще " + str(answer_3) + " и " + str(answer_4)
                a6 = "Отпустил старик рыбку в море, пошел домой, и видит рядом со своей избушкой такую картину:"
                a7 = "стоит " + str(answer_5) + " на нём " + str(answer_7) + " еще выше " + str(answer_6) + " а на самой верхушке стоит его старуха и боится пошевельнуться."
                a8 = "Что-то перепутала рыбка, - подумал старик. - Но прикольно получилось! Цирк, да и только!"

                blasthack(id, a1)
                blasthack(id, a2)
                blasthack(id, a3)
                blasthack(id, a4)
                blasthack(id, a5)
                blasthack(id, a6)
                blasthack(id, a7)
                blasthack(id, a8)

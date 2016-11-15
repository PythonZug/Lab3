import vk
import time
import datetime

print('VKBot')

# Авторизуем сессию с помощью access токена
session = vk.Session('38289b389f503e3c9aed1b100ea3900b710812ea2ec161a1148db2292f68c0ca922f83cbb46937847a63b')

# Создаем объект API
api = vk.API(session)

while (True):
    # Получим 20 последних входящих сообщений
    messages = api.messages.get()

    # Создадим список поддерживаемых комманд
    commands = ['help', 'weather', 'hello', 'пака', 'привет']

    # Найдем среди них непрочитанные сообщения с поддерживаемыми командами
    # таким образом получим список в формате [(1d_пользователя, id_сообщения, команда), ...]
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    # Отвечаем на полученные команды
    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        # Сформируем строку с датой и временем сервера
        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot vO.1\n>Разработал: Pavel')

        if comand == 'weather':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Погода отличная!')
        if comand == 'hello':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot vO.1\n>Здаров фраер')
        if comand == 'пака':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot vO.1\n>ага давй\nпака')
        if comand == 'привет':
            api.messages.send(user_id=user_id,
                              message='\nЗдаров фраер')

    # Формируем список id всех сообщений с командами через запятую
    ids = ', '.join([str(m[1]) for m in messages])

    # Помечаем полученные сообщения как прочитанные
    if ids:
        api.messages.markAsRead(message_ids=ids)

    # Проверяем сообщения каждые 3 секунды
    time.sleep(3)

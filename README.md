# UDP-chat

Концепция взаимодействия клиент-серверных программ с использованием UDP сокетов:
Для передачи данных используются датаграммы.

Процесс подготовительных действий для сервера и используемые системные вызовы (на примере Linux):
1.	создание UDP сокета (socket);
2.	связывание с номером порта и IP-адресом сетевого интерфейса (bind);
3.	настройка адреса сокета;
4.	прием сообщений (recvfrom);
5.	обработка поступившей информации, отправка ответа (sendto), продолжение прослушивания.

Для клиента выполняются аналогичные действия.
Для передачи данных по сети используется сетевой порядок байт (big-endian), это должно учитываться на хостах. Для передачи вещественных чисел данные преобразуются в другие типы. IP адрес преобразуется из символьного представления в числовое.
При указании адреса используется конкретный адрес сетевого интерфейса или константа INADDR_ANY, для привязки ко всей системе.

Реализация клиента и сервера на языке Python (используются другие вызовы):

[![](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/start_server.png)](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/start_server.png "Запуск сервера чата")
> Запуск сервера чата

[![](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/messages_on_server.png)](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/messages_on_server.png "Сообщения, поступающие на сервер")
> Сообщения, поступающие на сервер

[![](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/first_client_message.png)](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/first_client_message.png "Сообщения первого клиента")
> Сообщения первого клиента

[![](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/second_client_message.png)](https://github.com/SemikAlexander/UDP-chat/blob/master/Images/second_client_message.png "Сообщения второго клиента")
> Сообщения второго клиента

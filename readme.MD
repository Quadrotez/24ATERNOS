# 24Aternos

<p>Этот бот способен поддерживать ваш сервер на хостинге <a href="https://aternos.org">Aternos</a> бесконечно, 24/7<p>

<h2>Подготовления к работе</h2>
<p>Для начала работы вам требуется:</p>

<ol>
<li><a href="https://sky.pro/media/kak-ustanovit-python-na-razlichnyh-operaczionnyh-sistemah/">Установить Python</a><br></li>
<li>Скачать проект к себе на устройство и распаковать в любую свободную папку</li>
<li><a href="https://nodejs.org/en">Загрузить Node.js</a> и установить <br>
P. S. Для Linux обычно подходит выполнение команды "apt install npm". Если не получается, ищите в интернете</li>
<li>Открыть cmd (win+r и в строку ввести cmd)</li>
<li>Вводите следующие команды:</li>
    <ul>
    

<li>Проверка установки компонентов. Если у вас не высвечивается версия, значит вы сделали что-то не так.<br>
P. S. Если у вас Linux, напишите python3 вместо python</li> 

```bash
npm --v
python --v
```

<li>Установка библиотеки mineflayer</li>

```bash
npm install mineflayer
```

<li>Установка библиотек. Для этого нужно перейти в директорию, куда вы распаковали проект

```bash
cd путь/к/вашему/файлу
```

Или можно установить вручную
P. S. Если у вас Linux, напишите pip3 вместо pip</li> 
```bash
pip isntall configparser
pip install javascript
pip install tkinter
pip install threading
pip install install os
pip install sys
pip install mineflayer
```
</li>




</ul>

<li>Далее приступаем к самому интересному. Создаём файл config.ini и вписываем туда значения по данному шаблону:

Токен для бота в Telegram вы можете получить в <a href="https://helpdesk.bitrix24.ru/open/17538378/">BotFather</a>

```config.ini
[SECURITY]
token=Ваш токен бота


[SERVER]
host=Имя вашего хоста (Всё, что до двоеточия)
port=Порт сервера (Всё, что после двоеточия)
[BOT]
name=Имя для вашего бота
[COMMAND]
;Здесь вы можете управлять тем, какие команды нужно отправлять в сам чат майнкрафта
;для получения ответа.
position=.pos
start=.start
stop=.stop
```


</li>

<li>Готово! Осталось запустить "main.py".

[//]: # (Следующий пласт документации как раз посвящён ему)

</li>        

</ol>



'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.'''

import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding'])
    print(line)

ARGS_2 = ['ping', 'youtube.com']
YA_PING_2 = subprocess.Popen(ARGS_2, stdout=subprocess.PIPE)
for line in YA_PING_2.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding'])
    print(line)

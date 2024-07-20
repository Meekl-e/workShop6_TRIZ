# Репозиторий Ноговицина Михаила
## Структура проекта
1. `app.py` - прототип ТРИЗ-ассистента в телеграмм боте 
2. `decoder.py` -  декодировщик задачи `task.json` с использованием модели Word2Vec
3. `nn_analyze.py` - backend часть сайта, отвечающая за анализ Word2Vec
4. `model.bin`, `model.txt`, `udpipe_syntagrus.model` - файлы для работы Word2Vec
5. `old` - старые проекты

## Cборка и запуск
Чтобы запустить Word2Vec необходимо:
1. Скачать модель `python download_model.py`
2. Запустить `python decoder.py`
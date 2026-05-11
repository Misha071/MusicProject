# MusicScope
Анализ музыкальных прослушиваний пользователей

## Description
MusicScope — это Python-проект для анализа музыкальных данных на основе CSV-файла с историей прослушиваний пользователей.

Проект позволяет исследовать музыкальные предпочтения, активность пользователей, популярные жанры и исполнителей, а также выявлять закономерности во времени прослушивания.

## Data
Датасет содержит информацию о музыкальных прослушиваниях пользователей:

- `user_id` — идентификатор пользователя
- `track` — название трека
- `artist` — исполнитель
- `genre` — жанр
- `duration` — длительность трека в секундах
- `timestamp` — дата и время прослушивания

Дополнительно в процессе обработки создаются новые признаки:

- `date` — дата прослушивания
- `hour` — час прослушивания
- `day_name` — день недели
- `duration_min` — длительность трека в минутах

## Stack
- Python
- pandas
- numpy
- pytest
- argparse

## How to use

### Basic commands
```bash
python3 main.py info
python3 main.py genres
python3 main.py artists
python3 main.py users
python3 main.py duration
python3 main.py hours
python3 main.py days
python3 main.py genre-duration
python3 main.py report

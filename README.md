

# NEW_TRAINING_BOT

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-aiogram-brightgreen)

NEW_TRAINING_BOT - это телеграм-бот, разработанный для помощи в организации тренировок и фитнеса. Он предоставляет пользователю возможность создавать тренировочные планы, получать рекомендации по упражнениям и питанию(план питания можно редактровать и самому пользователю).

## Функциональности
- Создание и сохранение тренировочных планов: Пользователи могут создавать персонализированные тренировочные планы, указывая название упражнения, описание и ссылку на видео с ним(можно загружать на ютуб видео с закрытым доступом по ссылке).
- Рекомендации по упражнениям: Бот предоставляет пользователю рекомендации и описания различных упражнений в зависимости от цели и предпочтений пользователей.

## Какие функции я хочу добавить позже. Это мой первый проект после изучения языка Python и тд. Поэтому, пришлось разбираться во всем самому. 
- Отслеживание прогресса: Пользователи могут записывать свои тренировки, а бот будет отслеживать прогресс и предоставлять статистику для каждой тренировки.
- Установка уведомлений: Пользователи могут установить уведомления для напоминания о тренировках в определенное время.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/AluHadj22/NEW_TRAINING_BOT.git
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и заполните его необходимыми переменными окружения:

```bash
TOKEN=<ваш_токен>
```

## Использование

1. Запустите бота:

```bash
python bot.py
```

2. В телеграме найдите бота `@your_bot_name` и нажмите на кнопку "Start" или введите команду `/start`.

3. Следуйте указаниям бота для создания своего тренировочного плана, установки уведомлений и получения рекомендаций по упражнениям.

## Вклад

Если вы хотите внести свой вклад в развитие проекта, вы можете сделать следующее:

- Создайте форк репозитория.
- Создайте новую ветку для ваших изменений: `git checkout -b feature/new-feature`.
- Внесите необходимые изменения и сделайте коммиты: `git commit -m 'Add new feature'`.
- Запушьте вашу ветку: `git push origin feature/new-feature`.
- Создайте pull request в исходный репозиторий.

## Лицензия

[MIT](LICENSE)




# NEW_TRAINING_BOT

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-aiogram-brightgreen)
![Json](https://img.shields.io/badge/Json-orange)
![SQLite](https://img.shields.io/badge/SQLite-blue)



NEW_TRAINING_BOT - это телеграм-бот, разработанный для помощи в организации тренировок и фитнеса. Он предоставляет пользователю возможность создавать тренировочные планы, получать рекомендации по упражнениям и питанию(план питания можно редактровать и самому пользователю).

## Функциональности
- Создание и сохранение тренировочных планов: Пользователи могут создавать персонализированные тренировочные планы, указывая название упражнения, описание и ссылку на видео с ним(можно загружать на ютуб видео с закрытым доступом по ссылке).
- Рекомендации по упражнениям: Бот предоставляет пользователю рекомендации и описания различных упражнений в зависимости от цели и предпочтений пользователей.
- Можно посчитать правильный дефицит калорий, который зависит от вашего желания(Похудеть с миниимальной потеряй в мышцах, похудеть быстро, похудеть постепенно). Для этого, нажмите кнопку '/calories'
- Можно получить план питания нажав на кнопку Menu. Его тоже можно редактровать и заносить в базу данных.
- Для того, чтобы создать свой план питания и план тренировок, нужно добавить в созданную вами группу ТГ бота и дать ему админку. После, напишите в чате группы '/moderator'
- После того, как вы написали '/moderator', в ЛС придет сообщение от бота. Перейдите туда и у вас появятся кнопки '/load_menu' и '/load_TRAINING. Нажав, вам нужно следовать инструкциям бота. Если же вы хотите отменить редактрование, то напишите '/cancel'

## Какие функции я хочу добавить позже. 
- Отслеживание прогресса: Пользователи могут записывать свои тренировки, а бот будет отслеживать прогресс и предоставлять статистику для каждой тренировки.

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


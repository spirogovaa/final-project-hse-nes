# final-project-hse-nes

Привет! В этом проекте я бы хотела сделать проект на довольно ненаучную тему - астрологию. Дело в том, что есть те, [кто](https://www.livemint.com/Sundayapp/zDSjhU5IzcuI7ypo6W4WtL/Why-data-science-is-simply-the-new-astrology.html) считает, что data science is simply the new astrology, и я бы хотела проверить совместимость астрологии и data science в своем проекте. Моя цель - показать наглядно, что "незыблемые истины", которые можно найти в различных астрологических сайтах, на данных не проверяются. 

Ну, и конечно, в конце я подготовила для вас самый научный гороскоп на сегодня!


Основной вопрос: влияет ли знак зодиака на жизнь человека?

Мой план на проект - проверить ключевые показатели жизни людей на зависимость от знака зодиака: 
1. Партнер. Астрологи всегда предсказывают, что есть более и менее совместимые знаки зодиака. Мы проверим на основе статистики разводов и знаков зодиака разводящихся, есть ли какая-то тенденция между знаком зодиака партнера и успехом отношений.
2. Уровень счастья. Влияет ли знак зодиака на то, счастливы мы или нет? Я смотрю на современные данные - предсказания гороскопов для лета 2022 года. Астрологи всегда предсказывают на какой-то период (месяц\год\полгода\квартал) разную степень успеха и уровень "удачливости" для каждого знака зодиака. Если они правы, то мы заметим на данных гороскопов на неделю, что какие-то знаки зодиака более счастливые в этот период, а какие-то - менее.
3. Продолжительность жизни, причина смерти, профессия. На данных знаменитостей проверим, есть ли связь между знаком зодиака и показателями выше. 

Таким образом, мы затронем важные аспекты жизни человека и сможем сделать вывод о том, проверяются ли гипотезы астрологии на реальных данных. И наконец, узнаем, какой гороскоп предначертан звездами вам сегодня. :)

Основной файл: [horoscopes_project pirogova.ipynb](https://github.com/spirogovaa/final-project-hse-nes/blob/main/horoscopes_project%20pirogova.ipynb). 
Используемые датасеты:
1. divorces_2000-2015_translated.csv - здесь содержится информация о разводах с 2000 по 2015 год в городе Xalapa, Mexico, а также знаках зодиака супругов.
2. famous_dates.csv - с датой рождения и знаками зодиака знаменитостей.
3. famous_occupation (беру из API kaggle) - с датой рождения и знаками зодиака знаменитостей.
4. horoscope.csv - "базовый" датасет гороскопов. Он предоставляет еженедельный гороскоп для всех знаков зодиака, с конца июня 2022 года. 
5. kaggle.json для использования датасета famous_occupation
6. midnight.otf - шрифт для мистического гороскопа

Пошаговый план проекта:
1. Анализ совместимостей знаков зодиака, визуализация статистики по частоте совместимости, взятой из двух разных датасетов. Проверка того, противоречат ли данные астрологическим принципам
2. Анализ настроения == успеха \ удачи \ счастья различных знаков зодиака. Визуализация распределения уровня настроения для каждого знака зодиака за последние 9 месяцев. Проверка наличия или отсутствия "выбросов" в виде особенно счастливых или несчастливых предсказываемых знаков зодиака.
3. Проверка двусторонних гипотез на тестах хи-квадрат на наличие \ отсутствие зависимости выбора профессии и причины смерти от знака зодиака. Техническое сравнение MSE-score на предмет того, сильное ли различие в прогнозе модели линейной регрессии дает признак "знак зодиака", а не номер месяца.
4. Предоставление собственного гороскопа в Streamlit :)


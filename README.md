# tz

## Общие вопросы:
### 1) 8/10
Считаю, что знания требуют дальнейшего оттачивания.

### 2) 7/10
Владею общими навыками google sheets

## Логика 1:
Дано: 

- Дневной бюджет: 40$;
- К полудню потрачено 50% от изначальной суммы;
- К закрытию потрачено 80% от оставшейся суммы;

Найти:

Оставшуюся сумму от дневного бюджета.

Решение:
1. Найдем сумму, потраченную к полудню:
<p align="center">
    $\frac{40 * 50}{100} = 20$ $
</p>

    
2. Найдем сумму, потраченную от полудня до момента закрытия:

   
   <p align="center">
    $\frac{20 * 80}{100} = 16$ $
</p>

3. Определим остаток от дневного бюджета к концу рабочего дня:

   
   <p align="center">
    $20 - 16 = 4$ $
</p>

Ответ: 4 доллара.


## Логика 2:
Представим условие задачи в виде таблицы.
| Число компаний                         | Дней работы  | Кол-во часов в день часов  | Бюджет                  |
|----------------------------------|---------------|---------------|-----------------------------|
| 5            | 24             | 6             | 120                           |
| 9             | X             | 8             | 210                          |

Найти:

Неизвестную переменную X.

1. Найдем общее количество рабочих часов для первых 5 кампаний:

<p align="center">
    $всего\ часов = компании \times дни \times часы\ в\ день$
</p>

<p align="center">
    $всего\ часов = 5 \times 24 \times 6 = 720$ часов. 
</p>

2. Стоимость одного часа работы:


<p align="center">
    $цена\ часа = \frac{бюджет}{часы}$
</p>

<p align="center">
    $цена\ часа = \frac{120}{720} = 0.1667$  долларов/час. 
</p>




3. Найдем количество часов, которое можно оплатить, имея бюджет 216 долларов:

<p align="center">
    $новые\ часы = \frac{новый\ бюджет}{цена\ часа}$
</p>

<p align="center">
    $новые\ часы = \frac{216}{0.1667} = 1296$ часов. 
</p>




4. Найдем количество дней для 9 кампаний, работающих по 8 часов в день:
<p align="center">
    $новые\ дни = \frac{всего\ часов}{компании \times часы\ в\ день}$
</p>

<p align="center">
    $новые\ дни = \frac{1296}{9 \times 8} = 18$ дней.
</p>

Ответ: 18 дней.





## Логика 3:

Дано:

- Всего 200 баннеров;
- Для каждого рекламного баннера, который использовался в обеих кампаниях, приходится 3 баннера, которые использовались только в кампании №2;
- 60 баннеров использовались только в кампании №1;
- 80 баннеров не использовались ни в одной из кампаний.

Найти:

Количество баннеров, которое было использовано в обеих рекламных кампаниях.

Решение:
1. За $x$ обозначим количество баннеров в обеих компаниях, следовательно, баннеров для кампании №2 получим $3x$. 

2. Найдем общее количество использованных баннеров:

<p align="center">
    $использованные\ баннеры = всего\ баннеров − неиспользованные\ баннеры$
</p>

<p align="center">
    $использованные\ баннеры = 200 - 80 = 120$
</p>

3. Составим уравнение для поиска количества баннеров в обеих рекламных кампаниях. Общее уравнение будет выглядеть следующим образом:

<p align="center">
    $кампания\ 1 + кампания\ 2 + обе кампании = использованные баннеры$.
</p>

Подставим значения и получим:

<p align="center">
    $60 + 3x + x = 120$;
</p>    
<p align="center">
    $4x = 120 - 60$;
</p>    
<p align="center">
    $4x = 60$;
</p>
<p align="center">
    $x = \frac{60}{4}$;
</p>    
<p align="center">
    $x = 15$.
</p>

Ответ: 15 баннеров было использовано в обеих рекламный кампаниях.



  







## Логика 4:

Определим кто из людей использует 2 из 3 соцсетей и чьи предпочтения совпадают. Введем таблицу для наглядности:

| имя                         | инстаграм  | фейсбук | Ютуб                  |
|-----------------------------|---------------|---------------|-----------------------------|
|  Энн             | 1             | 0            | 1                          |
|  Джон 🟩             | 0             | 1 🟩             | 1    🟩                       |
|  Кейт 🟩            | 0             | 1  🟩           | 1   🟩                        |
|  Том             | 1             | 1             | 0                           |

Ответ: предпочтения совпадают у Джона и Кейт.


## Логика 5:
Дано: 
- Средний балл за 4 модуля: 78.

Найти:

Количество баллов нужно получить стажеру за 5-й модуль, чтобы средний балл по всему заданию составил 80.

Решение:

1. Найдем сумму баллов за 4 модуля:
<p align="center">
    $сумма\ за\ 4\ модуля = средний\ балл \times количество\ модулей$
</p>

<p align="center">
    $сумма\ за\ 4\ модуля = 78 \times 4 = 312$
</p>

2. Составим уравнение с учетом 5-го модуля. За $x$ обозначим модуль №5:

<p align="center">
    $сумма\ за\ 5\ модуль = x + 312$
</p>

3. Т.к. из условия задания имеем, что средний балл по всему заданию должен быть равен 80, составим уравнение для поиска количества баллов, нужных студенту за 5-й модуль. Решим уравнение:

<p align="center">
    $\frac{x+312}{5} = 80$;
</p>
<p align="center">
    $x + 312 = 80 \times 5$;
</p>
<p align="center">
    $x = 400 - 312$;
</p>
<p align="center">
    $x = 88$.
</p>

Ответ: для выполнения условия задачи за пятый модуль студент должен получить 88 баллов.


## Логика 6:

Дано:

- Расстояние: 260 км.
- Ср. скорость туда: 80 км/ч.
- Ср. скорость обратно: 100 км/ч.

Найти: 
Насколько в минутах обратный путь быстрее.

Решение:
1. Найдем время на путь туда:
<p align="center">
    $260/80 = 3.25$ часа $= 195$ минут.
</p>


2. Найдет время на путь обратно:


<p align="center">
    $260/100 = 2.6$ часа $= 156$ минут.
</p>


3. Найдем разницу между ними, что даст нам ответ на задание:

<p align="center">
    $195 - 156 = 39$ минут.
</p>



Ответ: на 39 минут обратный путь быстрее.

## Техническое задание
- Выручка за июль 2021: 757830.7399999996
- Лучший менеджер в сентябре 2021: Петрова
- Преобладающий тип сделки в октябре 2021: текущая
- Оригиналов договоров по майским сделкам в июне: 76
- Бонусы менеджеров:
<p align="center">
    | Менеджер    | Бонусы |
    |------------|----------------|
    | Андреев    | 30974.1520 |
    | Васильев   | 7273.8295  |
    | Иванов     | 24758.0960 |
    | Кузнецова  | 18713.4427 |
    | Михайлов   | 607.0680   |
    | Петрова    | 34782.4562 |
    | Попов      | 0.0000     |
    | Селиванов  | 7455.7790  |
    | Смирнов    | 34151.8620 |
    | Соколов    | 3730.7090  |
    | Филимонова | 11240.2135 |
</p>

- Остаток на 01.07.2021:

<p align="center">
    | Менеджер    | Остаток бонусов |
    |------------|----------------|
    | Андреев    | 26175.9483 |
    | Васильев   | 6934.5985  |
    | Иванов     | 22254.2570 |
    | Кузнецова  | 16108.7711 |
    | Михайлов   | 607.0680   |
    | Петрова    | 27753.6542 |
    | Селиванов  | 7102.4570  |
    | Смирнов    | 30073.1380 |
    | Соколов    | 3730.7090  |
    | Филимонова | 10830.5305 |
</p>

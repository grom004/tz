# tz

## Общие вопросы:
### 1) 8/10
Считаю, что знания требуют дальнейшего оттачивания.

### 2) 

## Логика 1:
Дано: 

- Дневной бюджет: 40$;
- К полудню потрачено 50% от изначальной суммы;
- К закрытию потрачено 80% от оставшейся суммы;

Найти оставшуюся сумму от дневного бюджета.

Решение:
1. Найдем сумму, потраченную к полудню:

    $40 * 50 / 100 = 20$ $
2. Найдем сумму, потраченную от полудня до момента закрытия:

   $20 * 80 / 100 = 16$ $
3. Определим остаток от дневного бюджета к концу рабочего дня:

   $20 - 16 = 4$ $

Ответ: 4 доллара.


## Логика 2:
Представим условие задачи в виде таблицы.
| Число компаний                         | Дней работы  | Кол-во часов в день часов  | Бюджет                  |
|----------------------------------|---------------|---------------|-----------------------------|
| 5            | 24             | 6             | 120                           |
| 9             | X             | 8             | 210                          |

Нужно найти неизвестную переменную X.

1. Найдем общее количество рабочих часов для первых 5 кампаний:

$всегочасов = компании \times дни \times часывдень$

$всегочасов = 5 \times 24 \times 6 = 720$ часов. 

2. Стоимость одного часа работы:

$цена\ часа = \frac{бюджет}{часы}$

$цена\ часа = \frac{120}{720} = 0.1667$  долларов/час. 

3. Найдем количество часов, которое можно оплатить, имея бюджет 216 долларов:

$новыечасы = \frac{новый\ бюджет}{цена\ часа}$

$новые\ часы = \frac{216}{0.1667} = 1296$ часов. 

4. Найдем количество дней для 9 кампаний, работающих по 8 часов в день:

$новые\ дни = \frac{всего\ часов}{компании \times часывдень}$

$новые дни = \frac{1296}{9 \times 8} = 18$ дней.

Ответ: 18 дней.

## Логика 4:

Определим кто из людей использует 2 из 3 соцсетей и чьи предпочтения совпадают. Введем таблицу для наглядности:

| имя                         | инстаграм  | фейсбук | Ютуб                  |
|-----------------------------|---------------|---------------|-----------------------------|
|  Энн             | 1             | 0            | 1                          |
|  Джон 🟩             | 0             | 1 🟩             | 1    🟩                       |
|  Кейт 🟩            | 0             | 1  🟩           | 1   🟩                        |
|  Том             | 1             | 1             | 0                           |

Ответ: предпочтения совпадают у Джона и Кейт.

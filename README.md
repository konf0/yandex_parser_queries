Парсер поисковой выдачи яндекса по популярным запросам компании sravni.ru. 
Главная задача была посмотреть по каким запросам домены находятся в топе поисковой выдачи и сколько трафика рекламного, а сколько органического.
В начале мы берем нужный список запросов из Postgre, с помощью selenium открываем каждый запрос и добавляем в Dataframe : Запрос , Домен, Тип рекламы и Дату.
Дальше отправляем эти данные в postgre и там ранжируем их по позиции в выдаче.
Теперь у нас есть данные для визуализации. Собираем дэшборд в Datalans
![image](https://github.com/konf0/yandex_parser_queries/assets/123234615/b07e843e-8b88-4154-aa5f-66f4b70ba6a2)
Среднее место домена в выдаче: Это поможет оценить его конкурентоспособность. Домен sravni.ru оказался лучше остальных , хотя в среднем и не находится на самых первых позициях. 
Потому что у него в балансе находятся оба типа трафика, значит около 50% трафика приходит органически. 

Популярные домены: мы можем увидеть, какие домены, связанные с sravni.ru, наиболее популярны. Это может помочь нам понять, какие темы или продукты наиболее востребованы.

Изменения в поисковой выдаче: Мы можете отследить, как менялась позиция домена sravni.ru в поисковой выдаче со временем. Это может помочь  понять, как изменяется популярность и конкурентоспособность домена.

Отношение органической и рекламной выдачи: Мы можете увидеть, как соотносятся органическая и рекламная выдача для доменов sravni. Это может помочь оценить эффективность рекламных кампаний.

Сколько раз домены sravni был на первой позиции: мы можете увидеть, сколько раз домены sravni занимали первую позицию в поисковой выдаче. Это может помочь  оценить его конкурентоспособность и видимость.



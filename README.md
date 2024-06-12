
Парсер поисковой выдачи Яндекса по популярным запросам компании Sravni.ru был создан для анализа популярности и эффективности домена. Основная цель - понять, по каким запросам домены находятся в топе поисковой выдачи и сколько трафика рекламного, а сколько органического.

Для начала, был создан список запросов, который был получен из Postgre, далее  с помощью Selenium открываем каждый запрос. Затем, каждый запрос добавлен в Dataframe, который содержал информацию о запросе, домене, типе рекламы и дате.

После этого, данные были отправлены в Postgre, где они были ранжированы по позиции в выдаче. Это позволило получить данные для визуализации в Datalans.
![image](https://github.com/konf0/yandex_parser_queries/assets/123234615/b07e843e-8b88-4154-aa5f-66f4b70ba6a2)

Среднее место домена в выдаче помогает оценить его конкурентоспособность. Домен Sravni.ru оказался лучше остальных, хотя в среднем и не находится на самых первых позициях. Это связано с тем, что у него в балансе находятся оба типа трафика, что означает, что около 50% трафика приходит органически.

Популярные домены помогают понять, какие домены, связанные с Sravni.ru, наиболее популярны. Это может помочь определить, какие темы или продукты наиболее востребованы.

Изменения в поисковой выдаче позволяют отследить, как менялась позиция домена Sravni.ru в поисковой выдаче со временем. Это помогает понять, как изменяется популярность и конкурентоспособность домена.

Отношение органической и рекламной выдачи помогает оценить эффективность рекламных кампаний. Можно увидеть, как соотносятся органическая и рекламная выдача для доменов Sravni.

Сколько раз домены Sravni были на первой позиции помогает оценить его конкурентоспособность и видимость. Это позволяет увидеть, сколько раз домены Sravni занимали первую позицию в поисковой выдаче.


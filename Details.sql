drop table if exists details;
create table if not exists details(
	name VARCHAR(250) primary key,
	type VARCHAR(250),
	quantity INT);

/* Добавить детали */
insert into details (name, type, quantity) values
('ААА', 'Тип А', 10),
('БББ', 'Тип Б', 2),
('ВВВ', 'Тип Б', 4);

/* Вывести все детали */
select * from details;

/* Вывести деталь по имени */
select * from details
where name = 'БББ';

/* Вставить одну строку */
insert into details (name, type, quantity) values
('ГГГ', 'Тип Г', 100);

/* Удалить строку по имени */
delete from details where name = 'ГГГ';

/* Агригация по типу */
SELECT 
    type,
    COUNT(*) as "Кол-во записей",
    ROUND(AVG(quantity), 2) as "Среднее кол-во деталей"
FROM details
GROUP BY type
order by 1;


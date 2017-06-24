create table dangdang.products
(
	id int not null auto_increment
		primary key,
	link varchar(255),
	isbn varchar(200) not null comment '',
	title varchar(200)  ,
	subtitle varchar(200)  ,
	author varchar(200)  ,
	publisher varchar(200),
	description text,
	category_1 varchar(200),
	category_2 varchar(200),
	category_3 varchar(200),
	price decimal(10,2),
	sell_price decimal(10,2),
	status int default 0
);

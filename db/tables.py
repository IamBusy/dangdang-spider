# -*-coding:utf-8 -*-
from sqlalchemy import Table, Column, INTEGER, String
from db.basic_db import metadata

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

# 登陆帐号表 login_info
product = Table("product", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("link", String(255), default=''),
                   Column("isbn", String(200), default=''),
                   Column("title", String(200), default=''),
                   Column("subtitle", String(200), default=''),
                   Column("author", String(200), default=''),
                   Column("publisher", String(200), default=''),
                   Column("description", String(200), default=''),
                   Column("category_1", String(200), default=''),
                   Column("category_2", String(200), default=''),
                   Column("category_3", String(200), default=''),
                   Column("price", DECIMAL(10，2), default='0'),
                   Column("sell_price", DECIMAL(10，2), default='0'),
                   Column("status", INTEGER, default='0'),
                   )

__all__ = ['product']
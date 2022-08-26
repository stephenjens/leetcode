-- 08/25/2022 13:38	Accepted	662 ms	0B	mysql
-- this seems like a pretty janky way to melt/un-pivot a table. apparently some
-- dbs have an UNPIVOT() function. mysql does not.
select product_id, 'store1' as store, store1 as price from products
where store1 is not null
union
select product_id, 'store2' as store, store2 as price from products
where store2 is not null
union
select product_id, 'store3' as store, store3 as price from products
where store3 is not null;

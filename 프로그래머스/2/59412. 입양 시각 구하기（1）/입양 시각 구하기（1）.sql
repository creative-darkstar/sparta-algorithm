select * from
(
    select
    date_format(DATETIME, '%H') as HOUR,
    count(*) as COUNT
    from ANIMAL_OUTS
    group by HOUR
    order by HOUR asc
) tmp
where HOUR >= 9 and HOUR < 20
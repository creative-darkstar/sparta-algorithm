select CATEGORY, count(CATEGORY) as PRODUCTS
from
(
    select
    left(PRODUCT_CODE, 2) as CATEGORY
    from PRODUCT
) as temp
group by CATEGORY
order by CATEGORY asc
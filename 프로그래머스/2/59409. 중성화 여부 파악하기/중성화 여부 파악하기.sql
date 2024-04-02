select
ANIMAL_ID,
NAME,
(
    CASE
    WHEN (SEX_UPON_INTAKE like '%Neutered%') or (SEX_UPON_INTAKE like '%Spayed%')
    THEN 'O'
    ELSE 'X'
    END
) as '중성화'
from ANIMAL_INS
order by ANIMAL_ID
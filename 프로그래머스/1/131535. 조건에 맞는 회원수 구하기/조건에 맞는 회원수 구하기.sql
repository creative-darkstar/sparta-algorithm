select count(USER_ID) from USER_INFO
where (AGE >= 20 and AGE <= 29)
and date_format(JOINED, '%Y') = '2021'
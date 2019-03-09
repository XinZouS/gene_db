-- select * from company

-- SELECT Name, TO_CHAR(InceptDt, 'mm/dd/yyyy')
-- FROM company 

SELECT DATE_FORMAT(InceptDt, '%m/%d/%Y %H:%i') as InceptDt, c.* FROM company c

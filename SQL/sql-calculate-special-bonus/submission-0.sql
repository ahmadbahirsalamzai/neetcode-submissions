select
    employee_id,
    CASE
        when employee_id % 2 = 1 and name not like 'M%' then salary
        else 0
    END as bonus
FROM employees 
order by employee_id
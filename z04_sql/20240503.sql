-- [ 1 ] �������(Employees) ���̺���
-- �����ȣ, �̸�, �޿�, �μ�, �Ի���, ����� �����ȣ�� ����Ͻÿ�.
-- �̶� �̸��� �̸��� ������ �����Ͽ� Name�̶�� ��Ī���� ����Ͻÿ�(107��).
select employee_id,emp_name ||'/'||job_id as Name,salary,department_id,hire_date,manager_id
from employees;
--[ 2 ] �������(Employees) ���̺���
-- ����� �̸��� Name, ������ Job, �޿��� Salary, ������ $100�� ���ʽ��� �߰��Ͽ� ����� ���� Increase Ann_Salary,
-- �޿��� $100 ���ʽ��� �߰��Ͽ� ����� ������ Increase Salary��� ��Ī�� �ٿ� ����Ͻÿ�(107��).
select emp_name as Name,job_id as Job,salary,salary*100*12 "Increase Salary"
from employees;
-- [ 3 ] H R �μ����� ���� �� ������ �޿� ���� ������ �ۼ��Ϸ��� �Ѵ�.
-- �������(Employees) ���̺��� �޿��� $7,000~$10,000 ���� �̿��� �����
-- �̸� �� �޿��� �޿��� ���� ������ ����Ͻÿ�(75��).
select emp_name,salary from employees
where salary<7000 or salary > 10000
order by salary
;
--- ������ 7000���� ũ�� 10000 ���� ���
select emp_name,salary from employees
where salary between 7000 and 10000
;
-- not�� ��� �ݴ����� ���
select emp_name,salary from employees
where salary not between 7000 and 10000
order by salary asc
;
-- [ 4 ] ����� �̸�(emp_name) �߿� ��e�� �� ��o�� ���ڰ� ���Ե� ����� ����Ͻÿ�.
-- �̶� �Ӹ����� ��e or o Name���̶�� ����Ͻÿ�(8��).
select emp_name from employees
where lower(emp_name) like '%o%' or lower(emp_name) like '%e%'
order by emp_name;
-- [ 5 ] �̹� �б⿡ 60�� IT �μ������� �ű� ���α׷��� �����ϰ� �����Ͽ� ȸ�翡 �����Ͽ���.
-- �̿� �ش� �μ��� ��� �޿��� 12.3% �λ��ϱ�� �Ͽ���.
-- 60�� IT �μ� ����� �޿��� 12.3% �λ��Ͽ� ������(�ݿø�) ǥ���ϴ� ������ �ۼ��Ͻÿ�.
-- ������ �����ȣ, �̸�(Name���� ��Ī), �޿�, �λ�� �޿�(Increase Salary�� ��Ī)������ ����Ͻÿ�(5��).
select employee_id,emp_name as Name,department_id,salary,round(salary+salary*0.123) from employees
where department_id = 60
;
-- [ 6 ] ��� ����� ������ ǥ���ϴ� ������ �ۼ��Ϸ��� �Ѵ�.
-- ������ ����� �̸�, �޿�, ���翩�ο� ���� ������ �����Ͽ� ����Ͻÿ�.
-- ���翩�δ� ������ ������ ��Salary + Commission��,
-- ������ ������ ��Salary only����� ǥ���ϰ�, ��Ī�� ������ ���̽ÿ�.
-- ���� ��� �� ������ ���� ������ �����Ͻÿ�(107��).
select emp_name,salary,salary+salary*nvl(commission_pct,0) as comm_salary,
commission_pct,
-- 1. case when then
-- case when commission_pct is null then 'Salary only'
-- when commission_pct is not null then 'Salary + Commission'
-- end as "commission_isNull"
-- 2. decode
-- decode(commission_pct,null,'Salary only','Salary + Commission')
-- decode ( department_id,
-- '10','A',
-- '20','B',
-- '30','C' ) as dept
-- 3. nvl2
nvl2(commission_pct,'Salary + Commission','Salary only')
from employees
order by salary desc
;
-- [ 7 ] �� ����� �Ҽӵ� �μ����� �޿� �հ�, �޿� ���, �޿� �ִ�, �޿� �ּڰ��� �����ϰ��� �Ѵ�.
-- ���� ��°��� ���� �ڸ��� �� �ڸ� ���б�ȣ-õ����, $ ǥ�ÿ� �Բ� �Ʒ��� ���� ����Ͻÿ�.
-- ��, �μ��� �Ҽӵ��� ���� ����� ���� ������ �����ϰ�,
-- ��� �� �Ӹ����� "�׷��Լ���"�� ��Ī(alias) ó���Ͻÿ�(11��).
select department_id,
to_char(sum(salary),'$000,999,999') sum_sal,
to_char(round(avg(salary),2),'$000,999,999') avg_sal,
to_char(max(salary),'$000,999,999') max_sal,
to_char(min(salary),'$000,999,999') min_sal
from employees
group by department_id
;
-- [ 8 ] ������� ����(job_id)�� ��ü �޿� ����� $10,000���� ū ��츦 ��ȸ�Ͽ� ���޺� �޿� ����� ����Ͻÿ�.
-- �� ������ ���(CLERK)�� ���Ե� ���� �����ϰ� ��ü �޿� ����� ���� ������� ����Ͻÿ�(7��).
select job_id,avg(salary) from employees
where job_id not like '%CLERK%'
-- �Ϲ��÷��� ������ �ִ� ��
group by job_id
having -- �׷��÷��� ������ �ִ� ��
avg(salary)>10000
;
-- outer join
-- [ 9 ] �� ����� ���� ������ ���踦 �̿��Ͽ� ������ ���� ������ ������ �ۼ��ϰ��� �Ѵ�.
-- (��) ȫ�浿�� ��տ��� �����Ѵ� �� Eleni Zlotkey �������� -> Steven King
-- � ����� �������� �����ϴ��� �� ���� �����Ͽ� ����Ͻÿ�.
-- ��, ������ ��簡 ���� ����� �ִٸ� �� ������ �����Ͽ� ����Ͻÿ�. (107��).
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+)
;
-- [ 10 ] Employees, Departments ���̺��� ������ �ľ��� ��
-- ��� ���� �ټ� �� �̻��� �μ��� �μ��̸��� ��� ���� ����Ͻÿ�.
-- �̶� ��� ���� ���� ������ �����Ͻÿ�(5��).
-- 1. �μ���ȣ,�����
-- 2. ����� >= 5
-- 3. ������� ����
select department_id,count(department_id)
from employees
group by department_id
having count(department_id)>=5
order by count(department_id) desc
;
-- [ �߰� ] HR �μ��� � ����� �޿������� ��ȸ�ϴ� ������ �ð� �ִ�.
-- Tucker�� ���Ե� ������� �޿��� ���� �ް� �ִ� ����� �̸�, ����, �޿��� ����Ͻÿ�(15��).
select salary from employees
where emp_name like '%Tucker%'
;
select salary from employees
where salary > (select salary from employees
where emp_name like '%Tucker%')
;
-- ��ü��� �����̻��� ����� ���� ���
select salary from employees
where salary > (select avg(salary) from employees)
order by salary desc
;
-- [ �߰� ] ��� ����� �ҼӺμ� ��տ����� ����Ͽ� ������� �̸�, ����,
-- �޿�, �μ���ȣ, �μ���տ���(Department Avg Salary�� ��Ī)�� ����Ͻÿ�(107��).
select avg(salary) from employees;
-- join
select salary,a.department_id,avg_salary
from employees a, (select department_id,round(avg(salary),2) avg_salary from employees group by department_id ) b
where a.department_id = b.department_id
;
select emp_name from
(select * from employees where salary>(select avg(salary) from employees) )
where emp_name like '%a%'
;
select * from employees where salary>(select avg(salary) from employees);
-- equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id
;
select emp_name,job_id,salary,department_id ,
(
select round(avg(salary),2) from employees a
where department_id = e.department_id
)
from employees e;
--
select round(avg(salary),2) from employees a
where department_id = 10;

select * from daum_movie;

select * from coupang;

--img ũ�⺯�� 
alter table daum_movie modify img varchar2(300);
alter table coupang modify img varchar2(300);

CREATE TABLE flight (
fno NUMBER(4) PRIMARY KEY,
airline VARCHAR2(100),
departure_time DATE,
arrival_time DATE,
flight_time VARCHAR2(20),
price NUMBER(10)
);

select * from flight;


























;
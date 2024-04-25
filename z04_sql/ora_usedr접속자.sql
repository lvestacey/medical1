-- 어제, 오늘, 내일 
select sysdate-1,sysdate, sysdate+1 from dual;

-- 오늘, 이달의 첫일, 이달의 마지막일 
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- 두날짜간 일수 
select trunc(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2)from employees;

--trunc 일단위 버림
select trunc(kor,-1)kor,count(trunc(kor,-1))from stu_score
group by trunc(kor,-1)
order by kor;

-- 퀴즈 hire_date날짜에서 월만 출력하시오. 
-- 2208-01-01
select to_char(hire_date, 'yyyy-mm-dd') from employees;
select to_char(hire_date, 'mm') from employees;

select to_char(hire_date,'mm') hire_date, count(to_char(hire_Date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

-- 퀴즈, hire_date 
select to_char(hire_date,'yyyy') hire_date, count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

-- 형변환 -number, charcater, date
-- number 사칙연산가능, 쉼표표시안됨, 원화표시안됨
-- char 사칙연산(+,-)안됨. 쉽표표시가능, 원화표시가능 
-- date +,-가능 날짜출력형태는 변경불가 

-- 시퀀스, 날짜의 년도를 가지고 학번을 부여하시오. 
-- stu_seq시퀀스를 가지고 5개 학번을 출력해보세요.
-- ko+2024+0001
select 'ko'||'2024'||'0001' from dual;
select 'kor'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;

--문자형 
-- 123,456,789, 156,778, 더하기값 
--(123,456,789)+(100,000)=123456789
select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) from dual; 
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999')) as result from dual;

-- 숫자타입으로 날짜타입으로 변경
select 20240425+3 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425+3) from dual;

-- 숫자타입을 날짜타입으로 변경
select emp_name,hire_date from employees
where hire_date >to_date(20070101)
order by hire_date;

-- 퀴즈. 08월 입사일이면서, 사원이름 2번째에 a가 들어가 있는 사람을 출력하시오.
-- 1. 입사 
select emp_name, hire_date from employees
where to_char(hire_date,'mm')='08' and emp_name like '_a%'
order by emp_name;

select hire_date from employees
where to_char(hire_date,'mm')in('01','05','08');

-- 2. 이름 
select emp_name from employees
where emp_name like '_a%';

-- 3. 
select emp_name from employees
where emp_name like '_a%' and to_char(hire_date,'mm')in('01','05','08')
order by hire_date;

--퀴즈. 20070101이후 입사한 사원이름 2번째에 a가 들어가 있는 사람을 출력하시오. 
select emp_name, hire_date from employees
where hire_date >to_date(20070101) and emp_name like '%a%'
order by emp_name;

-- 문자타입을 날짜타입으로 변경 
select sysdate-to_date('20240401') from dual;

select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;

select * from m_date;

insert into m_date (m_no,m_yesterday,m_today,m_tomorrow) values(
seq_mno.nextval,'2024-04-01',sysdate,sysdate-to_date('2024-04-01')
);

-- seq_m_no 시퀀스 생성
create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- 테이블생성 date,timestamp
create table m_date (
m_no number(4),
m_yesterday date,m_today date,m_tomorrow date,m_year date
);

-- 1개 row 저장
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year) values (
seq_m_no.nextval, sysdate-1,sysdate,sysdate+1,sysdate+365 
);
-- 검색
select * from m_date;

create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number 
);

-- 
insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);

select * from eventDate;

select to_number('20,000','99,999')-to_number('10,000','99,999')from dual;

select salary, commission_pct,salary+(salary*commission_pct) from employees;

select manager_id from employees
order by manager_id desc;

select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;
--개수 함수 
select count (*) from employees;
select count(emp_name) from employees;

select count(manager_id) from employees;

select emp_name,manager_id from employees;

select sum(salary) from employees;

select avg(salary) from employees;

select avg(salary) avg_sal from employees;

select min(salary),max(salary) from employees;

-- 퀴즈. 6461달러보다 높은 사람을 출력하시오. 
select emp_name,salary from employees
where salary > (select avg(salary) avg_sal from employees);

select emp_name,min(salary) from employees;

-- 퀴즈 최소월급을 받는 사람의 사번, 이름을 출력하시오. 
select employee_id, emp_name,salary from employees
where salary =(select min(salary) from employees);

-- 퀴즈 최대월급 받는 사람의 사번, 이름을 출력하시오. 
select employee_id, emp_name,salary from employees
where salary =(select max(salary) from employees);

--부서번호가 50번인 사원만 전체월급 
select department_id,salary from employees;

select sum(salary) from employees
where department_id='100';

select count(*) from stu_score;

-- 퀴즈. stu_score kor점수가 80점이상인 학생을 출력하시오. 
select kor from stu_score
where kor>=80;

-- 퀴즈. 국어점수에서 국어점수 평균이상, 영어점수에서 영어점수 평균이상인 학생을 출력하시오. 
SELECT count(*) from stu_score
where kor >=(select avg(kor) from stu_score)
and eng>=(select avg(eng) from stu_score);

create table s_info(
sno number,
s_count number
);

insert into s_info values (
stu_seq.nextval,1000
);

insert into s_info values (
stu_seq.nextval,2000
);

insert into s_info values (
stu_seq.nextval,(select count(*) from stu_score
where kor >=(select avg(kor) from stu_score)
and eng>=(select avg(eng) from stu_score))
);

select * from s_info;

-- 퀴즈. 월급이 최대, 최소, 평균인 사원을 출력하시오. 
-- 3명 출력 
select * from employees
where salary=(select max(salary) from employees)
or salary=(select min(salary) from employees)
or salary=(select avg(salary) from employees)
;
-- 최대값 
select emp_name,salary from employees
where salary =(select max (salary) from employees);

-- 평균값보다 낮은사원 중에 최대값인 사원을 출력하시오
-- 1. 평균값보다 사원을 검색
-- 2. 검색된 사원중에 최대값을 검색 
select emp_name,salary from employees
where salary=6400;

select emp_name,salary from employees
where salary=(
select max(salary) from(
select emp_name, salary from employees
where salary<=(select avg(salary) from employees)
order by salary desc
)
);

-- 평균보다 낮은 값 107명 
--select max (salary) from 테이블 

--56명 최대값 6400 
select max (salary) from ( 
select emp_name, salary from employees
where salary<=(select avg(salary) from employees)
order by salary desc
);

select emp_name, salary from employees
where salary<=(select avg(salary) from employees)
order by salary desc;

-- 문자함수 
-- lpad, rpad 빈공백 채우기 
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name,rpad(emp_name,20,'@') from employees;

--ltrim, rtrim 지정한 문자를 잘라내고 출력 
select emp_name,ltrim(emp_name,'Do') from employees;

--ko20240001
select 'ko2024001',ltrim('ko20240001','ko2024') from dual;

-- substr(데이터,순서,개수) ex)substr ('abcdefg',3,3) -> cde 
select emp_name, substr(emp_name,3,4) from employees;

select job_id from employees;

-- 퀴즈. job_id 앞 두글자와 사원번호를 결합해서 출력하시오. 
select substr(job_id,0,2)||employee_id from employees;

SELECT department_name FROM departments;

-- length
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- 날짜함수 +,-가능, 날짜데이터 끼리 더하기는 안됨. 
-- 날짜데이터 + 숫자가능 
select sysdate+1 from dual;

-- 날짜 데이터 - 날짜데이터 가능 
select sysdate-hire_date from employees;

-- 날짜 데이터 +날짜데이터 불가능 
select sysdate+hire_date from employees;

select round(sysdate, 'month') from dual;

select sysdate,trunc (sysdate,'month'),round(sysdate,'month')from dual;

select round(sysdate,'year') from dual;

-- 개월수 추가, 축소 
select sysdate,add_months(sysdate,-2) from dual;

select emp_name, hire_date from employees;

--ceil 올림, floor 버림, mod나머지, power제곱 
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

-- 퀴즈. 사원명 입사일 출력 
SELECT TO_CHAR(TO_DATE('1979-09-19', 'YYYY-MM-DD'), 'YYYY"년" MM"월" DD"일"') || ' ' || TO_CHAR(TO_DATE('1979-09-19', 'YYYY-MM-DD'), 'DAY') AS HIRE_DATE
FROM DUAL;

select emp_name||to_char (hire_date, 'yyyy"년" mm"월" dd"일" day') from employees;

-- 퀴즈, 사원명, 자리수 9자리 빈공백 0으로 표시 
-- salar*1400 앞에 원화표시와 쉼표를 넣어 출력하시오. 
SELECT 'w' || TO_CHAR(salary*1400, '999,999,999') AS "salary"
FROM employees;

-- 자신의 생일과 자신의 생일이 속한 달의 마지막 날짜 
-- '2010-10-10'
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-01') from dual;

select * from member;

desc member;

--DDL(data definition langauage)-column추가 
-- 컬럼추가, 삭제 
-- commit,rollback이 안됨. 바로 저장됨. 
alter table member add gender varchar2(6) default 'female' not null;

select * from member;

update member set gender='male';

commit;

--컬럼삭제
alter table member drop column phone;
desc member;

-- 컬럼수정 - 컬럼이름변경
alter table member rename column name to stu_name
;
--타입변경 
alter table member modify(stu_name varchar2(50));

-- 기존의 데이터가 변경하려는 크기보다 작을때만 가능 
update member set stu_name='';
alter table member modify(stu_name varchar2(6));
--  컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나 null일때 가능 
alter table member modify(stu_name number(4));
select stu_name from member;

alter table member modify(stu_name number(100));
desc member;








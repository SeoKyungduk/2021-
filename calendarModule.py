#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 인수로 년도를 넘겨받아 윤년, 평년을 판단해서 윤년이면 True, 평년이면 False를 리턴하는 함수
# 윤년, 평년 판별식 => 년도가 4에 떨어지고 100에 떨어지지 않거나 400에 떨어지면 윤년
# return 값이 논리값(True 또는 False)인 함수의 이름은 'is'로 시작하는 것이 관행이다.
def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# In[21]:


# 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 함수
def lastDay(year, month):
    # 12달의 마지막 날짜를 기억하는 리스트를 만든다. => 일단 2월의 마지막 날짜는 28일로 초기화시킨다.
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2월의 마지막 날짜를 확정한다. => 윤년이면 29일로 수정한다.
    # if isLeapYear(year):
        # days[1] = 29
    days[1] = 29 if isLeapYear(year) else 28
    # 인수로 넘겨받은 우러에 해당되는 마지막 날짜를 출력한다.
    return days[month - 1]


# In[34]:


# 인수로 년, 월, 일을 넘겨받아 1년 1월 1일 부터 지나온 날짜의 합계를 리턴하는 함수
def totalDay(year, month, day):
    # 1년 1월 1일 부터 전년도 12월 31일까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도까지 지난 날짜의 합계에 전달까지 지난 날짜를 더한다.
    for i in range(1, month):
        total += lastDay(year, i)
    # 전달까지 지난 날짜에 일을 더해서 리턴시킨다.
    return total + day


# In[43]:


# 인수로 년, 월, 일을 넘겨받아 요일을 숫자로 리턴하는 함수
# 일요일(0), 월요일(1), 화욜일(2), 수요일(3), 목요일(4), 금요일(5), 토요일(6)
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# In[44]:


if __name__ == '__main__':
    print(isLeapYear(2021))
    print(lastDay(2021, 2))
    print(totalDay(2021, 8, 2))
    print(weekDay(2021, 8, 2))


# In[ ]:





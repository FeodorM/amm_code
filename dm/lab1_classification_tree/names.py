#!/usr/bin/env python3.5

code = "Код заявки"
date = "Дата выдачи"
age = "Возраст"
sex = "Заемщик.Пол"
condition = "СемейноеПоложение"
dependents = "Иждивенцы"
education = "Образование"
work = "Вид деятельности"
experience = "Стаж"
experience_gen = "Стаж общий"
revenue = "Белый доход"
revenue_per_month = "Месячный доход, руб."
credit = "Сумма кредита, тыс. руб."
monthly_payment = "Месячный платеж, руб."
expirations = "Просрочек свыше 60 дн."

names = [
    code
    , date
    , age
    , sex
    , condition
    , dependents
    , education
    , work
    , experience
    , experience_gen
    , revenue
    , revenue_per_month
    , credit
    , monthly_payment
    , expirations
]

features = names[:-1]

categories = [
    sex
    , date
    , condition
    , dependents
    , education
    , work
    , experience
    , experience_gen
    , revenue
]

dates = [date]

# code int64
# age int64
# revenue_per_month int64
# credit int64
# monthly_payment int64
# expirations int64

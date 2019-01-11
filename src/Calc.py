# -*- coding: utf-8 -*-

print("        ***        ")
print("Калькулятор ипотеки")
print("        ***      \n")

apartmentsPrice = input("Пожалуйста, введите стоимость квартиры: ")
creditPercent = input("Пожалуйста, введите процент по кредиту в формате 9.5: ")
monthlyPayment = float(input("Пожалуйста, введите сумму ежемясечного платежа: "))
initialPayment = input("Пожалуйста, введите сумму первоначального взноса: ")
insurancePercent = input("Пожалуйста, введите процент страховки: ")
incrementSalary = input("Пожалуйста, введите ежегодную индексацию ежемесячного взноса в процентах: ")

monthCount = 0
overPayment = 0
debt = float(apartmentsPrice) - float(initialPayment)


def get_month_credit_payback():
    return debt * (float(creditPercent) / 100) / 12  # хранит месячный долг банку


def get_month_insurance_payback():
    return debt * (float(insurancePercent) / 100) / 12


while debt != 0:
    monthCount += 1

    if monthCount % 12 == 0:
        monthlyPayment = monthlyPayment + monthlyPayment * (float(incrementSalary) / 100)

    monthPayback = get_month_credit_payback() + get_month_insurance_payback()
    overPayment += monthPayback
    clearPayment = monthlyPayment - monthPayback

    if clearPayment >= debt:
        debt = 0
    else:
        debt = debt - clearPayment

print("         ***                   ")

if monthCount < 12:
    print("Кредит будет погашен через %d месяца(-ев)" % monthCount)
else:
    yearCount = monthCount / 12
    month = monthCount % 12
    print("Кредит будет погашен через %d лет/год(-а) и %d месяца(-ев)" % (yearCount, month))

print("Сумма переплаты по кредиту будет равна: %d" % overPayment)

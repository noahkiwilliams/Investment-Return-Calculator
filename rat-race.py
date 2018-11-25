import math
import time

''' FORMULA TO DOLLAR COST AVERAGE A SUM EVERY YEAR INTO AN ASSET W/ X% RETURN '''
''' WELCOME TO THE RAT RACE... TIME TO TEST YOUR LUCK!!! '''

class rat(object):
    def __init__(self, name, income, rate, career):
        self.name = name
        self.income = income
        self.rate = rate
        self.career = career
        ## create RAT object...

    def annual_savings(self):
        annual_savings = self.income * self.rate * .01
        # print(str(annual_savings))
        return(annual_savings)

    def lifetime_savings(self):
        lifetime_savings = self.income * self.rate * self.career
        # print(str(lifetime_savings))
        return(lifetime_savings)

def dollar_cost_average(rat, investment_returns):
    current_balance = rat.annual_savings()

    for x in range (rat.career):
        a = x ## counter for year numbers
        x = round(current_balance, 3)
        rate_of_return = 1 + .01 * investment_returns
        new_balance = x * rate_of_return + rat.annual_savings()
        current_balance = new_balance
        print("YEAR:" + str(a + 1) + " = " + str(x)) ## print responses

print('\n')
print("WELCOME TO THE RAT RACE.")
print("NOTHING IS GUARANTEED, PROFIT IS THE PURPOSE, AND YOU HAVE NO RIGHTS.")
print("OBEDIENCE WILL BE REWARDED.")

print('\n')

print("THIS IS A CALCULATOR TO FIND THE RETURNS ON A PORTION OF INCOME DOLLAR-COST-AVERAGED INTO AN INVESTMENT WITH A CONSTANT ANNUAL RETURN.")
print("DOLLAR-COST-AVERAGING IS A METHOD OF INVESTING A CONSTANT AMOUNT AT SET INTERVALS TO PREVENT CATASTROPHIC LOSSES.")

print('\n')
print("*** DISCLAIMER: THESE RETURNS ARE THEORETICAL AND DO NOT REFLECT CURRENT FINANCIAL CONDITIONS. ***")
print("*** DISCLAIMER: THIS IS NOT INVESTMENT ADVICE, AND NO ADVICE SHOULD BE TAKEN FROM THIS CALCULATION. ***")

print('\n')

def create_new_rat():
    name = "RAT"
    str_income = input("ENTER YOUR ANNUAL INCOME (NUMBERS ONLY): ")
    str_rate = input("WHAT PERCENT OF YOUR INCOME DO YOU SAVE? ENTER A NUMBER BETWEEN 0 AND 100: ")
    str_career = input("ENTER THE NUMBER OF YEARS YOU PLAN TO WORK: ")
    str_investment_returns = input("WHAT PERCENT, ON AVERAGE, WILL YOUR INVESTMENTS RETURN? ENTER A NUMBER BETWEEN 0 AND 100: ")


    income = int(str_income)
    rate = int(str_rate)
    career = int(str_career)
    investment_returns = int(str_investment_returns)

    new_rat = rat(name, income, rate, career)



    print('\n')
    print("YOUR DOLLAR-COST-AVERAGED RETURNS, YEAR-BY-YEAR:")
    print('\n')

    dollar_cost_average(new_rat, investment_returns)
    print('\n')

create_new_rat()

print('\n')

restart = input("ENTER 'NEW' TO MAKE A NEW CALCULATION: ")
print('\n')
if(restart == 'NEW' or restart == 'new'):
    create_new_rat()

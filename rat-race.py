import math

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
        annual_savings = self.income * self.rate
        # print(str(annual_savings))
        return(annual_savings)

    def lifetime_savings(self):
        lifetime_savings = self.income * self.rate * self.career
        # print(str(lifetime_savings))
        return(lifetime_savings)

def dollar_cost_average(rat, investment_returns):
    current_balance = rat.annual_savings()

    for x in range (rat.career + 1):
        a = x ## counter for year numbers
        x = round(current_balance, 3)
        rate_of_return = 1 + .01 * investment_returns
        new_balance = x * rate_of_return + rat.annual_savings()
        current_balance = new_balance
        print("YEAR:" + str(a) + " = " + str(x)) ## print responses

frank = rat("Frank", 150000, 0.1, 30) ## hypothetical RAT 1
alice = rat("Alice", 150000, 0.1, 30) ## hypothetical RAT 1

''' CREATE NEW RATS TO TEST DIFFERENT COMBINATIONS OF INCOME,
RATE OF INVESTMENT RETURNS, YEARS WORKED, ETC. '''

print(str(frank.annual_savings))
print(str(frank.lifetime_savings))

dollar_cost_average(frank, 4)
print("BREAK")
dollar_cost_average(alice, 8)

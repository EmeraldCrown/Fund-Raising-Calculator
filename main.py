#define variables
import time
fund_target = 0
cost_unit = 0
proj_sales = 0
profit_mar = 0

def simple_time():
  time.sleep(1)
def no_string(question):
  valid = False
  error_msg = "Please enter a number greater than 0"
  response = input(question)
  while not valid:
    try:
      if float(response) <= 0:
        print(error_msg)
        response = input(question)
      else:
        return response
        valid = True
    except ValueError:
      print(error_msg)
      response = input(question)
#programme begins

print("""Welcome to the Fund Raising Calculator.
We will calculate your profit margins, the amount of units you must sell and a whole heap of other things just with a few simple inputs.
Lets get started.""")
simple_time()
fund_target = no_string("What is your overall fundraising target? ")
print(fund_target)





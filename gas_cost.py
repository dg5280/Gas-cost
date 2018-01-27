
#Write a script that calculates how much money I would save
#by taking the bus

def daily_gas(miles,mpg):
  #print "Calculating gallons of gas each day by dividing %r miles by %r mpg" % (miles,mpg)
  return miles / mpg

def daily_cost(daily_gas,gas_price):
  return daily_gas * gas_price

prompt = '>> '

print "What's the current price of gas?"
gas_price = float(raw_input(prompt))

print "How many miles do you drive round trip every day?"
miles = float(raw_input(prompt))

print "What's the average miles per gallon of the Xterra?"
mpg = float(raw_input(prompt))



#print "Gas prices are %r" % (gas_price)
#print "Average mileage is %r miles to work every day" % (miles)
#print "You are gettn %r miles per gallon" % (mpg)

gallons_day = daily_gas(miles,mpg)
#daily_cost = (gallons_day,gas_price)

print "You'll consume", round(gallons_day,1), "gallons of gas per day."
print "This will cost approximately", round(daily_cost(gallons_day,gas_price),2), "dollars per day."




#Go back and look at ex14.py for input examples.
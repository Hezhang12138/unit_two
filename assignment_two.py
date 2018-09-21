
# He Zhang
# Sept. 21th
# assignment_two
# This is the first chat box I have ever done, I find it is amazing that I made it, and chat with it successfully.






What_is_your_name = input("What is your name?:")

print("You did a great job", What_is_your_name, "and another question.")

where_are_you_come_from = input("Where are you come from?")

print(where_are_you_come_from, "is a beautiful place, isn't it?")

What_is_your_favorite_number = input("What is your favorite number?")

my_favorite_number = 6

times = int(What_is_your_favorite_number) / int(my_favorite_number)

print(What_is_your_favorite_number, "is a great number!", "which is", times, "times larger than my favorite number 6")

What_is_your_dream_car = input("What is your dream car?:")

print("Emmm, I love", What_is_your_dream_car, ", do you know more about it?")

How_much_does_your_dream_car_cost = float(input("How much does your dream car cost?:"))

print("Wow,", How_much_does_your_dream_car_cost, "is a lot.")

How_many_years_the_user_would_take_a_loan_out_to_pay = float(input("how many years would you take a loan out to pay"))

print(How_many_years_the_user_would_take_a_loan_out_to_pay, "is a long time!")

What_annual_interest_rate_you_expect_to_get = float(input("what annual interest rate are you expect to get?"))

print(What_annual_interest_rate_you_expect_to_get, "Emmm, I believe you can do it!")

r = What_annual_interest_rate_you_expect_to_get / 100 / 12

monthly_payment = (r * How_much_does_your_dream_car_cost) / (1 - ( 1 + r) ** (-How_many_years_the_user_would_take_a_loan_out_to_pay * 12))

print("Your monthly payment for the", What_is_your_dream_car, "is", monthly_payment)

print("I think we have a great talk! Bye")
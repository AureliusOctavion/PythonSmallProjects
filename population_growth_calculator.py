# Write the necessary code to display the total population count for the next 3 years (without a leap year).


# Conversions to keep in mind:

# Current population = 380123456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

# 60 seconds = 1 minute
# 60 minutes = 1 hour
# 24 hours = 1 day
# 365 days = 1 year

# Given:
current_population = 380123456
birth_rate = 6 # seconds
death_rate = 12 # seconds
immigration_rate = 40 # seconds


seconds_per_year = 60 * 60 * 24 * 365

# By dividing the number of seconds in a year, by the rate at which a person is born we get the number of births in a year
births_per_year = seconds_per_year // birth_rate # 31,536,000 // 6 = 5,256,000 births per year

# By dividing the number of seconds in a year, by the rate at which a person dies we get the number of deaths in a year
deaths_per_year = seconds_per_year // death_rate # 31,536,000 // 12 = 2,628,000 deaths per year

# By dividing the number of seconds in a year, by the rate at which a person immigrates we get the number of immigrations in a year
immigrations_per_year = seconds_per_year // immigration_rate # 31,536,000 // 40 = 788,400 immigrations per year

# Net population change per year
# the total amount by which the population grows (or shrinks) in a single year after accounting for all the relevant factors: births, deaths, and immigration.

net_population_change_per_year = births_per_year - deaths_per_year + immigrations_per_year 

# Calculate population for the next 3 years
year_1_population = current_population + net_population_change_per_year
year_2_population = year_1_population + net_population_change_per_year
year_3_population = year_2_population + net_population_change_per_year

# Print results
print(year_1_population)
print(year_2_population)
print(year_3_population)



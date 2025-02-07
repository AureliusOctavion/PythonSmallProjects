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


# Conversions for born every minute till year

# 10 people are born every minute
one_person_born_every = 6 # seconds
conversion_for_born_every_minute = 60 / one_person_born_every # 10

# 600 people are born every hour
conversion_for_born_every_minute_hour = conversion_for_born_every_minute * 60 # 600

# 14400 people are born every day
conversion_for_born_every_minute_day = conversion_for_born_every_minute_hour * 24 # 14400

# 5256000 people are born every year
conversion_for_born_every_minute_year = conversion_for_born_every_minute_day * 365 # 5256000





# Conversions for die every minute till year

# 5 people die every minute
one_person_die_every = 12 # seconds
conversion_for_die_every_minute = 60 / one_person_die_every # 5

# 300 people die every hour
conversion_for_die_every_minute_hour = conversion_for_die_every_minute * 60 # 300

# 7200 people die every day
conversion_for_die_every_minute_day = conversion_for_die_every_minute_hour * 24 # 7200

# 2628000 people die every year
conversion_for_die_every_minute_year = conversion_for_die_every_minute_day * 365 # 2628000


# Conversions for immigrate every minute till year

# 3 people immigrate every two minutes
one_person_immigrate_every = 40 # seconds
conversion_for_immigrate_every_minute = one_person_immigrate_every / 60 * 2 # 3

# 90 people immigrate every hour
conversion_for_immigrate_every_minute_hour = conversion_for_immigrate_every_minute * 30 # 90

# 2160 people immigrate every day
conversion_for_immigrate_every_minute_day = conversion_for_immigrate_every_minute_hour * 24 # 2160

# 788400 people immigrate every year

conversion_for_immigrate_every_minute_year = conversion_for_immigrate_every_minute_day * 365 # 788400




# Current population

given_current_population = 380123456


new_current_population = given_current_population + conversion_for_born_every_minute_year - conversion_for_die_every_minute_year + conversion_for_immigrate_every_minute_year

print(new_current_population)


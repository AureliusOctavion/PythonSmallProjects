# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles = 10
time_minutes = 30
time_seconds = 30
mile_to_km = 1.6


kilometers = miles * mile_to_km

total_time_hours = time_minutes / 60 + time_seconds / 3600

average_speed_kmh = kilometers / total_time_hours

print(average_speed_kmh)
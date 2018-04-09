cars = 100
#using cars as variable to assign value of 100
space_in_a_car = 4.0
##using space_in_car as variable to assign value of 30
drivers = 30
#using drivers as variable to assign value of 30
passengers = 90
#using passengers as variable to assign value of 90
cars_not_driven = cars - drivers
#using cars_not_driven as variable to assign value by doing maths 100-30=90
cars_driven = drivers
#using cars_driven as variable to assign value of drivers i.e 30
carpool_capacity = cars_driven * space_in_a_car
#using carpool_capacity as variable to assign value doing maths 30*4.0=120.0
average_passengers_per_car = passengers / cars_driven
#using average_passengers_per_car as variable to assign value doing math equation 90/30=3

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today"
print "we have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car."

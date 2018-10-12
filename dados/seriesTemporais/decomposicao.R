dec = decompose(AirPassengers)

dec$seasonal
dec$trend
dec$random

plot(dec$seasonal)
plot(dec$trend)
plot(dec$random)

plot(dec)

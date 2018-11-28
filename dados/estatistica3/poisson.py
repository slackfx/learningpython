from scipy.stats import poisson

# média de 2 acidentes
# qual a probabilidade de ocorrer 3 ?

poisson.pmf(3, 2)

# e a probabilidade de serem 3 ou menos acidentes ?

poisson.cdf(3, 2)

# e mais de 3 acidentes ?

poisson.sf(3, 2)

# Em média ocorrem 10 mortes por mês em um hospital.

# Qual a probabilidade de, em um determinado mês, ocorrerem 12 mortes?
poisson.pmf(12, 10)
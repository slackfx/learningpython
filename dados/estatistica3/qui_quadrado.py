import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19, 6], [43, 32]])

chi2_contingency(novela)

jogoAzar = np.array([[41, 34], [18, 7]])

chi2_contingency(jogoAzar)

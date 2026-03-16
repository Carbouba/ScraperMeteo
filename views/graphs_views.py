import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../data")
from queries import get_temp_date

data = get_temp_date()
temp = data[0]
date = data[1]

plt.plot(date, temp)
plt.title("Prévisions météo")
plt.xlabel("Date")
plt.ylabel("Température")
plt.show()

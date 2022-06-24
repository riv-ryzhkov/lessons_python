import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# График
df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
df = df.cumsum() # Return cumulative sum over a DataFrame or Series axis
df.plot()
plt.show()

# Диаграмма (bar)
df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
df.plot.bar(stacked=True)
plt.show()

# Диаграмма (box)
df = pd.DataFrame(np.random.rand(7, 5), columns=list('ABCDE'))
df.plot.box()
plt.show()

# Гистограмма
data = pd.Series(np.random.normal(size=100))
data.hist(grid=False)
plt.show()
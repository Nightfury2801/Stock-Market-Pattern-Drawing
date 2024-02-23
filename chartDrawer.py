import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/BPCL.csv')
temp_df =  df[:50]

plt.plot(temp_df['Date'], temp_df['Close'])
plt.rc('xtick', labelsize=2)
plt.xlabel('Date', size=2)
plt.ylabel('Closing Price')
plt.title('Stock Price closing')
plt.show()

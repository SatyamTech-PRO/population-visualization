import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#step 1 read the csv data
data = pd.read_csv("data.csv")

#step 2 show the data (optional, just to confirm it's loading)
print(data)

#step 3 Bar chart for Gender distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=data)
plt.title("Gender distribution")
plt.xlabel("Gender")
plt.ylabel("number of people ")
plt.tight_layout()
plt.show()

#step 4  histogram for age distribution
plt.figure(figsze=(8,5))
sns.histplot(data["age"], bins=6 , kde=True , color = "skyblue")
plt.title("age distribution")
plt.xlabel("age group ")
plt.ylabel("number of people ")
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
population_data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_87.csv", skiprows=4) 
metadata_country = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_87.csv")  
metadata_indicator = pd.read_csv("Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_87.csv") 
population_data = population_data[['Country Name', 'Country Code', '2022']]  
population_data = population_data.dropna()  
merged_data = pd.merge(population_data, metadata_country, on="Country Code", how="left")
top_10_countries = merged_data.sort_values(by="2022", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x="2022", y="Country Name", data=top_10_countries, hue="Country Name", palette="coolwarm", legend=False)
plt.xlabel("Population (in billions)")
plt.ylabel("Country")
plt.title("Top 10 Most Populated Countries in 2022")
plt.show()
plt.figure(figsize=(10, 5))
sns.histplot(merged_data["2022"], bins=20, kde=True, color="blue")
plt.xlabel("Population (in billions)")
plt.ylabel("Frequency")
plt.title("Population Distribution of Countries in 2022")
plt.show()

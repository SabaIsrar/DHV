import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set the font weight to bold
rcParams['axes.labelweight'] = 'bold'

# Load the dataset
df = pd.read_csv('crimes_against_women_2001-2014.csv')
df = df.drop(['Unnamed: 0', 'Importation of Girls'], axis=1)

# Plot 1: Total Women Harassment Crimes Over the Years
agg_df = df.melt(id_vars=['STATE/UT', 'DISTRICT', 'Year'], var_name='Crime_Type', value_name='Count')
agg_df = agg_df.groupby(['Year'], as_index=False)['Count'].sum()

plt.figure(figsize=(15, 8))
ax = sns.barplot(x='Year', y='Count', data=agg_df, color='blue')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Number of Cases', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontweight='bold')
plt.title('Total Women Harassment Crimes Over the Years', fontweight='bold')
plt.savefig("22092394_1.png", dpi=300)

# Plot 2: Women Harassment Crimes Over the Years by Crime Type
melted_df = df.melt(id_vars=['STATE/UT', 'DISTRICT', 'Year'], var_name='Crime_Type', value_name='Count')
agg_df = melted_df.groupby(['Year', 'Crime_Type'], as_index=False)['Count'].sum()

plt.figure(figsize=(15, 8))
sns.lineplot(x='Year', y='Count', hue='Crime_Type', data=agg_df, errorbar=None)
plt.legend(title='Crime Type', loc='upper left', frameon=False)
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Number of Cases', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.savefig("22092394_2.png", dpi=300)

# Plot 3: Total Women Harassment Crimes in 2014 (Pie Chart)
df_2014 = df[df['Year'] == 2014]
total_crimes_2014 = df_2014.sum(axis=0)  # Exclude non-numeric columns

plt.figure(figsize=(18, 18))
# Assuming total_crimes_2014 is a pandas Series
plt.pie(total_crimes_2014[3:], labels=total_crimes_2014.index[3:], startangle=100,autopct='%1.1f%%',textprops={ 'fontweight': 'bold', 'fontsize': 14})

plt.tight_layout()
plt.savefig("22092394_3.png", dpi=300)

# Plot 4: Top 5 States with Highest Women Harassment Crimes in 2014 (Pie Chart)
# Filter the DataFrame for the year 2014
df_2014 = df[df['Year'] == 2014]

df_2014_numeric = df_2014.apply(pd.to_numeric, errors='ignore')

# Sum the total crimes for each state
total_crimes_by_state = df_2014.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1)


# # Sum the total crimes for each state
# total_crimes_by_state = df_2014.groupby('STATE/UT').sum().sum(axis=1)

# Select the top five states with the highest crimes
top5_states = total_crimes_by_state.nlargest(5)

plt.figure(figsize=(10, 10))
plt.pie(top5_states, labels=top5_states.index, autopct='%1.1f%%', startangle=140)
plt.savefig("22092394_4.png", dpi=300)
# plt.title('Top 5 States with Highest Women Harassment Crimes in 2014')
# plt.show()

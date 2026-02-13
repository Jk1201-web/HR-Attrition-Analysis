import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"c:\Users\hp\Downloads\archive (2)\HR_Attrition.csv")

# print(df.head())

# print(df.shape)

# print(df.isnull().sum())

# print(df.info())

# print(df.describe())

# Attrition count :

# print(df['Attrition'].value_counts())

# sns.countplot(x='Attrition', data=df)
# plt.title("Attrition Count")
# plt.savefig('Attrition_plot_png')
# plt.show()

# Age Vs Attrition :

# plt.figure(figsize = (8,5))
# sns.boxplot(x = 'Attrition', y = 'Age', data = df)
# plt.title('Age vs Attrition')
# plt.savefig('Age_vs_Attrition_plot_png')
# plt.show()

# Salary Vs Attrition :

# plt.figure(figsize = (8,5))
# sns.boxplot(x = 'Attrition', y = 'MonthlyIncome', data = df)
# plt.title('Monthly Income vs Attrition')
# plt.savefig('MonthlyIncome_vs_Attrition_plot_png')
# plt.show()

# Over time Vs Attrition :

# sns.countplot(x='OverTime', hue='Attrition', data=df)
# plt.title("OverTime vs Attrition")
# plt.savefig('OverTime_vs_Attrition')
# plt.show()

# Job Role Vs Attrition :

# plt.figure(figsize=(12,6))
# sns.countplot(y='JobRole', hue='Attrition', data=df)
# plt.title("Job Role vs Attrition")
# plt.savefig('JobRole_vs_Attrition_plot_png')
# plt.show()

# Correlation Heatmap :

# plt.figure(figsize=(12,8))
# sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
# plt.title("Correlation Heatmap")
# plt.savefig('Correlation_Heatmap_png')
# plt.show()

# 
# attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
# print(attrition_rate)

plt.figure(figsize=(6,4))

ax = sns.countplot(x='Attrition', data=df)

total = len(df)
for p in ax.patches:
    percentage = f'{100 * p.get_height()/total:.1f}%'
    ax.annotate(percentage,
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom')

plt.title("Attrition Percentage")
plt.savefig("attrition_percentage.png", dpi=300, bbox_inches='tight')
plt.show()

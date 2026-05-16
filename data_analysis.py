

import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

df=pd.read_csv('Employee.csv')

#--------------
#DATA FILTERING
#-------------
#Male workers
male=df[df['Gender']=='Male']

#female workers
female=df[df['Gender']=='Female']
#Example code of data filtering
example1=df[(df['Gender']=='Male')&
       (df['City']=='Bangalore')&
       (df['JoiningYear']<=2016)
]


#Education
bachelors_degree=df[df['Education']=='Bachelors']

Masters_degree=df[df['Education']=='Masters']

PHD_degree= df[df['Education'] == 'PHD']

#Payment tier
payment_1=df[df['PaymentTier']==1]
payment_2=df[df['PaymentTier']==2]
payment_3=df[df['PaymentTier']==3]

#Salary by groupby
avg_salary_by_gender=df.groupby('Gender')['PaymentTier'].mean()
payment_by_city=df.groupby('City')['PaymentTier'].mean()
payment_by_education=df.groupby('Education')['PaymentTier'].mean()


print('Average salary by gender',avg_salary_by_gender)
print('Average payment by city',payment_by_city)
print('Average payment by education',payment_by_education)

#-------------
#Visualisation
#-------------
#Plot by gender
counts_by_gender = df['Gender'].value_counts()

#Plot by education
counts_by_education=df['Education'].value_counts()

#Plot by city
counts_by_city=df['City'].value_counts()

#SUBPLOT
#Plot by gender
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].bar(counts_by_gender.index, counts_by_gender.values, color='green')
axes[0].set_title('Number of employees by gender')

#Plot by education
axes[1].bar(counts_by_education.index,counts_by_education.values, color='red')
axes[1].set_title('Education distribution')

#Plot by city
axes[2].bar(counts_by_city.index,counts_by_city.values,color='darkblue')
axes[2].set_title('City distribution')


old = df[(df['JoiningYear'] <= 2016) & (df['PaymentTier'] == 3)]
new = df[(df['JoiningYear'] > 2016) & (df['PaymentTier'] == 3)]

print("Old high-tier employees:", len(old))
print("New high-tier employees:", len(new))

plt.tight_layout()
plt.show()
#Advanced visualization
pivot = df.pivot_table(values='PaymentTier', index='Education', columns='Gender')

plt.figure(figsize=(6,4))
sns.heatmap(pivot, annot=True, cmap="YlGnBu")
plt.title("Payment Tier: Education vs Gender")
plt.show()

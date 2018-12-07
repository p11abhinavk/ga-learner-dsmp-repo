# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = senior_citizens.shape[0]
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
import numpy as np
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = age.mean()
age_std = np.std(age)
print(max_age,min_age,age_mean,age_std)


# --------------
#Code starts here

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = race_0.shape[0]
len_1 = race_1.shape[0]
len_2 = race_2.shape[0]
len_3 = race_3.shape[0]
len_4 = race_4.shape[0]

print(race_0)
print('Race 0 ',len_0)
print('Race 1 ',len_1)
print('Race 2 ',len_2)
print('Race 3 ',len_3)
print('Race 4 ',len_4)

minority_n = min(len_0,len_1,len_2,len_3,len_4)
if minority_n == len_0:
    minority_race = 0
elif minority_n == len_1:
    minority_race = 1
elif minority_n == len_2:
    minority_race = 2
elif minority_n == len_3:
    minority_race = 3
else:
    minority_race = 4
print(minority_race)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
if avg_pay_high>avg_pay_low:
    print("Good scores fetch higher salary")
else:
    print("Good scores do not get you higher salary")



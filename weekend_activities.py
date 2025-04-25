import matplotlib.pyplot as plt

# dictionary containing activities and time spent
activity_time = {'Sleeping': 9, 'Homework': 2, 'Playing Games': 3, 'Reading': 1, 'Eating': 2, 
              'With Friends': 4, 'Other': 3}

# extract activites and time spent
activities = activity_time.keys()
time_spent = activity_time.values()

# pastel color options for pie chart
pastel_colors = ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF", "#A0C4FF", "#BDB2FF"]

# create the pie chart
plt.figure(figsize=(8,8))
plt.pie(time_spent, labels=activities, autopct='%1.1f%%', startangle=90, colors=pastel_colors)

# add the title
plt.title('How I Spent My Saturday')

# show the plot
plt.show()

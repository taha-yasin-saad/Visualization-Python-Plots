import matplotlib.pyplot as plt

# Sample data for job applications (replace with your data)
job_applications = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

plt.figure(figsize=(8, 6))
plt.hist(job_applications, bins=10, edgecolor='black', alpha=0.7)

plt.title('Distribution of Job Applications')
plt.xlabel('Number of Applications')
plt.ylabel('Frequency')
plt.show()
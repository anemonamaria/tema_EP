import matplotlib.pyplot as plt

# How many requests can be handled by a single machine?
#  201 ---> emea
# 307 ---> asia
#   298 --> us

import matplotlib.pyplot as plt
%matplotlib inline

x = ['ASIA', 'EMEA', 'US']
y = [201, 307, 298]
# plt.plot(x, y)


ax = plt.subplot()
ax.bar(x, y)

plt.xlabel('Server regions')
plt.ylabel("Number of requests handled by a single machine")
plt.gcf().set_size_inches(15, 5)


x = [50, 100, 200, 300]
rr = [48.11, 92.24, 202.77, 306.51]
rm = [43.23, 113.63, 197.63, 323.67]
wrr = [45.35, 92.23, 192.00, 277.24]

plt.plot(rr, x, label = "Round Robin")
plt.plot(rm, x, label = "Random Machine")
plt.plot(wrr, x, label = "Weighted Round Robin")


plt.ylabel('Number of requests')
plt.xlabel("Number of seconds")
plt.legend()
plt.show()
plt.gcf().set_size_inches(15, 5)
import pandas as pd
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def csv_to_df(file_name):
    game_df = pd.read_csv(file_name)
    return game_df

print(csv_to_df('Rushhour6x6_1.csv'))

df = csv_to_df('Rushhour6x6_1.csv')
df[]

fig = plt.figure(figsize=[6,6])
fig.patch.set_facecolor((1,1,0.5))
ax = fig.add_subplot(111)

for x in range(7):
    ax.plot([x, x], [0, 6], 'k')

for y in range(7):
    ax.plot([0, 6], [y, y], 'k')

ax.set_position([0,0,1,1])

ax.set_xlim(-1,7)
ax.set_ylim(-1,7)

# ax.add_patch((1, 1))
# plt.patches.Rectangle((1, 1), 1, 1, angle=0.0)

ax.add_patch(plt.Rectangle((1, 1), 1, 2))


plt.show()

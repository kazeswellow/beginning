import matplotlib.pyplot as plt
import seaborn as sns
from random import choice

"""
roll a pair of dice many times and show the distribution
"""

SPOTS = 1, 2, 3, 4, 5, 6
ROLLS = 500000


def main():
    """
    | accumulate each roll of the dice
    | accumulate the sum of each roll
    :return: none
    """

    list_die_1 = []
    list_die_2 = []
    sums = []

    for _ in range(ROLLS):
        # roll the dice
        die_1 = choice(SPOTS)
        die_2 = choice(SPOTS)

        # store the results
        list_die_1.append(die_1)
        list_die_2.append(die_2)
        sums.append(die_1 + die_2)

    # plot the sum of the rolls
    sns.countplot(x=sums).set(title=f"sum of pair of dice rolled {ROLLS:,d} times")

    # plot the number of times each spot appeared
    _, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
    sns.countplot(x=list_die_1, ax=ax1).set(title=f"die 1 rolled {ROLLS:,d} times")
    sns.countplot(x=list_die_2, ax=ax2).set(title=f"die 2 rolled {ROLLS:,d} times")

    plt.show()


if __name__ == '__main__':
    main()

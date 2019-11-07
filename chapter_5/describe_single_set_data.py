import random
from collections import Counter
from matplotlib import pyplot as plt


def plot_friends_vs_people(num_of_friends, num_of_people):
    friends_count = Counter(num_of_friends)
    xs = num_of_people
    ys = [friends_count[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of friends count")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.draw()


def mean(v): return sum(v) / len(v)


def median(v):
    u = sorted(v)
    return mean([u[len(u) // 2], u[len(u) // 2 + 1]]) if 0 == len(u) % 2 else u[len(u) // 2]


def quantile(v, p): return sorted(v)[int(p * len(v))]


def mode(v):
    sorted_counts = Counter(v).most_common()
    max_value = sorted_counts[0][1]
    return [item[0] for item in sorted_counts if item[1] == max_value]


def data_range(v): return max(v) - min(v)


def main():
    random.seed(42)
    num_of_friends = [random.randint(1, 204) for _ in range(100)]
    # num_of_people = range(101)
    # plot_friends_vs_people(num_of_friends, num_of_people)

    mean_num_of_friends = mean(num_of_friends)
    print(mean_num_of_friends)

    median_num_of_friends = median(num_of_friends)
    print(median_num_of_friends)

    print(quantile(num_of_friends, 0.1))
    print(quantile(num_of_friends, 0.25))
    print(quantile(num_of_friends, 0.99))

    mode_num_of_friends = mode(num_of_friends)
    print(mode_num_of_friends)

    data_range_num_of_friends = data_range(num_of_friends)
    print(data_range_num_of_friends)

    # plt.show()


if __name__ == '__main__':
    main()

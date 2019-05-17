#!/bin/python3

import sys
from collections import defaultdict


def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    # p: population of towns
    # x: location of towns
    # y: location of clouds
    # r: range of clouds

    target_town = None
    town_max_clouds = 0
    target_cloud = None
    target_max_popu = 0
    # prepare town hash table
    # town = defaultdict(list)
    town = defaultdict(int)
    for i in range(len(p)):
        # print("town location %d, population %d" % (x[i], p[i]))
        # if not town[x[i]]:
        #     town[x[i]] = [p[i], []]     # [population, covered clouds]
        # else:
        #     town[x[i]][0] += p[i]
        town[x[i]] += p[i]
    # print("town:", town)
    cloud = defaultdict(list)
    for j in range(len(y)):
        cloud_location = y[j]
        cover_location = range(cloud_location - r[j], cloud_location + 1 + r[j])
        for t in town:
            if t in cover_location:
                if not cloud[cloud_location]:
                    cloud[cloud_location] = [town[t], [t]]  # [population, town location]
                else:
                    cloud[cloud_location][0] += town[t]
                    cloud[cloud_location][1].append(t)
                if cloud[cloud_location][0] > target_max_popu:
                    target_max_popu = cloud[cloud_location][0]
                    target_cloud = cloud_location

        # for c in cover_location:
        #     if c in town:
        #         town[c][1] += 1
        #         if not target_town:
        #             target_town = (c, town[c][0], town[c][1])
        #         else:
        #             if town[c][0] > target_town[1]: # compare population
        #                 target_town = (c, town[c][0], town[c][1])


    # print("b4 cloud:", cloud)
    # remove 1 cloud from largest population
    # town[target_town[0]][1] -= 1
    del cloud[target_cloud]
    # print("af cloud:", cloud)
    # max_ppl = sum([town[k][0] for k in town
    #                           if town[k][1] <= 0])
    if cloud:
        max_ppl = sum(town[t] for t in town
                              for c in cloud
                              if t not in cloud[c][1])
    else:
        max_ppl = sum(town[t] for t in town)
    return max_ppl


if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r)
    print(result)


# In:
# 5
# 9 9 1 5 8
# 1 7 7 11 7
# 2
# 2 3
# 4 11

# Out:
# 23

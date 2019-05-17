#!/usr/bin/env python

class Yelp(object):
    def __init__(self, restaurants, ratings):
        self.restaurants = restaurants
        self.ratings = ratings

    def find(self, coordinates, radius, dining_hour=None, sort_by_rating=False):
        #  coordinates: (latitude, longitude)
        #  radius: kilometer in integer
        #  dining_hour: If None, find any restaurant in radius.
        #               Otherwise return list of open restaurants at specified hour.
        #  sort_by_rating: If True, sort result in descending order,
        #                  highest rated first.

        result = []
        # Returns list of Restaurant within radius.
        if coordinates is not None and len(coordinates) == 2:
            min_latitude, max_latitude = coordinates[0], coordinates[0] + radius
            min_longitude, max_longitude = coordinates[1], coordinates[1] + radius
            result =  [r for r in self.restaurants
                       if min_latitude <= r.latitude < max_latitude and
                          min_longitude <= r.longitude < max_longitude]

        if isinstance(dining_hour, int):
            result = [r for r in result
                      if r.open_hour <= dining_hour < r.close_hour]

        if sort_by_rating:
            rating_result = [ra for ra in self.ratings
                                for r in result
                                if ra.restaurant_id == r.id]
            # heap_q = HeapSort(result)
            # heap_q.heap_sort()
            sorted_ratings = sorted(rating_result, key=lambda x: x.rating, reverse=True)
            result = [r for ra in sorted_ratings
                        for r in result
                        if ra.restaurant_id == r.id]

        return result


# class HeapSort:
#     def __init__(self, array_list):
#         self.array_list = array_list
#
#     def swap(self, i, j):
#         self.array_list[i], self.array_list[j] = self.array_list[j], self.array_list[i]
#
#     def max_heapify(self, end, i):
#         l = 2 * i + 1
#         r = 2 * i + 2
#         max_i = i
#         if l < end and self.array_list[max_i] < self.array_list[l]:  # left node > root
#             max_i = l
#         if r < end and self.array_list[max_i] < self.array_list[r]:  # right node > root
#             max_i = r
#         if max_i != i:
#             swap(i, max_i)
#             max_heapify(end, max_i)
#
#     def heap_sort(self):
#         end = len(self.array_list)
#         # build heap
#         start = end // 2 - 1  # get mid point, //: divide to get int only
#         for i in range(start, -1, -1):
#             max_heapify(end, i)
#
#         for i in range(end - 1, 0, -1):
#             swap(i, 0)        # swap root & end node
#             max_heapify(i, 0)


class Restaurant(object):
    # where open_hour and close_hour is in [0-23]
    def __init__(self, id, name, latitude, longitude, open_hour, close_hour):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.open_hour = open_hour
        self.close_hour = close_hour

    def __repr__(self):
        return self.name

class Rating(object):
    # rating is in [1-5]
    def __init__(self, restaurant_id, rating):
        self.restaurant_id = restaurant_id
        self.rating = rating

def main(argv):
    restaurants = [Restaurant(0, "Domino's Pizza", 37.7577, -122.4376, 7, 23),
                   Restaurant(1, "Pizza Hut", 24.3425, 0.2341, 9, 18),
                   Restaurant(2, "Napoleon", -56.4897, -23.038, 11, 21),
                   Restaurant(3, "McDonald's", 54.2345, 234.1012, 0, 23),
                   Restaurant(4, "KFC", 1.234, 87.103, 11, 19)]
    ratings = [Rating(0, 3),
               Rating(1, 4),
               Rating(2, 5),
               Rating(3, 2),
               Rating(4, 4)]

    y = Yelp(restaurants, ratings)
    y.find((37.7, -122.6), 5, None, False)

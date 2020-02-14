# Author: Mackenna Semeyn
# Course: Computational Biology Spring 2020
# Due date: 2/14/2020
# File: partial_digest.py
# This file defines the functions necessary to execute the solution to the partial digest problem.

import sys


def partial_digest(multiset):
    # set width of fragment being examined
    width = max(multiset)
    # remove largest element from the multiset
    multiset.remove(max(multiset))
    # add zero and largest element to result set
    resultset = [0, width]
    # call place function to implement recursive solution
    place(multiset, resultset)


def place(multiset, resultset):
    # if multiset is empty, print result set, size, and return
    if not multiset:
        print(sorted(resultset))
        print("Size: ", len(resultset))
        sys.exit()
    # set y equal to the maximum element in the multiset
    y = max(multiset)
    # print("y = ", y)
    # remove y from the multiset
    # multiset.remove(y)
    # find distances from current y to values in resultset
    dx = distance(y, resultset)
    # print("dx = ", dx)
    # print("multiset = ", multiset)
    # check if dx is contained inside multiset
    if set(dx).issubset(set(multiset)):
        # add y to result set
        resultset.append(y)
        # print("resultset = ", resultset)
        # remove lengths in dx from multiset
        for elem in dx:
            # print("removing ", elem)
            multiset.remove(elem)
        # call place function on updated sets
        place(multiset, resultset)
        # print("multiset = ", multiset)
        # print("resultset = ", resultset)
        # remove y from result set
        resultset.remove(y)
        # print("removing ", y, " from resultset")
        # add lengths in dx to multiset
        for elem in dx:
            multiset.append(elem)
            # print("appending ", elem)
    # find distances from width - y
    ndx = distance(max(resultset) - y, resultset)
    # print("ndx = ", ndx)
    # check if ndx is contained inside the multiset
    if set(ndx).issubset(set(multiset)):
        # add width - y to resultset
        resultset.append(max(resultset) - y)
        # remove lengths in ndx from multiset
        for elem in ndx:
            # print("removing ", elem)
            multiset.remove(elem)
        # call place function on updated sets
        place(multiset, resultset)
        # print("multiset = ", multiset)
        # print("resultset = ", resultset)
        # remove width - y from the result set
        resultset.remove(max(resultset) - y)
        # add lengths in ndx to multiset
        for elem in ndx:
            multiset.append(elem)
            # print("appending ", elem)


def distance(y, resultset):
    dx = []
    for element in resultset:
        dx.append(abs(y - element))
        # print(y, " - ", element, " = ", abs(y - element))
    return dx

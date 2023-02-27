# Tugas Kecil 2 Closest Pair Problem

## Table of Contents

- [Tugas Kecil 2 Closest Pair Problem](#tugas-kecil-2-closest-pair-problem)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Problem Description](#problem-description)
  - [Program Features](#program-features)
  - [Algorithm Description](#algorithm-description)
  - [Program Structure](#program-structure)
  - [Running The Program](#running-the-program)
  - [Libraries Used](#libraries-used)

## Project Description

A Closest pair of points problem solver using the Divide and Conquer Algorithm, made by Kenneth Ezekiel (13521089) and Alisha Listya (13521171) for the Algorithm & Design Course

## Problem Description

The closest pair of points problem is, as the name suggests, a problem when: given n number of points, find the closest pair of points by the euclidean distance for the set of points.

This Project aims to take the original problem and solve it on a higher dimension (the original problem was based on 2 Dimensional set of points), with the Divide and Conquer Approach, also comparing it with the Brute Force Approach.

## Program Features

The features of our program:
* Getting the closest pair of points in n-dimensional space
* Divide and Conquer Algorithm + Execution Time + Number of distance calculation operations
* Read and Write to file (I/O)
* Points Visualizer + Write to PNG
* Closest pair of points visualizer

## Algorithm Description

The divide and conquer algorithm for finding the closest pair of points in 2 Dimensional is already known widely, dividing the points into 2 sub-array recusively, and then combining their results, with the consideration of points near the middle point of division (+- delta or the closest distance got from the recursion).

Implementing it into 3 Dimensional space and then n-Dimensional space is a more interesting story as now we also need to consider not a strip from the middle point, but a slab (in 3 Dimensional) and a more complex structure in n-Dimensional space. But our approach to this problem uses the [sparsity condition](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjSu6_C6bP9AhVt53MBHUUxDi8QFnoECBUQAw&url=https%3A%2F%2Fwww.cs.ubc.ca%2F~liorma%2Fcpsc320%2Ffiles%2Fclosest-points.pdf&usg=AOvVaw1AZ6S6JbrWX_9jXq7R0ZfX) and limits the Time Complexity for O(n^2) into O(n*log n).

## Program Structure

```

```

## Running The Program

To run the program, simply use the command `run.bat` on Windows or directly run the `main.py` python script in the `src` folder

## Libraries Used

* Numpy
* Matplotlib
* Os
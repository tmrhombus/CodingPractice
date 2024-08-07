
# Coding Practice

This a repository for practicing various algorithm implementations, with a focus on machine learning  

## Neural Network - Handwritten Number Recognition

Also known as Multiclass Logistic Regression optimized via Gradient Descent \
Implemented in Python from scratch without using any ML libraries \
Three layers: 400/25/10 nodes with sigmoid activations, 94% accuracy

<img src="./MachineLearning/05_NeuralNetwork/output/result.gif" width="800"  />  

 ## Support Vector Machine
 Optimal Margin Classifier + Kernel Trick = Support Vector Machine \
 Also known as L1 Norm Soft Margin Support Vector Machine \
 Shown are scans of decision boundaries for different choices of regularization (C) and scale (λ)  

  <img src="./MachineLearning/04_SupportVectorMachine/output/animation2.gif" width="300"  />   <img src="./MachineLearning/04_SupportVectorMachine/output/animation_ex2.gif" width="300"  /> 


 ## Logistic Regression
   
  2D feature vectors mapped to 6th order polynomials \
  Shown with different values of regularization parameter λ (over/under fit)
  
  <img src="./MachineLearning/03_LogisticRegression/output/animation_microchips.gif" width="300"  />   <img src="./MachineLearning/03_LogisticRegression/output/microchips_J_convergence.png" width="300"  /> 
  
  Linear decision boundary - no feature mapping
 
  <img src="./MachineLearning/03_LogisticRegression/output/animation_testscores.gif" width="300"  /> 

## Clustering Algorithms (unsupervised learning)

### K-Means (implemented in C++)

 <img src="./kmeans/plots/animation.gif" width="300"  />

### Mean Shift (implemented in C++)
  
 <img src="./meanshift/plots2/animation.gif" width="300"  />  <img src="./meanshift/plots/animation.gif" width="300"  />


 ## Gradient Descent
  Python implementations of Batch Gradient Descent along with cost function 
  
  <img src="./MachineLearning/01_GradientDescent/outfiles/Jplot.png" width="300"  /> 
  
  <img src="./MachineLearning/01_GradientDescent/outfiles/animation.gif" width="300"  />  <img src="./MachineLearning/02_GradientDescentMatrixMethod/outfiles/animation.gif" width="300"  />
  
  <img src="./MachineLearning/01p5_GradientDescent/output/result.gif" width="600"  />  
  

## maze solver
 Python implementation to find the minimum number of steps to complete a maze \
 Part of the Google FooBar challange
 
 <img src="./mazesolver/outfiles/maze1/animation.gif" width="300">   <img src="./mazesolver/outfiles/maze2/animation.gif" width="300">

# Other projects and algorithm implementations

## datagenerator
 code to generate fake datasets
 - normal distributions
 - gaussian jitter along a line


## bitwise operations
 c++ examples of functions executing bitwise operations 
 - logical operators
 - right/left shift div/mult by 2
 - & 1 for odd/even
 - XOR find singly-occurring element in array

## recursion
 c++ examples of recursive fucntions 
 - write number in binary
 - calculate compound interest minus a commission
   after some set time
 - count up and down from min to max
 - calculate factorial
 - find the maximum number in an array
 - sort an array from min to max (selection sort)
 - find the sum of all numbers between a and b

## sorting
 python examples of sorting algorithms
 - quicksort
 - bubblesort
 - mergesort

 ## hash sets
  python implementation of a hash set, then using the hash set to solve a few problems
  - check if an array contains any duplicate numbers
  - find the intersection of two arrays
  - determine if an integer is "happy" (number theory definition) 
    https://en.wikipedia.org/wiki/Happy_number

## trees
- binary tree, breadth first search, depth first search (pre/post/in order)  
- binary search tree

 ## Project Euler
 Solutions to questions from https://projecteuler.net/
 1. Sum of multiples of 3 or 5 < 1k :: 233168
 2. Sum of even Fibinocci numbers < 4M :: 4613732
 3. Largest prime factor of 600851475143 :: 6857
 4. Largest palindrome made from the product of two 3-digit numbers: 913 x 993 = 906609
 5. Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 :: 232792560
  - It has a prime factorization of [1, 2, 3, 2, 5, 7, 2, 3, 11, 13, 2, 17, 19]
 6. Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum :: 25164150
 7. The 10001st prime number :: 104743
 8. Given a 1000-digit number, find the group of 14 sequential numbers with largest product :: 23514624000
 9. There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc. :: 200 x 375 x 425 = 31875000
 10. Sum of all primes less than 2M :: 142913828922


## leetcode
Find all unique combinations of 4 numbers in an array which add to a given target

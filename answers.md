# CMPS 2200 Assignment 3
## Answers

**Name:**_____Cole Welch__________


Place all written answers from `assignment-03.md` here for easier grading.

1a)
A greedy algorithm for producing as few coins as possible that sum to N is to 
select the highest 2^k of coin that is <=N and log it, then subtract that value from N. If it is not possible
to select the coin, move on to the next highest denomination of coin and repeat until N is equal to 0, at which point
you can return the totals for each type of coin.



1b)
Greedy Choice Property: the largest possible coin is 
chosen at each step, this is valid because any other combination of coins
would result in more coins.

Optimal Substructure: The problem reduces to finding the optimal solution for N - 2^k, so it has optimal substructure.

1c) Both the work and span for this algorithm are O(log n)


2a) when coins are [1, 3, 4] and N = 6, the greedy algorithm uses coins 4, 1, 1, which is 3 coins.
The optimal solution uses 3, 3, which is 2 coins, showing greedy fails.

2b) It still has optimal substructure because the minimum number of coins to make N can be built by
taking one coin (D_i) and solving the subproblem for N - D_i

2c) a dynamic programming algorithm fills a table dp where dp[i] is the fewest
coins needed to make i, and for each amount up to N, we try all denominations and set
dp[i] = min(dp[i], 1 + dp[i-D_i]). The work is O(N k) and the span is O(N)
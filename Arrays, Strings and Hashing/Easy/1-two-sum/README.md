<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

## Analysis of Approaches

### Brute Force Approach
**Description**: Check every pair of numbers to see if they sum to the target.
- **Time Complexity**: `O(n^2)`, where `n` is the number of elements in the list. This method checks every combination of elements in the array.
- **Drawbacks**: Inefficient for large arrays due to the high time complexity.

### Two-pointer Technique
**Description**: First sort the array, then use two pointers to find the two numbers that add up to the target.
- **Time Complexity**: `O(n log n)` due to the sorting step, then `O(n)` for the two-pointer scan.
- **Drawbacks**: Sorting the array can disrupt the indices, making it difficult to return the original indices of the numbers.

## Solution Explanation

The solution finds two indices of numbers in `nums` that add up to a specified `target` using a hash table. Here’s the approach in detail:

1. **Initialize Hash Table**: Create an empty dictionary (`pastNums`) to store previously seen numbers and their indices.
2. **Find Complement**:
    - Traverse each index and number in `nums`.
    - Calculate the complement by subtracting the current number from the target.
    - If the complement exists in the hash table, return the current index and the stored index of the complement, as they form the required pair.
    - Otherwise, store the current number with its index in the hash table.
3. **No Valid Pair**: If no pair is found that adds up to the target, return an empty result.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the input list. The lookup and insertion operations in the hash table both take constant time on average.
- **Space Complexity**: `O(n)` because the hash table needs to store the indices of all previously seen numbers.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: nums = [2,7,11,15], target = 9

1. **Processing Elements**:
   - First element is `2`. Complement needed is `9 - 2 = 7`.
   - Store `2` in the hash table: `{2: 0}`.
   - Next element is `7`. Hash table has the complement `7`.
   - Indices found: `0` and `1`.

**Output**: [0,1]

This step-by-step demonstration shows the efficiency and simplicity of using a hash table to quickly find the two indices that sum to the target by checking complements.

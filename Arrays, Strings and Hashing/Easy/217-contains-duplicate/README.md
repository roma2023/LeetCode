<h2><a href="https://leetcode.com/problems/contains-duplicate">Contains Duplicate</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solution Explanation

The solution checks if a given list of integers, `nums`, contains any duplicate values using a hash set. Here’s a brief outline of the approach:

1. **Initialize Hash Set**: Create an empty set to store unique numbers.
2. **Check Duplicates**:
    - Iterate through each number in the list.
    - If the number is already in the set, a duplicate is found, so return `True`.
    - If not, add the number to the set and continue.
3. **No Duplicates Found**: If the loop completes without finding any duplicates, return `False`.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the input list. Each lookup and insertion operation in the set takes constant time on average.
- **Space Complexity**: `O(n)` because the set needs to store all the distinct numbers in the worst case.

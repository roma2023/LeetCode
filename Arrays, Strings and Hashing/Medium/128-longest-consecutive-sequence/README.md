<h2><a href="https://leetcode.com/problems/longest-consecutive-sequence">Longest Consecutive Sequence</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solution Explanation

The solution finds the length of the longest consecutive elements sequence in an unsorted array using a set. Here’s the plan in detail:

1. **Initialize Set**: Convert the input list to a set to facilitate quick lookups of consecutive numbers.
2. **Find Sequences**:
    - Traverse each number in the input list.
    - If the current number does not have a preceding consecutive neighbor (i.e., `num - 1` is not in the set), then it marks the start of a new sequence.
    - Starting from this number, keep counting consecutive numbers until the next number isn't found in the set.
    - Track the maximum length of consecutive sequences found.
3. **Return Maximum Length**: Return the maximum length of any consecutive sequence.

### Complexity Analysis

- **Time Complexity**: `O(n)` since each number is only processed once when checking for consecutive sequences.
- **Space Complexity**: `O(n)` because the set stores all unique numbers from the input list.


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

The solution determines the length of the longest consecutive elements sequence in an unsorted array of integers using a hash set. This approach avoids the `O(n log n)` complexity of sorting by leveraging `O(1)` average time complexity for set operations. Here's how it is executed:

1. **Convert to Set**:
   - Convert the list of numbers into a set to enable quick checks for the existence of consecutive numbers.
2. **Find Consecutive Sequences**:
   - Iterate through each number in the original list.
   - For each number, check if it is the start of a new sequence. This is determined by checking if `num-1` is not in the set.
   - If it's the start of a sequence, use a counter to count how many consecutive numbers exist starting from this number.
3. **Track Maximum Length**:
   - Continuously update the maximum length encountered during the iteration.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the number of elements in the array. Each element is checked at most twice — once in the set conversion and once in the main iteration.
- **Space Complexity**: `O(n)`, due to the additional space required for the set that stores the elements of the array.

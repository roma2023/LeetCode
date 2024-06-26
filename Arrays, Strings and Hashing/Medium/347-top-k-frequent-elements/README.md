<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">Top K Frequent Elements</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>

## Analysis of Approaches

### Sorting Approach
**Description**: A simple method could involve sorting the numbers by frequency using a dictionary and then picking the top `k` entries.
- **Time Complexity**: `O(n log n)` due to the sorting step, which could be too slow for large datasets.

### Heap (Priority Queue) Approach
**Description**: Utilizing a min-heap to keep track of the top `k` frequent elements as you iterate through the frequency dictionary.
- **Time Complexity**: `O(n log k)`, where `n` is the number of unique elements and `k` is the heap size. This approach can be optimal for small `k` values.

## Solution Explanation

The solution finds the `k` most frequent elements in a list of integers using a bucket sort approach. Here's the method breakdown:

1. **Frequency Count**:
   - Use a dictionary (`count`) to record the frequency of each number in the list.
2. **Bucket Sort Preparation**:
   - Prepare a list of empty lists (`bucket`) where the index represents the frequency of the elements that will be stored at that index.
   - Populate the `bucket` such that each number is placed into the list at the index corresponding to its frequency.
3. **Retrieve Top K Frequent Elements**:
   - Start from the end of the `bucket` array (which corresponds to the highest possible frequency) and add elements to the result list (`res`).
   - Continue until `k` elements have been added to the result, which will be the most frequent elements.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input list. This efficiency comes from using the bucket sort method, which avoids the higher time complexity of comparison-based sorting.
- **Space Complexity**: `O(n)` due to the storage needed for the `count` dictionary and the `bucket` list, which together hold all unique elements and their frequencies.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: nums = [1,1,1,2,2,3], k = 2

1. **Frequency Count**:
   - Count: `{1: 3, 2: 2, 3: 1}`
2. **Bucket Sort Preparation**:
   - Bucket: `[[], [3], [2], [1]]`
3. **Retrieve Top K Frequent Elements**:
   - Start from the end and pick the top 2 elements: `1` and `2`.

**Output**: [1, 2]

This demonstration shows how efficiently the solution identifies the `k` most frequent elements using bucket sort, particularly effective for distributing and categorizing data based on frequency.

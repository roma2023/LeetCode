<h2><a href="https://leetcode.com/problems/product-of-array-except-self">Product of Array Except Self</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>

## Solution Explanation

The solution calculates the product of all elements in an array except for the element itself without using division. This is achieved using prefix and postfix products. Here's the method in detail:

1. **Initialize Result Array**:
   - Start with a result array `res` initialized with 1s. This array will store the result of the product except self for each element.
2. **Calculate Prefix Product**:
   - Iterate through the array from the start, updating `pre` to hold the product of all previous numbers. Update the result array such that each element at index `i+1` holds the product of all numbers before it.
3. **Calculate Postfix Product**:
   - Iterate through the array from the end, updating `post` to hold the product of all following numbers. Simultaneously, update the result array to multiply the existing value by the product of all numbers after it.
4. **Combine Prefix and Postfix**:
   - By the end of these operations, each element in the result array represents the product of all other elements in the array except itself.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the number of elements in the array. Each element is visited a constant number of times (once for prefix calculations and once for postfix calculations).
- **Space Complexity**: `O(n)` for the result array that is returned. The additional space used for the `pre` and `post` variables is constant, `O(1)`.

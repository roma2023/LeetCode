<h2><a href="https://leetcode.com/problems/valid-palindrome">Valid Palindrome</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

## Analysis of Approaches

### Sorting Both Strings
**Description**: A straightforward approach would be to sort both strings and then compare them for equality.
- **Time Complexity**: `O(n log n)` due to the sorting process, where `n` is the length of the string.
- **Space Complexity**: `O(n)` needed to store the sorted strings if strings are immutable.
- **Drawbacks**: While simple, sorting can be slower for large strings and is less efficient than using hash tables.

### Two Pointer Technique
**Description**: Use two pointers to compare characters from the beginning and end, moving toward the center. This is the approach used in the solution.
- **Pros**: Efficient in terms of space, only requires a few comparisons and minimal extra space.
- **Time Complexity**: `O(n)`, where `n` is the length of the string after cleaning non-alphanumeric characters.
- **Space Complexity**: `O(1)`.

## Solution Explanation

The solution verifies if a string `s` is a palindrome by using two pointers to check characters from both ends, moving towards the center, after normalizing the string by removing non-alphanumeric characters and converting to lowercase. Here’s the step-by-step approach:

1. **Initialize Two Pointers**: `left` starts at the beginning, `right` at the end of the string.
2. **Skip Non-Alphanumeric Characters**: Move pointers inward to skip any characters that aren't letters or numbers.
3. **Compare Characters**: Compare characters at the `left` and `right` pointers:
   - If they are different, the string is not a palindrome.
   - Move the pointers towards the center and continue comparison.
4. **Determine Palindrome**: If all characters match up correctly, return `true`. If any mismatch is found, return `false`.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the string. We potentially examine each character once.
- **Space Complexity**: `O(1)`, as this approach only uses two pointers and does not require additional space for another data structure.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: s = "A man, a plan, a canal: Panama"

1. **Processing**:
   - Normalize by ignoring spaces and punctuation, compare using two pointers.
   - Check 'A' vs 'a', 'm' vs 'm', etc., adjusting pointers as you go.

**Output**: true

This demonstration clearly illustrates how the two-pointer technique efficiently determines if a string is a palindrome without requiring extra space for string manipulation.

<h2><a href="https://leetcode.com/problems/valid-anagram">Valid Anagram</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

## Analysis of Approaches

### Sorting Both Strings
**Description**: A straightforward approach would be to sort both strings and then compare them for equality.
- **Time Complexity**: `O(n log n)` due to the sorting process, where `n` is the length of the string.
- **Space Complexity**: `O(n)` needed to store the sorted strings if strings are immutable.
- **Drawbacks**: While simple, sorting can be slower for large strings and is less efficient than using hash tables.

### Counting Frequency with Array
**Description**: Since the problem is constrained to lowercase letters, use a fixed-size array of 26 to count character frequencies.
- **Pros**: Faster and more space-efficient for problems limited to a single case alphabetic characters.
- **Time Complexity**: `O(n)`, where `n` is the length of the strings.
- **Space Complexity**: `O(1)`, since the size of the array is constant and does not scale with the size of the input.

## Solution Explanation

The solution verifies whether two strings `s` and `t` are anagrams by counting the frequency of characters in each string. The algorithm uses a hash table (Python dictionary) to keep track of the frequency differences between `s` and `t`. Here’s the step-by-step approach:

1. **Initial Length Check**: If the strings have different lengths, they're not anagrams.
2. **Frequency Count**: Traverse both strings simultaneously. Increment the count for each character in `s` and decrement the count for each character in `t`.
3. **Validation**: After processing both strings, check if all counts are zero. If any count is non-zero, the strings are not anagrams.

### Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the input strings. We iterate through both strings once and then validate the frequency table.
- **Space Complexity**: `O(n)` because the hash table stores the frequency of up to `n` distinct characters.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: s = "anagram", t = "nagaram"

1. **Initialize Hash Table**: Create a dictionary to count character occurrences.
2. **Increment and Decrement Counts**:
   - For `s = "anagram"`, increment counts.
   - For `t = "nagaram"`, decrement counts.
3. **Check for Zero Counts**: All counts are zero, indicating all characters match in frequency.

**Output**: true

This demonstration clearly shows the efficiency of using a hash table to quickly verify if two strings are anagrams by ensuring their character counts are identical.

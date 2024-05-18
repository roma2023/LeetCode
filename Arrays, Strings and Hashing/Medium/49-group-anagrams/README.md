<h2><a href="https://leetcode.com/problems/group-anagrams">Group Anagrams</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

## Analysis of Approaches

### Sorting Each String
**Description**: One could sort the characters of each string and use the sorted string as a key in a hash map to group anagrams.
- **Pros**: Simple and intuitive.
- **Time Complexity**: `O(n * m log m)`, where `n` is the number of strings and `m` is the maximum length of a string, due to the sorting overhead.

### Frequency Counting (Optimized)
**Description**: Using a frequency count of each letter in a string to create a hashable signature, as implemented in the optimal solution. This avoids the need for sorting.
- **Pros**: Faster than sorting, especially for longer words.
- **Time Complexity**: `O(n * m)`, more efficient than sorting when `m` is large.

## Solution Explanation

The solution groups anagrams from a list of strings using a character count signature method. Here’s how it works:

1. **Initialize Hash Table**: Use a hash table (`defaultdict`) to group words by their character signatures.
2. **Generate Signatures**:
   - For each word in the list, initialize a fixed-size array (`signature`) of length 26 to zero, corresponding to the counts of each alphabet letter.
   - Count the frequency of each character in the word and update the `signature` array.
   - Convert the `signature` array to a tuple (to use it as a hashable key in the dictionary) and append the word to the corresponding list in the hash table.
3. **Collect Results**: Return the values of the hash table, which contain lists of anagrams.

### Complexity Analysis

- **Time Complexity**: `O(n * m)`, where `n` is the number of words and `m` is the average length of the words. The factor of 26 in the complexity arises from processing each character of each word to compute its signature, but it's generally absorbed into the `m` term.
- **Space Complexity**: `O(n * m)` because the hash table stores a key for each unique signature and a list of words corresponding to each signature. Each key is an array of length 26, and the words themselves take space proportional to their total length across all anagrams.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

1. **Generating Signatures and Grouping**:
   - "eat", "tea", "ate" share the same signature `[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`.
   - "tan", "nat" share the signature `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]`.
   - "bat" has the unique signature `[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`.

2. **Results**:
   - Groups formed: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

**Output**: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

This demonstration clearly shows how the solution effectively groups anagrams based on character signatures, ensuring a fast and accurate grouping.

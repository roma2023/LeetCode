<h2><a href="https://leetcode.com/problems/encode-and-decode-strings">Encode and Decode Strings</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Design an algorithm to encode <b>a list of strings</b> to <b>a string</b>. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>

<pre>
string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}</pre>
Machine 2 (receiver) has the function:

<pre>
vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}
</pre>

<p>So Machine 1 does:</p>

<pre>
string encoded_string = encode(strs);
</pre>

<p>and Machine 2 does:</p>

<pre>
vector&lt;string&gt; strs2 = decode(encoded_string);
</pre>

<p><code>strs2</code> in Machine 2 should be the same as <code>strs</code> in Machine 1.</p>

<p>Implement the <code>encode</code> and <code>decode</code> methods.</p>

<p>You are not allowed to&nbsp;solve the problem using any serialize methods (such as <code>eval</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;Hello&quot;,&quot;World&quot;]
<strong>Output:</strong> [&quot;Hello&quot;,&quot;World&quot;]
<strong>Explanation:</strong>
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---&gt; Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;&quot;]
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> contains any possible characters out of <code>256</code> valid ASCII characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Could you write a generalized algorithm to work on any possible set of characters?</p>

## Analysis of Approaches

### Delimiter-Based Approach
**Description**: An initial thought might be to use a special character as a delimiter to separate strings. However, this approach fails if the delimiter character is present in the input strings.
- **Drawbacks**: Requires escaping or encoding delimiter characters if they appear in input strings, complicating the process.

### JSON or XML Encoding (Not Allowed)
**Description**: Using JSON or XML to serialize the list of strings could be intuitive and robust but does not comply with the problem's constraints against using serialization methods like `eval`.
- **Drawbacks**: Not allowed by the problem constraints, and typically overkill for the task.

## Solution Explanation

This solution involves encoding and decoding a list of strings into a single string using a length-based encoding scheme. Here’s the approach in detail:

### Encode Method

1. **Iterate Through Strings**: For each string in the input list, compute its length.
2. **Build Encoded String**: Append to the result string a format that consists of the length of the string, followed by a hash (`#`), and then the string itself. This format helps to precisely determine where each string begins and ends in the encoded string.
3. **Return Encoded String**: The output is a single string that contains all the encoded strings concatenated together.

### Decode Method

1. **Initialize Variables**: Start with an empty list to hold the decoded strings.
2. **Extract Strings**:
   - Continuously look for the hash (`#`) to find the next string's length.
   - Use this length to slice the appropriate substring from the encoded string.
   - Append the extracted substring to the list of decoded strings.
   - Remove the processed portion from the encoded string.
3. **Return Decoded List**: The output is a list of strings that were originally encoded.

### Complexity Analysis

- **Time Complexity**: 
  - **Encode**: `O(n)`, where `n` is the total number of characters across all strings. Each string is processed linearly to build the encoded string.
  - **Decode**: `O(n)`, since each character in the encoded string is processed once to rebuild the original list of strings.
- **Space Complexity**: `O(n)`, where `n` is the total length of the input string list. The space is used for storing the encoded string and the temporary variables during decoding.

## Demonstration of the Optimal Solution

### Example Using Input 1

**Input**: ["Hello", "World"]

1. **Encoding**:
   - "Hello" is encoded as "5#Hello"
   - "World" is encoded as "5#World"
   - Combined encoded string: "5#Hello5#World"

2. **Decoding**:
   - Extract "5#Hello": Recognizes '5' as the length, extracts "Hello".
   - Extract "5#World": Recognizes '5' as the length, extracts "World".

**Output**: ["Hello", "World"]

This demonstration shows the seamless encoding and decoding process, ensuring that the data remains intact through transmission.


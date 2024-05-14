import functools
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        length = 0
        encoded_string = ""
        for string in strs:
            length = len(string)
            encoded_string += f'{str(length)}#{string}'
        return encoded_string

        """
        So just to clarify, what are the strings can be, can they be None, what's a length of the string? Is it of any length, can it be an empty string? 

        So, hmmm here we can of using some hashing functions, we could encode each character of a string into their respective ASCII numbers but we need to separate them using somas, so if we are given a list like this:
        ["ab", "bc"] => ["25,26","26,27"]
        but then we also need to come up with the strings sepeerator, which I think can be a space for example, in that case
        ["ab", "bc"] => ["25,26","26,27"] => "25,26 26,27"

        ["25,26","26,27"] => [["25", "26"], ["26", "27"]] => [["a", "b"],["b", "c"]] => ["ab", "bc"]

        in our decode function, we could use string.split(" ") to split between strings, then later once we have the list of strings, we could split each string into strings of ASCII numbers then turn them into a characters and join them using "".join(string)
        
        alright an empty string has no ASCII value, hence we could have it as an exception and directly pass it as a character % to distinguish it among othwer strings, right?

        so in the example of, ["ab", "bc", ""] => "25,26 26,27 %"
        """

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list = []
        decoded_string = ""
        length = 0
        
        while s != "":
            index_of_length = s.find("#")
            length = int(s[0 : index_of_length])
            decoded_list += [s[index_of_length + 1 : index_of_length + 1 + length]]
            s = s[index_of_length + 1 + length :] 
        
        return decoded_list

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
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
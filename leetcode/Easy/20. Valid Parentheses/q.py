class Solution:
    def isValid(self, s: str) -> bool:
        compare_char = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char in compare_char.values() : # Open bracket stack push
                stack.append(char)
            else:
                if(stack and stack[-1] == compare_char[char]) : # Stack Top is Open bracket("(", "[", "{") And Compare Close bracket (")", "]", "}")
                    stack.pop() # Compare result is same Type :Stack Pop
                else :
                    return False # Compare result is different type :Return False
        if stack: # Stack is not empty
            return False
        return True

def main(*string) -> bool:
    t = Solution()
    return t.isValid(string)

if __name__ == "__main__":
    string = "{}[]"
    return_value = main(string)
    print(return_value)
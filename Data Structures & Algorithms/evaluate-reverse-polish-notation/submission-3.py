class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                nums.append(int(token))
            else:
                match token:
                    case "+":
                        nums[-2] += nums[-1]
                    case "-":
                        nums[-2] -= nums[-1]
                    case "*":
                        nums[-2] *= nums[-1]
                    case "/":
                        nums[-2] = int(nums[-2] / nums[-1])

                nums.pop()
        
        return nums[0]

                
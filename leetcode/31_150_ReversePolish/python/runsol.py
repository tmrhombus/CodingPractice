from solution import Solution 

tokens = ["1", "2", "+"]
tokens = ["2","1","+","3","*"]  # 9
tokens = ["4","13","5","/","+"] # 6
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22


sol = Solution()
out = sol.evalRPN(tokens)

print(f"tokens: {tokens}")
print(f"{out}")


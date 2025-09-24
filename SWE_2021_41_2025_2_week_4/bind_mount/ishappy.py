def isHappy(n):
    history = set()
    while n != 1 and n not in history:
        history.add(n)
        n = sum(int(eachDigit)**2 for eachDigit in str(n))
    return n == 1

if __name__ == "__main__":
    sample1_output = isHappy(19)
    sample2_output = isHappy(2)
    
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample1_output}\n")
        f.write(f"2: {sample2_output}\n")
    
    print("Results saved to /app/bind_mount/output.txt")
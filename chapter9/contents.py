with open ("chapter9/log.txt", "r") as f:
    line = f.read()
    
    lineo = 13 
    for line in line:
        if("Lorem ipsum dolor" in line):
            print(f"yes Lorem ipsum dolor is present in line no. {lineo}")
            break
        lineo += 1
    else:
        print("Lorem ipsum dolor is not present in the log file.")
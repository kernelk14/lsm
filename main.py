#!/usr/bin/env pypy3

# LSM: Like aSseMbly. (like assembly)

# program = 'start: move 5 to reg1'.split()

file = open("test.lsm", 'r')
program = file.read().split()
ip = 0

stack = []
reg1 = []
reg2 = []
reg3 = []

for ip in range(len(program)):
    code = program[ip]
    print(f"Stack: {stack}")
    if code.endswith(':'):
        if code.startswith('start'):
            print("Scanning starting point")
        elif not code.startswith('start'):
            print("ERROR: No starting point found.")
            exit(1)
        else:
            print("No starting point found.")
        ip += 1
    elif code == 'move': 
        if program[ip + 1].isdigit():
            stack.append(int(program[ip + 1]))
        else:
            print(f"WARNING: In pos {ip}, instruction `{code}`: We can only push numbers yet.")
        ip += 1
    elif code == 'to':
        print(f"Next: `{program[ip+1]}`")
        if program[ip + 1] == 'reg1':
            a = stack.pop()
            reg1.append(a)
            print(f"Register 1: {reg1}")
        if program[ip + 1] == 'reg2':
            a = stack.pop()
            reg2.append(a)
            print(f"Register 2: {reg2}")
        if program[ip + 1] == 'reg3':
            a = stack.pop()
            reg3.append(a)
            print(f"Register 3: {reg3}")
        else:
            if program[ip+1] == 'reg1':
                ip += 1
                continue
            print(f"ERROR: In instruction `{program[ip+1]}`: Unknown register redirection")
        ip += 1
    elif code.isdigit():
        ip += 1
        continue
    elif code == 'reg1':
        ip += 1
        continue
    
    else:
        print(f"ERROR: In pos {ip}, unknown instruction `{code}`.")
        ip += 1
    ip += 1

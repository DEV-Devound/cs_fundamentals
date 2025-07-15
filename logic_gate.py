def and_gate(a, b):
    a_bool = bool(a)
    b_bool = bool(b)
    result = a_bool and b_bool
    return int(result)
def or_gate(a, b):
    a_bool = bool(a)
    b_bool = bool(b)
    result = a_bool or b_bool
    return int(result)
def not_gate(a):
    result = int(bool(bool(a)))
    return int(result)
def xor_gate(a, b):
    if (a != b):
        result = True
    else: 
        result = False
    return int(result)
def nand_gate(a, b):
    a_bool = bool(a)
    b_bool = bool(b)
    result = not (a_bool and b_bool)
    return int(result)
def nor_gate(a, b):
    a_bool = bool(a)
    b_bool = bool(b)
    result = not(a_bool or b_bool)
    return(int(result))

inputs = [(0, 0), (0,1), (1, 0), (1, 1)]
print("A B | AND OR XOR NAND NOR")
print("-------------------------")
for a, b in inputs:
    and_out = and_gate(a, b)
    or_out = or_gate(a, b)
    xor_out = xor_gate(a, b)
    nand_out = nand_gate(a, b)
    nor_out = nor_gate(a, b)
    print(f"{a} {b} |  {and_out:<3} {or_out:<3} {xor_out:<3} {nand_out:<4} {nor_out:<3}")
print("\nA | NOT")
print("---------")
for a in [0, 1]:
    print(f"{a} |  {not_gate(a)}")

def combined_1(a, b, c):
    return or_gate(and_gate(a, b), not_gate(c))
def combined_2(a, b, c, d):
    return xor_gate(nand_gate(a, b), nor_gate(c, d))
print("AND_GATE OR NOT_GATE: ", combined_1(1, 0, 0))
print("NAND_GATE XOR NOR_GATE", combined_2(0, 1, 0, 0))

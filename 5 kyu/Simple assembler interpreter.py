def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        temp, r, s = (program[i] + ' 0').split()[:3]
        if temp == 'inc': d[r] += 1
        if temp == 'dec': d[r] -= 1        
        if temp == 'mov': d[r] = d[s] if s in d else int(s)
        if temp == 'jnz' and (d[r] if r in d else int(r)): i += int(s) - 1
        i += 1
    return d
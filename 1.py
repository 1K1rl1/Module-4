def strcounter(s): #Сложность O(N**2)
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)    
                       
def strcounter_new(s): #O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym,count in syms_counter.items():
        print(sym, count)

strcounter_new('aaaaaabbbbbbbcccdcdccdcdcdcs')

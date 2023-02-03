def isisomorphic(s,t):
    dict_s={}
    dict_t={}
    for i,value in enumerate(s):
        dict_s[value]=dict_s.get(value,[])+[i]
    for j,value in enumerate(t):
        dict_t[value]=dict_t.get(value,[])+[j]
    if sorted(dict_s.values())==sorted(dict_t.values()):
        return True
    else:
        return False
print(isisomorphic("egg","add"));
print(isisomorphic("foo","bar"));
print(isisomorphic("paper","title"));
print(isisomorphic("fry","sky"));
print(isisomorphic("apples","apple"));
                   

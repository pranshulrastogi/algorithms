def get_substrs(s,i,l):
    if i>=l:
        return [""]
    else:
        substrs = get_substrs(s,i+1,l)
        res = []
        for sub in substrs:
            res.append(s[i]+sub)
            res.append(sub)
        return res



if __name__ == "__main__":
    print(get_substrs('ab',0,2))
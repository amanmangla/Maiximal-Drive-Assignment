def lenOfLongSubstring(s):
    str_list=[]
    max_len=0
    
    for i in s:
        if i in str_list:
            str_list=str_list[str_list.index(i)+1:]
            
        str_list.append(i)    
        max_len=max(max_len,len(str_list))
        
    return max_length
    
str=input()
print(lenOfLongSubstring(str))
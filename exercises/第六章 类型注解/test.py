# 函数类型注解
def calc(score: list[int])->float:
    return sum(score)/len(score)

print(calc([100,98,84]))

# 又忘了 函数一次性返回多个值时 返回的就是元组
def function1(score:list[int])->tuple[int,int,float]:
    max_s=max(score)
    min_s=min(score)
    avg_s=sum(score)/len(score)
    return max_s,min_s,avg_s

max_val,min_val,avg_val=function1([99,72,56])
print(max_val,min_val,round(avg_val,2))
    


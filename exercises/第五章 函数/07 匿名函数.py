out_line=lambda : print("----------")
add=lambda x,y:x+y

out_line()
print(add(1,2))
# 需求：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list =["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript","Rust"]
# 注意sort与sorted的区别
#但此处是自定义排序按照字符个数排序 所以 需要进行自定义排序
#细节注意 语法是 ---- key=函数名
def get_len(zifuchuan):
    return len(zifuchuan)
data_list.sort(key=get_len)
print(data_list)

data_list.sort(key=lambda item :len(item))
print(data_list)

data_list.sort(key=lambda item :len(item),reverse=True)
print(data_list)
## 详细理解
# sort()遍历列表，把列表中每一个原始元素，挨个传入key指定的函数。
# key 函数执行，返回加工后的参考值（这里就是字符串长度数字）。
# sort不修改原始元素，只对比这一堆参考值的大小，决定先后顺序。
# 根据参考值的大小关系，把原始的字符串元素调换位置。
# reverse=True就把参考值的比较结果反转，实现降序。
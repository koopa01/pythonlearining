# day 06 - 19.看代码写结果并解释原因
info = [1,2,3]
userinfo = {'account':info, 'num':info, 'money':info}

info.append(9)
print(userinfo) # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}

info = "题怎么这么多"
print(userinfo) # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
# 第一个输出  因为开辟空间后,info在第二层内存地址进行了修改,所以userinfo也发生了改变
# 第二个输出  因为info指向了另一个内存地址,但userinfo没有发生改变
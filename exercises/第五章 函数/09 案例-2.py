"""
电商订单计算器---定义一个函数
用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
具体规则如下：
  1.优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
  2.积分抵扣需要商品总金额满 5000 才可以使用,100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def calc_order_cost(*args,coupon,score,express):
    """根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    *args: 一批商品的信息（商品名、价格、数量）
    coupon:优惠券金额
    score:积分
    express:运费
    return 订单的总金额
    """
#1.计算商品的总金额
    cost=0
    for s in args:
        each_cost=s[1]*s[2]
        cost+=each_cost
#2.计算优惠券部分优惠金额
    youhui=0
    if cost>=5000 and coupon<=cost:
        youhui=coupon
        
# 自己写时候1.忘记整除的写法2.忽略了2种抵消加起来可能超过原先价格

    # if cost>=5000 and score//100>=1:
    #     if cost>=score//100:
    #         youhui+=score//100
    # if cost-youhui>=0:
    #     return cost-youhui + express
    # else:
    #     return express
#3.计算积分部分优惠金额
    if cost>=5000:
        score_deduct=score//100
        if cost>=score_deduct:
            youhui +=score_deduct
    youhui=min(youhui,cost)
#4.加运费后返回
    return cost-youhui+express
    

print(calc_order_cost(["A",2,2500],["B",2,2500],coupon=500,score=0,express=1))
print(calc_order_cost(["A",2,2500],coupon=500,score=100,express=1))
    
    
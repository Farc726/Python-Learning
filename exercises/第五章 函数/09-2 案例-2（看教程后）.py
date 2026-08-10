"""
电商订单计算器---定义一个函数
用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
具体规则如下：
  1.优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
  2.积分抵扣需要商品总金额满 5000 才可以使用,100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
#设置参数
#小细节 若没有优惠券积分免运费---不传递参数-->可设置默认参数0
def calc_order_cost(*args,coupon=0,score=0,express=0):
#1.计算商品金额（这里用列表来存放每个商品的总金额后sum）
    total_cost=[s[1]*s[2] for s in args]
    total=sum (total_cost)
#2.计算优惠券部分优惠金额
    youhui=0
    if total>=coupon and total>=5000:
        youhui+=coupon

#3.计算积分抵扣部分优惠金额
    if total>=5000 and score//100>=1:
        youhui+=score//100
        
    youhui=min(youhui,total)
#4.加上运费 即可 返回
    return total-youhui+express
    
print(calc_order_cost(("A",188,2),("B",388,1),("C",6999,1),coupon=10,score=4000,express=9.9))
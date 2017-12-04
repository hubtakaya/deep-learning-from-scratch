#coding: utf-8
from layer_native import *


apple = 100
apple_num = 2

orange = 150
orange_num = 3

tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_price_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
add_price = add_price_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(add_price, tax)

#backward
dprice = 1
dadd_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_price_layer.backward(dadd_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)

print("price: ", int(price))
print("dapple: ", dapple)
print("dorange: ", dorange)
print("dApple_num: ", int(dapple_num))
print("dOrange_num: ", int(dorange_num))
print("dTax: ", dtax) 


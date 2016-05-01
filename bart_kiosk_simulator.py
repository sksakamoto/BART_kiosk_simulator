def load_card(num1, num5, num10, num20):
	ones = num1*1
	fives = num5*5
	tens = num10*10
	twenties = num20*20
	total = ones + fives + tens + twenties
	return total
print load_card(0,0,0,0)
print load_card(0,0,0,9)
print load_card(2,3,0,0)
print load_card(3,1,1,3)


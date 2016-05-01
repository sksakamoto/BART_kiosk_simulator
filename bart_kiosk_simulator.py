def load_card(num1, num5, num10, num20):
	ones = num1*1
	fives = num5*5
	tens = num10*10
	twenties = num20*20
	total = ones + fives + tens + twenties
	return total

clipper_card1 = load_card(1,0,0,0)
clipper_card2 = load_card(0,0,0,1)
clipper_card3 = load_card(1,1,0,0)
clipper_card4 = load_card(2,1,1,0)

DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def travel_to_destination(fare_price, card_value):
	if card_value >= fare_price:
		print "Welcome aboard, enjoy your trip!"
	else: 
		print "You need more money!"

print travel_to_destination(clipper_card1, FREMONT_TO_COLMA)
print travel_to_destination(clipper_card2, HAYWARD_TO_CONCORD)
print travel_to_destination(clipper_card3, DUBLIN_TO_POWELL)
print travel_to_destination(clipper_card4, FRUITVALE_TO_UNION_CITY)


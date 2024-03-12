def areSamosasSufficient(guests, doughSheets, mincedMeat, kiriCheese, requests):
    Samosas_Meat_Amount = min(doughSheets,(mincedMeat/5))
    Samosas_Cheese_Amount = kiriCheese/2
    Samosas_Meat_wanted = sum([request[0] for request in requests])
    Samosas_Cheese_wanted = sum([request[1] for request in requests])

    if (Samosas_Meat_wanted <= Samosas_Meat_Amount) and (Samosas_Cheese_wanted <= Samosas_Cheese_Amount):
        return("يكفي")
    else:
        print("ما يكفي")

print(areSamosasSufficient(5,20,40,14,[[1,1],[3,2],[2,3],[2,1],[2,2]]))
# لازم يكون عندنا 18 جبنة عشان نسوي 9 سمبوسات جبن و لازم يكون عندنا 50 قرام لحم عشان نسوي سمبوسات لحم
print(areSamosasSufficient(5,20,50,18,[[1,1],[3,2],[2,3],[2,1],[2,2]]))

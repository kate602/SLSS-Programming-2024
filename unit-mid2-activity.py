# Midunit Exercise
# Kate Jiang
# 4/09/2024'

item_list = [
    ["multigrain bread", "$4"],
    ["white bread", "$3"],
    ["rasberry jam", "$3.99"],
    ["smooth peanut butter", "$6"],
    ["wholewheat bread", "$3"],
    ["strawberry jam", "$4.50"],
    ["bread sticks", "$5"],
    ["orange juice", "$3"],
    ["apple juice", "$2.50"],
    ["sourdough bread", "$5.50"],
    ["grape jam", "5.29"],
    ["orange jam", "4.29"],
    ["cinammon raison bread", "$4.50"],
    ["cheese", "$4.50"],
    ["apples", "$6"],
]

#item_list_dict = {
#   "white bread": "$3",
#}

#item_list_dict["white bread"]

def findSimilarItems(keyword: str):
    similar_list = []

    for item in item_list:
        if item[0].find(keyword) >= 0:
            similar_list.append(item)

    return similar_list

def findcheapest(item_list: list):
    cheapest_price = 9999
    cheapest_item = []

    for item in item_list:
        cur_price = float(item[1][1:])

        if cur_price < cheapest_price:
            cheapest_price = cur_price
            cheapest_item = [item[0]]
        elif cur_price == cheapest_price:
            cheapest_item.append(item[0])

    return cheapest_item

similar_list1 = findSimilarItems("bread")
print(findcheapest(similar_list1))

similar_list2 = findSimilarItems("juice")
# print(findcheapest(similar_list2))
print(similar_list2)

similar_list3 = findSimilarItems("jam")
print(findcheapest(similar_list3))
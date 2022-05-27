if __name__ == "__main__":
    dict = {"fruit": "Mango", "Country": "Nigeria", "Salary": 2000, "Scores":[30,40,50]}
    keys =dict.values()
    print(keys)
    scores = dict.get("Scores")
    print(scores)

    scores[0] = 390
    print(dict)

    dict.update({"fruit": "Apple"})
    print(dict)

    dict.pop("Country")
    print(dict)

for x in ([20, 40, 50, 15]):
    print(x)
    if x == 40:
        break
    print("All is good")


















import random
people = ["Waldo", "William", "Wesley", "Wyatt", "Walson", "Walter", "Waylon", "Winston", "Wallace", "Willie", "Waylen", "Wolf", "Wendel", "Woodrow", "Willow", "Willem", "Wayland", "Whitley", "Wolfe", "Williams", "Woods", "Welles", "Whoot", "Wilbur", "Wilfredo", "Whitten", "Wilfred", "Wario", "Warrick", "Winner", "Wright", "Wayden"]
zin = 'Waldo zit op stoelnummer'
index = 0
random.shuffle(people)
print(people)
for x in people:
    if x == 'Waldo':
    
        print(zin, index)
    index += 1
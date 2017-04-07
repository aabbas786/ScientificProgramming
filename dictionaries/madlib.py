s = """Tonight's the {noun1}! The one {noun2} we all wait for, well next to {holiday}. {person} and I are going to be a {noun3}. The {noun4} turn {color}. The {vegetables} are lit. We're ready to collect our {noun5}."""

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
holiday = input("Enter a holiday: ")
person = input("Enter the name of a person: ")
noun3 = input("Enter another noun: ")
noun4 = input("One more noun please: ")
color = input("One color please: ")
vegetables = input("Name any vegetable (plural): ")
noun5 = input("Just one last noun please and thank for your time: ")
s1 = s.format(noun1=noun1, noun2=noun2, holiday=holiday, person=person, noun3=noun3, noun4=noun4, color=color, vegetables=vegetables, noun5=noun5)

print(s1)

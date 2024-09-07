#print("whats up alfred")
name=["louis", "joker", "wally"]
birthday=["22/22", "31/31", "09/07"]
import datetime
today=datetime.datetime.now()
print(today)
today=str(today)
today=today.split()
print(today)
today=today[0]
print(today)
today=today.split("-")
print(today)
today=today[1:]
print(today)
today="/".join(today)
print(today)
for fkj in range(len(birthday)):
    if today==birthday[fkj]:
        print(name[fkj])
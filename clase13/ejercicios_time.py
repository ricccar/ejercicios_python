from datetime import date

d = date.fromisoformat("20261207")  # año mes y dia
print(d)

d = date.strptime("20-06-1297", "%d-%m-%Y")  # año mes y dia
print(d)

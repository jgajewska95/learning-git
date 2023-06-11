Lista_zakupów = {'Piekarnia': ['chleb', "bułki", "pączek"],
             'Warzywniak': ["marchew", "seler", "rukola"],}
for x, y in Lista_zakupów.items():
  print(f"Idę do {x}, kupuję tu następujące rzeczy: {y}".title())

  d = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["chleb", "bułki", "pączek"]
  }
values = list(d.values())

count = 0
# flat_list = []
for sublist in values:
    count += len(sublist)
    # flat_list += sublist
print(f"w sumie kupuję {count} produktów")


from contact_data import contacts

ali_email = contacts["Ali"]["email"]
ali_phone = contacts["Ali"]["phone_number"]
print(ali_email, ali_phone)

print(contacts["Ali"]["phone_number"], contacts["Zainab"]["email"], contacts["Ibrahim"]["phone_number"])

for key in ('Ali', 'Zainab', 'Ibrahim'):
    print(contacts[key])


def add(n1, n2):
    total = n1 + n2
    return total


print(add(35, 49))


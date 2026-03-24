contacts = {
  "Alice": "555-1234",
  "Renan": "533-3234",
  "Andrea": "333-4444",
}
print(f"Alice's number: {contacts["Alice"]}")
contacts["Diana"] = "111-4545"
print(f"Contacts after the adding Diana: {contacts}")
contacts["Renan"] = " 555-0000"
print(f"Contacts after the updating Renan: {contacts}")
del contacts["Alice"]
print(f"Contacts after deleting Alice: {contacts}")
print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"All contacts: {len(contacts)}")
new_links = []
old_links = []
with open("NewLink.txt", "r") as file:
    for i in file.readlines():
        if i not in new_links:
            new_links.append(i)
with open("OldLinks.txt", "r") as file:
    for i in file.readlines():
        if i not in old_links:
            old_links.append(i)

print("Size of New Links: " + str(len(new_links)))

# Print Unique Links from both arrays
with open("UniqueLinks.txt", "w") as file:
    for i in new_links:
        if i not in old_links:
            file.write(i)
print("\n\n ###################### Search Completed ######################\n\n")

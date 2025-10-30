names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
unique_names_ordered = []

for name in names:
    if name not in unique_names_ordered:
        unique_names_ordered.append(name)

print(unique_names_ordered)
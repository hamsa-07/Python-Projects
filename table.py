from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["a", "b", "c"])
table.add_column("Type", ["1","2", "3"])

table.align = "l"
print(table)
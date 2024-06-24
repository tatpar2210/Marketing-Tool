import pandas as pd

location = str(input("Enter the CSV file location: "))
sep = str(input("Provide separator used: "))
csv_file = pd.read_csv(location, sep)

dct_1 = dict(csv_file)
dct_1_keys = list(dct_1.keys())

# Making of empty dictionary to bring dataframe dictionary to normal dictionary,
# otherwise will get an error.
dct_2 = {}

for a in range(0, len(dct_1_keys)):
    s = {dct_1_keys[a]: list(dct_1.get(dct_1_keys[a]))}
    # adding up dct_1(CSV file dictionary) elements to dct_2(normal dictionary).
    dct_2.update(s)
# print(dct_2)

# Column Names
dct_2_keys = list(dct_2.keys())
# print(dct_2_keys)

choice_2 = ""
str_1 = "Changes can be done in {} select any one: "
while choice_2 != "Done":
    # getting product_name list to show up in input string.
    print("If finished type [Done]")
    choice_2 = str(input(str_1.format(dct_2_keys)))
    dct_3 = {}

    for i in range(0, len(dct_2_keys)):
        # matches user input with dictionary field name in which changes to be made.
        if choice_2 == dct_2_keys[i]:
            print(csv_file)

            # What element user wanna changes.
            index = int(input("Give index that to be changed="))

            # Assigning variable for the position of the element in changing field.
            change_at = dct_2.get(dct_2_keys[i])[index]
            # print(change_at)
            # Changing of elements
            str_2 = "Change {} by="
            if type(change_at) == str:
                dct_2.get(dct_2_keys[i])[index] = str(input(str_2.format(change_at)))

            elif type(change_at) == int:
                dct_2.get(dct_2_keys[i])[index] = int(input(str_2.format(change_at)))

            else:
                "Invalid Data Type!!"
        x = {dct_2_keys[i]: list(dct_2.get(dct_2_keys[i]))}
        # Fully-Final dictionary##
        i += 1
        dct_3.update(x)
print("\n")
# print(dct_3)
# print(dct_2.get(dct_2_keys[i]))

df_2 = pd.DataFrame(dct_3)
print(df_2)

# Sorting of CSV (Optional)
sort_ch = str(input("Wanna do sorting in csv file(Y/N): "))
if sort_ch == "Y":
    str_6 = "Sort by({}): "
    sort_by = str(input(str_6.format(dct_2_keys)))
    df_2.sort_values(by=sort_by, ascending=True, inplace=True)
    print(df_2)
else:
    pass

# Saving of dataframe to csv
str_3 = "\nWanna over-right to {} or to save with different name(Y/N): "
save = str(input(str_3.format(location)))
if save == "Y":
    csv_2 = df_2.to_csv(location, sep, index=False)
elif save == "N":
    location_2 = str(input("Give new location to save updated CSV: "))
    sep_2 = str(input("Provide separator="))
    csv_2 = df_2.to_csv(location_2, sep_2, index=False)
else:
    print("Invalid Input!!")

print("Saved...ThankYou")

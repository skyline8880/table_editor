def phone_corrector(dataframe, *args):
    progressbar, phone_column = args
    progressbar.setValue(dataframe.name)
    dataframe[phone_column] = "".join(str(dataframe[phone_column]).strip())
    for symbol in dataframe[phone_column]:
        try:
            int(symbol)
        except Exception:
            dataframe[phone_column] = dataframe[phone_column].replace(
                symbol, ""
            )
    if len(dataframe[phone_column]) == 11:
        if 900 <= int(dataframe[phone_column][1:4]) <= 999:
            if dataframe[phone_column][0] != "7":
                dataframe[phone_column] = f"7{dataframe[phone_column][1:]}"
            return dataframe[phone_column]
    if len(dataframe[phone_column]) == 10:
        if 900 <= int(dataframe[phone_column][0:3]) <= 999:
            dataframe[phone_column] = f"7{dataframe[phone_column]}"
            return dataframe[phone_column]
    return


def empty_duplicates(dataframe, *args):
    progressbar, phone_column, secondary_list = args
    progressbar.setValue(dataframe.name)
    if dataframe[phone_column] in secondary_list:
        return
    return dataframe[phone_column]


def fullname_duplicates(dataframe, *args):
    progressbar, junior_column, second_list = args
    if isinstance(dataframe[junior_column], float):
        return
    lgth = len(dataframe[junior_column].split(" "))
    if (
        "".join(dataframe[junior_column].lower().strip().split(" "))
        in ["".join(
            sec_per.lower().strip().split(" ")[:lgth]
            ) for sec_per in second_list]):
        progressbar.setValue(dataframe.name)
        return dataframe[junior_column]
    return

import matplotlib.pyplot as plt

def move_column(dataframe, col_name, new_index):
    col_to_move = dataframe.pop(col_name)

    dataframe.insert(new_index, col_name, col_to_move)
    dataframe.head()

def subtract_1(val):
    # if(val is not int):
    #     return error message
    return val - 1

def correct_GAD_scores(df):
    if((df == 0).any().any()): # presence of any 0 indicates data has been corrected
        return 
    else:
        return df.apply(subtract_1)

def df_to_table(input_dataframe, output_table_name, conn):
    input_dataframe.to_sql(output_table_name, conn, index=False, if_exists='replace')

def add_custom_id_column(dataframe, new_col_name, first_id_no):
    if new_col_name in dataframe:
        return
    else:
        dataframe.insert(
            0,
            new_col_name,
            range(first_id_no, first_id_no + len(dataframe))
        )

        col_to_move = dataframe.pop(new_col_name)
        dataframe.insert(0, new_col_name, col_to_move)

# ChatGPT helped redesign this function to no longer rely on another column as a reference

def visualize_count_plot(dataframe, x_label_name, y_label_name, plot_name):
    plt.bar(dataframe.index, dataframe.values)

    plt.xlabel(x_label_name)
    plt.ylabel(y_label_name)
    plt.title(plot_name)

    plt.show()

def visualize_and_label_count_plot(dataframe, x_label_name, y_label_name, plot_name, label_lookup):
    positions = range(len(dataframe))

    plt.bar(positions, dataframe.values)

    plt.xticks(
        positions,
        [label_lookup[i] for i in dataframe.index],
        rotation=45,
        ha='right'
    )

    plt.xlabel(x_label_name)
    plt.ylabel(y_label_name)
    plt.title(plot_name)

    plt.show()
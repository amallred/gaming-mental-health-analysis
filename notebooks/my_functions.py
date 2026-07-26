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
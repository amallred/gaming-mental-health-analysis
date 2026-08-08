import matplotlib.pyplot as plt
import seaborn as sns

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

# =========
# Final analysis functions
# =========

# Global Variables

colors_ld=['#92c5de','#4393c3', '#2166ac', '#5e3c99', '#2d1e2f', '#0f0a14']
colors_dl=['#0f0a14', '#2d1e2f', '#5e3c99', '#2166ac', '#4393c3', '#92c5de']

# Functions

def remove_top_right_borders(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def annotate_plot (data_source_name, x_coord, y_coord):
    plt.annotate(
    f'Data Source(s): {data_source_name}', 
    (x_coord,0), 
    (0,y_coord), 
    fontsize=8, 
    xycoords='axes fraction', 
    textcoords='offset points', 
    va='top',
    fontstyle='italic'
    )


def display_GAD_countplot(dataframe, avg_label_y_align, plot_title, data_source_name, x_coord, y_coord, file_name):

    average_GAD = dataframe['GAD_total'].mean().round(1)

    plt.figure(figsize=(10,6))

    # This tells the palette how the categories should be colored
    palette_list = {
        'None/Minimal': colors_ld[0],
        'Mild': colors_ld[1],
        'Moderate': colors_ld[2],
        'Severe': colors_ld[3]
    }

    ax = sns.countplot(
        x='GAD_total', 
        data = dataframe,
        hue = 'cat_name', 
            # hue tells the palette what column to use to know 
            # what category to use from the palette_list
        dodge=False,
        gap=-.25,
        palette = palette_list,
        edgecolor=colors_ld[-1]
    )

    remove_top_right_borders(ax)

    # Add average line
    ax.axvline(
        average_GAD,
        color="red",
        linewidth = 1,
        alpha = .7
    )

    ax.text(
        average_GAD+0.25,
        avg_label_y_align,
        f"Avearage\nScore",
        color="red",
        fontsize=10
    )

    # Cite sources
    annotate_plot(data_source_name, x_coord, y_coord)

    # Customize xticks
    plt.xticks([0, 10, 20], [0, 10, 20])

    plt.legend(
        title='Anxiety Level', 
        loc='center right'
        )

    plt.title(plot_title, fontsize=18, pad=20)
    plt.xlabel("Generalized Anxiety Disorder-7 (GAD-7) Assessment Score", fontsize=12)
    plt.ylabel("Number of Survey Participants", fontsize=12)

    plt.tight_layout()

    # Save figure as image
    plt.savefig(f'../plots/{file_name}.png')

    plt.show()

    # References: 
    #   1- https://stackoverflow.com/questions/59695334/custom-color-palette-in-seaborn
    #   2- I got very close, but needed help understanding how 'hue', 'dodge', and 'gap'worked: ChatGPT helped
    #   3- https://www.geeksforgeeks.org/python/how-to-adjust-number-of-ticks-in-seaborn-plots/ 
    #   4- https://stackoverflow.com/questions/41046214/cite-a-data-source-in-matplotlib 


def get_GAD_cat_percentages_query(survey_id):
    return f"""
    SELECT
        g.GAD_cat,
        c.cat_name,
        COUNT(*) AS sum_participants,
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS percentage
    FROM gad_data_usa_18_22 g
    JOIN GAD_category c on c.GAD_cat = g.GAD_cat
    WHERE survey_id = {survey_id}
    GROUP BY g.GAD_cat
    ORDER BY g.GAD_cat
    """

def display_GAD_pie_chart (series_name, plot_name, data_source_name, x_coord, y_coord, file_name):
    fig, ax = plt.subplots(figsize=(8,8))

    ax.pie(
        series_name,
        colors = colors_ld,
        # labels=series_name.index,
        autopct='%1.1f%%',
        textprops={'fontsize': 16,
                    'weight' : 'bold'}
        )

    ax.set_title(plot_name, fontsize=18)

    ax.legend(
        labels = series_name.index,
        loc="lower right",
        title = "Anxiety Level"
    )

    # Cite sources
    annotate_plot(data_source_name, x_coord, y_coord)

    # Save figure as image
    plt.savefig(f'../plots/{file_name}.png')

    plt.tight_layout()
    plt.show()

    # Reference(s):
    #   https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

def label_line(ax, x_coord, y_coord, label, color_name):
    ax.text(
        x_coord,
        y_coord,
        f"{label}",
        color=color_name,
        fontsize=10,
        ha='right'
    )
<center>

![gaming-mental-health-analysis](/images/Gaming_&_Mental_Health_Analysis.png)

<strong>An investigation into the impact of gaming on anxiety.</strong>

<br>

![GitHub top language](https://img.shields.io/github/languages/top/amallred/gaming-mental-health-analysis?logoColor=f37821&labelColor=0f0a14&color=%23f37821)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/amallred/gaming-mental-health-analysis?labelColor=%230f0a14)</center>



## Installation

1. Clone the repo
      ```bash
      git clone https://github.com/amallred/gaming-mental-health-analysis
      ```
2. Create and activate virtual environment
      ```bash
      # Windows
      python -m venv venv
      venv/Scripts/activate

      # Max / Linux
      python3 -m venv venv
      source venv/bin/activate
      ```
3. Install required packages
      ```bash
      pip install -r requirements.txt
      ```

## Usage  

Run the notebooks in the following order:
1. gaming_mental_health_cleaning.ipynb
2. nhis_mental_health_cleaning.ipynb
3. gad_eda.ipynb
4. final_analysis.ipynb


## Analysis

### Preliminary Analysis:
In my preliminary investigation of the gaming data, I explored what factors appear to most correlate with higher anxiety levels in this survey's participants (Ex: demographics like age/gender/country, hours spent gaming, gaming platform, etc.).

By answering these questions, potential outcomes include:
- Data could be presented to gaming corporations to encourage better mental health reminders (like in [Satisfactory](https://www.satisfactorygame.com/))
- To improve customer's mental health (and potentially increase the longevity of revenue) games could be marketed to match the purpose most associated with better mental health indicators.

### Overall Analysis and Observations:
I compared the data representing the mental health of gamers with a CDC survey of the general population that used the same psychological test, the General Anxiety Disorder-7 questionnaire. I narrowed the participants for this analysis to be located in the USA and between the ages of 18-22 to account for the most participants from each survey. Using the database created from these datasets, I explored the following questions:

#### How do the total GAD-7 scores compare between gamers and the general population?
    Overall, Gamers exhibited a higher GAD-7 score than the General Population, though the average score fell just beyond the "Mild Anxiety" threshold. This is higher, but not as significantly different as I expected to see. 
|  |  |
| --- | --- |
|![average gamers exhibit mild anxiety levels](/plots/gamer_gad_countplot.png) | ![General Population Demonstrates Low Anxiety Levels](/plots/nhis_gad_countplot.png) |

#### How did the GAD-7 categorizations compare between gamers and the general population?
    While the average GAD-7 score was just over the "Mild Anxiety" threshold for Gamers, there was a greater representation of individuals with levels higher than "Mild" in that group than in the general population.
|  |  |
| --- | --- |
|![anxiety levels among gamers](/plots/gamer_gad_pie.png) | ![anxiety levels in the general population are minimal](/plots/nhis_gad_pie.png) |

#### Did hours spent gaming impact participant's GAD-7 score?
    Weekly gaming hours showed little correlation with individual's anxiety levels.
![anxiety levels vary greatly across weekly gaming hours](/plots/gamer_gad_scatter.png)

#### How did gaming platform impact participants' anxiety levels?
Mobile gamers showed significantly higher anxiety levels than gamers on other platforms.
![mobile gamers exhibit higher anxiety levels](/plots/gamer_gad_boxplot.png)

### Takeaways
The data showed that there was a noticeable difference in gamers' mental health, with averages exceeding the levels of the general population. In this subset, individuals who gamed primarily on mobile devices exhibited much higher anxiety levels. Learning this leads me to question if there should be stricter guidelines on time limits or reminders for self-care in mobile applications. 


## Acknowledgements
I would like to thank the team at Code:You for their support on this project. Thank you, also, to Kevin Le for a very helpful one-on-one session to help me through blockers and reviewing my project.

## Author
Amanda Allred | [LinkedIn](https://www.linkedin.com/in/amallred/) | [Email](amallredmom@gmail.com)

## Resources
- [Online Gaming Anxiety Dataset](https://www.kaggle.com/datasets/divyansh22/online-gaming-anxiety-data/discussion/294172)
- [pdf of survey for data](https://osf.io/vnbxk/files/vyr5f)
- [GAD survey questions and scoring information](https://www.mdcalc.com/calc/1727/gad7-general-anxiety-disorder7)
- [SWL information](https://labs.psychology.illinois.edu/~ediener/SWLS.html)
- [SPIN survey questions](https://psychology-tools.com/test/spin)
- Other graphic-specific references are included in comments throughout the code.

### Other potential datasets to include in future analysis:
- **Look into non-gaming related GAD, SWL, SPIN tests**
- [Digital Habits & Smartphone Addiction Dataset](https://www.kaggle.com/datasets/guriya79/smart-phone)
  - Well maintained and clean data but no demographic information beyond age and gender
- [The Impact of Online Gaming on Various Social Constructs](https://osf.io/c9utj/overview)
- [Can playing Dungeons and Dragons be good for you?....](https://osf.io/3pgt7/overview)
  - (Only 18-20 participants total, though)
- [2018 A weak scientific basis for gaming disorder: Let us err on the side of caution](https://osf.io/m3wyb/overview)

#### AI Usage Notes
- I used ChatGPT to explain why I needed to change the encoding of my gaming data file to `read_csv` and used its suggestions to inform further investigation online before deciding that encoding to latin-1 was the best option for this data.
  - What I learned: Sometimes special characters work in one encoding (latin-1) and not in another (UTF-8 for example) can throw the error I was encountering (UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 599: invalid start byte). In this case, the '0xA0' character represents a non-breaking space character. Also, the encoding labels ISO-8859-1 == Latin-1. 
- I used ChatGPT to help with the logic of pulling data from only the top 5 represented countries.
- Other AI references are noted in the comments throughout the code. These were intentionally kept to a minimum and most concepts were repeated in multiple cells.
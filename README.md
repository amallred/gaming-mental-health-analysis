<center>

![gaming-mental-health-analysis](/images/Gaming_&_Mental_Health_Analysis.png)

<strong>An investigation into what factors most strongly impact gamers' anxiety levels.</strong>

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
      env/Scripts/activate

      # Max / Linux
      python3 -m venv venv
      source env/bin/activate
      ```
3. Install required packages
      ```bash
      pip install -r requirements.txt
      ```

## Usage *** UPDATE THIS*** 

Run the notebooks in the following order:
1. data_cleaning.ipynb
2. eda.ipynb
3. charts.ipynb

In this investigation, I explored what factors appear to most correlate with higher anxiety levels in this survey's participants (Ex: demographics like age/gender/country, hours spent gaming, gaming platform, etc.).

By answering these questions, potential outcomes include:
- Data could be presented to gaming corporations to encourage better mental health reminders (like in [Satisfactory](https://www.satisfactorygame.com/))
- To improve customer's mental health (and potentially increase the longevity of revenue) games could be marketed to match the purpose most associated with better mental health indicators.

## Author
Amanda Allred | [LinkedIn](https://www.linkedin.com/in/amallred/) | [Email](amallredmom@gmail.com)

## Resources
- [Online Gaming Anxiety Dataset](https://www.kaggle.com/datasets/divyansh22/online-gaming-anxiety-data/discussion/294172)
- [pdf of survey for data](https://osf.io/vnbxk/files/vyr5f)
- [GAD survey questions and scoring information](https://www.mdcalc.com/calc/1727/gad7-general-anxiety-disorder7)
- [SWL information](https://labs.psychology.illinois.edu/~ediener/SWLS.html)
- [SPIN survey questions](https://psychology-tools.com/test/spin)
- Other graphic-specific references are included in comments throughout the code.

### Other potential datasets to include in the analysis:
- **Look into non-gaming related GAD, SWL, SPIN tests**
- [Digital Habits & Smartphone Addiction Dataset](https://www.kaggle.com/datasets/guriya79/smart-phone)
  - Well maintained and clean data but no demographic information beyond age and gender
- [The Impact of Online Gaming on Various Social Constructs](https://osf.io/c9utj/overview)
- [Can playing Dungeons and Dragons be good for you?....](https://osf.io/3pgt7/overview)
  - (Only 18-20 participants total, though)
- [2018 A weak scientific basis for gaming disorder: Let us err on the side of caution](https://osf.io/m3wyb/overview)

#### AI Usage Notes
- I used ChatGPT to explain why I needed to change the encoding of my file to `read_csv` and used its suggestions to inform further investigation online before deciding that encoding to latin-1 was the best option for this data.
  - What I learned: Sometimes special characters work in one encoding (latin-1) and not in another (UTF-8 for example) can throw the error I was encountering (UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 599: invalid start byte). In this case, the '0xA0' character represents a non-breaking space character. Also, the encoding labels ISO-8859-1 == Latin-1. 
- I used ChatGPT to help with the logic of pulling data from only the top 5 represented countries.
- Other AI references are noted in the comments throughout the code. These were intentionally kept to a minimal number and most concepts were repeated in multiple graphs.
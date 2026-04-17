# gaming-mental-health-analysis

## Overview
This analysis aims to adress these questions:
- How do demographics (age/gender/country) impact hours played/anxiety levels?
- What games / platforms lead to higher anxiety levels?
- How does the reason the players play the games compare with their anxiety?

By answering these questions, potential outcomes include:
- Data could be presented to gaming corporations to encourage better mental health reminders (like in [Satisfactory](https://www.satisfactorygame.com/))
- To improve customer's mental health (and potentially increase the longevity of revenue) games could be marketed to match the purpose most associated with better mental health indicators.

## Resources
- [Online Gaming Anxiety Dataset](https://www.kaggle.com/datasets/divyansh22/online-gaming-anxiety-data/discussion/294172)
- [pdf of survey for data](https://osf.io/vnbxk/files/vyr5f)
- [GAD survey questions](https://patient.info/doctor/mental-health/gad-7)
- [SWL information](https://labs.psychology.illinois.edu/~ediener/SWLS.html)
- [SPIN survey questions](https://psychology-tools.com/test/spin)


### Other potential datasets to include in the analysis:
- [Digital Habits & Smartphone Addiction Dataset](https://www.kaggle.com/datasets/guriya79/smart-phone)
  - Well maintained and clean data but no demographic information beyond age and gender
- [The Impact of Online Gaming on Various Social Constructs](https://osf.io/c9utj/overview)
- [Can playing Dungeons and Dragons be good for you?....](https://osf.io/3pgt7/overview)
  - (Only 18-20 participants total, though)
- [2018 A weak scientific basis for gaming disorder: Let us err on the side of caution](https://osf.io/m3wyb/overview)

#### AI Usage Notes
- I used ChatGPT to explain why I needed to change the encoding of my file to `read_csv` and used its suggestions to inform further investigation online before deciding that encoding to latin-1 was the best option for this data.
  - What I learned: Sometimes special characters work in one encoding (latin-1) and not in another (UTF-8 for example) can throw the error I was encountering (UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 599: invalid start byte). In this case, the '0xA0' character represents a non-breaking space character. Also, the encoding labels ISO-8859-1 == Latin-1.
| Table | Issue Description | Resolvable? | Done | Notes |
| ----- | ----------------- | ----------- | ---- | ----- | 
| Gaming Study Data | Index and S. No. columns are similar | yes | ... | ... |
| Gaming Study Data | Column names unclear and inconsistent | yes | ... | ... |
| Gaming Study Data | Timestamp in odd format and datatype | yes | ... | ... |
| Gaming Study Data | 'earnings', 'why play', 'League', 'Playstyle' columns are open-ended | ... | ... | ... |
| Gaming Study Data | SPIN questions not available in survey pdf | ... | ... | ... |
| Gaming Study Data | Residence and Birthplace repeated with _ISO3. Check for duplicate data and formatting | yes | ... | Use ISO3 columns for consistent format |
| Gaming Study Data | Remove original residence & birthplace columns | yes | ... | ... |
| Gaming Study Data | Platform content - remove excess from 'Console' | yes | ... | ... |
| Gaming Study Data | GADE_Difficulty_in_life transform to int to match other data  | yes | ... | ... |
| Gaming Study Data | Hours to int from float | yes | ... | ... |
| Gaming Study Data | SPIN float to int | yes | ... | ... |
| Gaming Study Data | Highest league column can be removed; all NaN | yes | yes | ... |
| Gaming Study Data | Streams column name is misleading; rename | yes | yes | ... |
| Gaming Study Data | SPIN_Total to int | yes | ... | ... |
| Gaming Study Data | ... | ... | ... | ... |
| Gaming Study Data | ... | ... | ... | ... |
| Gaming Study Data | ... | ... | ... | ... |

-------------

### Renaming
- Would it be better to set the row index starting at 1 and use S. No?
- GAD (General Anxiety Disorder) 
{
'GAD1_Feeling_nervous' : 'Feeling nervous, anxious, or on edge'
'GAD2_Cant_stop_worrying' : 'Not being able to stop or control worrying'
'GAD3_Worrying_too_much' : 'Worrying too much about different things'
'GAD4_Trouble_relaxing' : 'Trouble relaxing'
'GAD5_Restless' : 'Being so restless that it's hard to sit still'
'GAD6_Easily_annoyed' : 'Becoming easily annoyed or irritable'
'GAD7_Feeling_afraid' : 'Feeling afraid as if something awful might happen'
'GADE_Difficulty_in_life' : 'If you checked off any problems, how difficult have these made it for you to do your work, take care of things at home, or get along with other people?'
}

- Reassignment dictionary
{'GAD1' : 'GAD1_Feeling_nervous',
'GAD2' : 'GAD2_Cant_stop_worrying',
'GAD3' : 'GAD3_Worrying_too_much',
'GAD4' : 'GAD4_Trouble_relaxing',
'GAD5' : 'GAD5_Restless',
'GAD6' : 'GAD6_Easily_annoyed',
'GAD7' : 'GAD7_Feeling_afraid',
'GADE' : 'GADE_Difficulty_in_life',
'SWL1' : 'SWL1_Ideal_life',
'SWL2' : 'SWL2_Excellent_conditions',
'SWL3' : 'SWL3_Satisfied_with_life',
'SWL4' : 'SWL4_Got_important_things',
'SWL5' : 'SWL5_Change_nothing',
'earnings' : 'Earnings',
'whyplay' : 'Why_play',
'highestleague' : 'Highest_league',
'streams' : 'Streams',
'SPIN1' : 'SPIN1_Fear_authority',
'SPIN2' : 'SPIN2_Distress_blushing',
'SPIN3' : 'SPIN3_Fear_social_events',
'SPIN4' : 'SPIN4_Avoid_strangers',
'SPIN5' : 'SPIN5_Fear_criticism',
'SPIN6' : 'SPIN6_Avoid_embarrassment',
'SPIN7' : 'SPIN7_Distress_sweating',
'SPIN8' : 'SPIN8_Avoid_parties',
'SPIN9' : 'SPIN9_Avoid_attention',
'SPIN10' : 'SPIN10_Fear_talking_strangers',
'SPIN11' : 'SPIN11_Avoid_giving_speeches',
'SPIN12' : 'SPIN12_Avoid_criticism',
'SPIN13' : 'SPIN13_Distress_heart',
'SPIN14' : 'SPIN14_Fear_observation',
'SPIN15' : 'SPIN15_Fear_embarrassment',
'SPIN16' : 'SPIN16_Avoid_authority',
'SPIN17' : 'SPIN17_Distress_trembling',
'accept' : 'Accept',
'Playstyle' : 'Play_style',
'GAD_T' : 'GAD_Total',
'SWL_T' : 'SWL_Total',
'SPIN_T' : 'SPIN_Total'
}

- SWL (Satisfaction With Life)
{'SWL1_Ideal_life' : 'In most ways my life is close to my ideal.',
'SWL2_Excellent_conditions' : 'The conditions of my life are excellent.',
'SWL3_Satisfied_with_life' : 'I am satisfied with life.',
'SWL4_Met_wants' : 'So far I have gotten the important things I want in life.',
'SWL5_Change_nothing : 'If I could live my life over, I would change almost nothing.'
}

- SPIN (Social Phobia Inventory)
{
'SPIN1_Fear_authority' : 'I am afraid of people in authority.',
'SPIN2_Distress_blushing' : 'I am bothered by blushing in front of people.',
'SPIN3_Fear_social_events' : 'Parties and social events scare me.',
'SPIN4_Avoid_strangers' : 'I avoid talking to people I don’t know.',
'SPIN5_Fear_criticism' : 'Being criticized scares me a lot.',
'SPIN6_Avoid_embarrassment' : 'I avoid doing things or speaking to people for fear of embarrassment.',
'SPIN7_Distress_sweating' : 'Sweating in front of people causes me distress.',
'SPIN8_Avoid_parties' : 'I avoid going to parties.',
'SPIN9_Avoid_attention' : 'I avoid activities in which I am the center of attention.',
'SPIN10_Fear_talking_strangers' : 'Talking to strangers scares me.',
'SPIN11_Avoid_giving_speeches' :  'I avoid having to give speeches.',
'SPIN12_Avoid_criticism' : 'I would do anything to avoid being criticized.',
'SPIN13_Distress_heart' : 'Heart palpitations bother me when I am around people.',
'SPIN14_Fear_observation' : 'I am afraid of doing things when people might be watching.',
'SPIN15_Fear_embarrassment' : 'Being embarrassed or looking stupid are among my worst fears.',
'SPIN16_Avoid_authority' : 'I avoid speaking to anyone in authority.',
'SPIN17_Distress_trembling' : 'Trembling or shaking in front of others is distressing to me.'
}
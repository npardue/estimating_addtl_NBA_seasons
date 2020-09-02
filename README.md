
# Creating a regression model that predicts the amount of seasons an NBA player can be expected to play

##### - Nick Pardue, nickpardue@gmail.com

### [Presentation]

![logo_background.jpeg](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/logo_background.jpg)

### Context
For any given season, the NBA typically has around 450 individual players. That's 15 players for each of the 30 teams. Of those 15 players, only two or three per team are normally considered to be "Star Players." That means that, the other 12-13 players per team (or ~83% of all players) fall somewhere in the category of what are known as "Role Players." These are players that.. you guessed it! Fill a role in the team's needs by providing a particular skill-set. The skill-sets vary greatly, but can be things such as being a solid defensive player, someone who can provide points off the bench while your starters rest, or someone who can be trusted not to turn the ball over while facilitating the offense. Role players can be starters; however, the majority of them come off of the bench. 

What I would like to do is create a way of predicting how many more seasons a player can be expected to play for the purpose of increasing a player's leverage in contract negotiations. Not including Supermax contracts, as those don't apply to our Role Players, contracts are generally anywhere from one to four years long, whereas the average career length is only 4.5 years. Typically, Role Players end up signing contracts that fall in the 1-2 year range. This is a product of NBA teams looking ahead at what big name players are going to become free agents in the coming years, and then signing Role Players to shorter contracts in an effort to increase their financial flexibility for the summers said big name players go on the market. What this means for Role Players is that they have less financial security, and their families have to live in a reality of knowing that they may have to move to a new city every year, or every other year. 

### Goal
Create a model that can accurately predict the amount of additional seasons a player in the NBA can be expected to play, in an effort to help Role Players increase their financial security through negotiating longer contracts. 


### Data Sets
Sourced Data
- [Basketball Reference]: Player Production Stats for the [Raw Data]
- [Kaggle]: Draft Year, Height & Weight for the [Clean Draft, Height & Weight Data]

[Cleaned Data] 


### Cleaned Data Description
I analyzed a dataset of over 6k NBA player entries from the 1996-97 to 2018-19 seasons. Each entry contained 147 variables that fell into the following categories, with more detailed descriptions found in the [Glossary]:
 - Age
 - Mileage Stats from Reg. Season and Playoffs
    - Games Played, Minutes Played.
 - Production Stats from Reg. Season and Playoffs
    - Points per Game, Field Goals Attempted, Field Goal %, Assists, Steals, Turnovers, etc.
 - Advanced Stats from Reg. Season and Playoffs
     - Player Efficiency Rating, Win Shares, Value over Replacement Player, Usage %, % of Team's Production Stats, etc.
 - Measurements
     - Height and Weight. 

 

### Exploratory Analysis

 ##### Figure 1: What's the average number of seasons left for NBA players in our data?
 - As expected, the average career length of our limited dataset (4.16 years) falls close to the overall average (4.5 years). Also, it's interesting to see how many fewer players manage to play 10 or more seasons, and just how many more players careers are shorter than or at the average length. 
 
![dist-seasons-left.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/dist-seasons-left.png)

 ##### Figure 2: What is the average player's size each season?
 - These visuals speak to the trends that have been observed in the NBA over the past 20 years. Both show a spike shortly after the 1999-00 season in response to the dominance of big men like David Robinson and Tim Duncan on the Spurs in '99, and Shaq on the early-2000's Lakers. These spikes are followed up by drops in value in the mid-2000's as players like Dwyane Wade and Manu Ginóbili rose to prominence, while battling more defensive teams such as the Pistons and Spurs. Reaching 2010, the averages shot up again momentarily, likely to try counteracting the '08 Celtics, and '08-10 Lakers. Finally, the averages begin to drop off indicating the change in playstyle towards "small ball," started by the Heat and Spurs, and perfected by the Warriors.
 
![ht_by_season.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/ht_by_season.png)
![wt_by_season.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/wt_by_season.png)


 ##### Figure 3: What is the average player's age each season?
- The average age of players per season appears to have been on a constant decline since around 2000. It doesn't come as too much of a surprise as players are being asked to be able to do more things for their teams, and younger, more athletic players, tend to be able to fit into that mold. 
 
![age_by_season.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/age_by_season.png)



### Modeling

 ##### Figure 1: Running Multiple Models on Training Data
 - I split the original data set into a training and a test set (80:20), and then ran several vanilla models on the training set in an effort to pick out a few models that worked best for hypertuning. The vanilla models I chose to run were a KNN Regressor (KNN), Decision Tree (DT), Random Forest Regressor (RF), Extra Trees Regressor (ET), AdaBoost Regressor (ADA), and a Naive Bayes Gaussian model. The results are displayed in an order of Model -> R<sup>2</sup> for assessing over/underfitting -> RMSE for assessing prediction accuracy. 
 
 ![van_model_results.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/van_model_results.png)
 
 - From these results, I chose to further investigate the KNN, RF, and ADA models through parameter grid hypertuning, settling on the RF as my final model.
 
 ##### Figure 2: Tuned Random Forest Results
 - Hypertuning helped reduce the RF models' original issue of overfitting to the training data, producing an R<sup>2</sup> = 0.70, and an RMSE of 2.03 years; however, I was unable to address the test set overfitting to an R<sup>2</sup> = 1.0, and an RMSE of 2.5 years. Shown below are the results for the test set predictions.
 
 ![test_act_v_pred.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/test_act_v_pred.png)
 
 ##### Figure 3: Prominent Features 
 - After seeing how badly overfit the model was to the test data, I wanted to look into which features were important. Upon looking at the values for each of the 147 features, it looks like I flooded the model with far too many redundant features. On the bright side, this means that I have a solid list of features to cut out from the next iteration of my model. Shown below are the top 20 features in order of importance in predicting additional seasons a player may have. Predictably, many are related to a player's age (Age, season, current_year & draft_year), minutes and games played, percentage of a team's shots taken, and stats relating to a player's offensive and defensive win shares.
 
 ![top_features.png](https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/top_features.png)




### Limitations
- I was unable to include players who went undrafted into the modeling process, as the dataset I used for draft years did not list the year they played their first games.
- Time constraints got in the way of my learning and implementing a web scraping technique that would've provided the first season of undrafted players, and the height and weight values for players prior to the 1996-97 season.

### Future Improvements
- Implement undrafted players into the model.
- Include data from before the 1996-97 season.
- Create a feature of player-type through clustering, and feed that into the model.


### Reproducing Our Results
Download the [Cleaned Data], and then follow along with the [Executive Notebook] to produce a copy of the results.

### Repo Navigation
```
├── data
│   ├── clean (child folders contain cleaned .csv files from the years 1989-2019, pertaining to child-name-related stats)
│   │   ├── draft (draft, height & weight info)
│   │   ├── play-36
│   │   ├── play-advanced
│   │   ├── reg-36
│   │   ├── reg-advanced
│   │   ├── regseason
│   │   └── glossary.txt
│   ├── combined
│   │   └── many .csv files of combined regular season and playoff data
│   ├── final
│   │   └── final_df.csv
│   ├── raw (child folders contain raw .csv files from the years 1989-2019, pertaining to child-name-related stats)
│   │   ├── draft (draft, height & weight info)
│   │   ├── play-36
│   │   ├── play-advanced
│   │   ├── reg-36
│   │   ├── reg-advanced
│   │   ├── regseason
│   │   └── .DS_Store
│   ├── .DS_Store
│   ├── cleaning_script.py
│   └── glossary.txt
│
├── images
│   ├── .DS_Store
│   ├── Many Images in Alphabetical Order
│   ├── sources.txt (sources of images)
│   └── More Images in Alphabetical Order
│
├── Cleaning_082620.ipynb
│
├── EDA_082620.ipynb
│
├── Executive Notebook.ipynb
│
├── ModelingMoreFeats_082920.ipynb
│
├── NBA Career Length.pdf (presentation)
│
├── README.md
│
└── nohup.out

```

### Sources of Images Used in Presentation
Sources can be found [here].



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
  
   [presentation]: <https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/NBA%20Career%20Length.pdf>
   [basketball reference]: <https://www.basketball-reference.com/>
   [clean draft, height & weight data]: <https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/data/clean/draft/all_seasons.csv>
   [kaggle]: <https://www.kaggle.com/justinas/nba-height-and-weight-analysis/notebook?select=all_seasons.csv>
   [cleaned data]: <https://github.com/npardue/estimating_addtl_NBA_seasons/tree/master/data/final>
   [raw data]: <https://github.com/npardue/estimating_addtl_NBA_seasons/tree/master/data/raw>
   [glossary]: <https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/data/glossary.txt>
   [executive notebook]: <https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/Executive%20Notebook.ipynb>
   [here]: <https://github.com/npardue/estimating_addtl_NBA_seasons/blob/master/images/sources.txt>


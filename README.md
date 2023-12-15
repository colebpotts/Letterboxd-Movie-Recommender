# Movie Reccomender System
## Capstone - Sprint 2

Author: Cole Beevor-Potts
Date: December 15th 2023

# My project: a movie reccomender system 

## The Problem
I love to watch good movies, and a great movie makes me feel full of contentment by the end. However, it takes time and effort to determine what to watch, especially when we start to consider how much time you have to watch, what kind of movie I am looking for, and so on. The absolute last thing you want when you have spent 30 minutes hunting for movie, finally pick one, sit down and devote 2 hours of your precious time watching it just to rate it 2 stars and go to bed.

I want to build a product that adds values immediately, allowing users to better identify movies that are aligned with what they are looking for.

## The Opportunity
My product will offer the ability for users to connect their letterboxd account and get movie suggestions based on their existing movie ratings. They can determine which genre, director, actor, or length of film they want to see. Or they can choose to see something completely new! The goal is to create a movie curation experience that is personal, efficient, and effective.
I am choosing to work off of letterboxd because I feel it is already the most personalized movie rating platform, and that my product would amplify this benefit. 

## The Impact
This product will save users time in discovering new movies more efficiently, while also getting more effective suggestions so that at the end of the night, they are watching a movie they enjoy!

**Main Goal** We have a average rating score of 6.35 within our dataset (For movies with more than 150 reviews), the goal is to get someone watching a movie that they would rate significatnyl higher than that.

- **Time Savings**: If I can save the average person 30 minutes of time a week by making their decision making process easier, and cut that time down to 5 minutes, then with thousands of users , this tool could collectively save thousands of hours.
- **Improved User Experience:** By offering personalized and efficient movie recommendations, this project could enhance the user experience of thousands of movie enthusiasts. Users will find a higher success rate of doing what they set out for in the first place: enjoying film!
- **Discovery of New Films:** This project can introduce users to a broader range of movies, broadening their horizons and promoting diversity in their movie-watching habits.

# My Data How Data Science Will Provide this
I will be using a dataset scraped from Letterboxd that is available on Kaggle by Sam Learner. Find the dataset here: https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data

It is comprised of 3 tables: Movies, Ratings, and Users. Between these 3 tables I will build a ML model that will identify trends and correlations between the movies users' like. I will use this to build my reccomender system. The data is robust with 3 files, 28 total columns, and the rating table having over 11 million unique reviews to pull from. 

I will add the personalized suggestion by feeding the reccomender with the users rating data that I will build an HTML scraped to get. I will then feed this data to the model to predict which movie the user would rate the highest, thus making a high quality reccomendation. 

So far we have:
* Conducted EDA and merged our ratings and movies tables
* Vectorized movie overview
* Created binary variables for all other categorical variables including genre
* Conducted a nearest neighbour analysis to find the similar movies
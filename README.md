# Letterboxd Movie Recommender System

Author: Cole Beevor-Potts
Date: January 8th 2024

## The Problem
I love to watch good movies, and a great movie makes me feel full of contentment by the end. However, it takes time and effort to determine what to watch and the absolute last thing you want when you have spent 30 minutes hunting for movie, finally pick one, sit down and devote 2 hours of your precious time watching it just to rate it 2 stars and go to bed.

I want to build a product that adds values immediately, allowing users to better identify movies that are aligned with what they are looking for by:

* Finding movies that are very similar to what they are looking for
* And, predicting which movie they will rate they higher and therfor enjoy the most!

## The Opportunity
The goal is to create a movie curation experience that is personal, efficient, and effective. My product will offer the ability for users to provide a movie and have the similar movies reccomended back to them, and predict the ratings for their movie!


I am wworking off of letterboxd data because I feel it is already the most personalized movie rating platform, and that my product would amplify this benefit. 

## The Impact
The average Netflix user spends about 18 minutes to determine what they want to watch. If we spent 18 minutes picking a show every day, that means we spend 106 hours or over 4.5 days wasting our time!

This product will save users time in discovering new movies more efficiently, while also getting more effective suggestions. The goal of my reccomender system is to make your movie watching decision: 
* Easier
* Faster
* More enjoyable!

**Main Goal** We have a average rating score of 6.35 within our dataset (For movies with more than 150 reviews), the goal is to get someone watching a movie that they would rate higher than that.

- **Time Savings**: If I can save the average person 30 minutes of time a week by making their decision making process easier, and cut that time down to 5 minutes, then with thousands of users , this tool could collectively save thousands of hours.
- **Improved User Experience:** By offering personalized and efficient movie recommendations, this project could enhance the user experience of thousands of movie enthusiasts. Users will find a higher success rate of doing what they set out for in the first place: enjoying film!
- **Discovery of New Films:** This project can introduce users to a broader range of movies, broadening their horizons and promoting diversity in their movie-watching habits.

# My Data
I will be using a dataset scraped from Letterboxd that is available on Kaggle by Sam Learner. Find the dataset here: https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data

It is comprised of 3 tables: Movies, Ratings, and Users. I will use this to build my reccomender system. The data is robust with 3 files, 28 total columns, and the rating table having over 11 million unique reviews to pull from. 

I will use the Movie tables containing 260,000 movies and 19 features to make my content based reccomendations.

I will use the Ratings table, containing 11 million user reviews, to predict a users ratings based on how they lie in the landscape of other users and their movie rating history. 


So far we have:
* Conducted EDA and merged our ratings and movies tables
* Completed our content based reccomender 
    * Using a BERT trained model to find word embeddings of movie description
* Completed our collaborative filtering to predict users ratings

Next Steps
* Combine models to take in users data, find similar movies based on content, and then reccomend them the movies of those that they would rate the highest!

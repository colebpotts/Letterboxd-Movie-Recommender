# I want to watch a movie...
## Capstone - Sprint 2

Author: Cole Beevor-Potts
Date: Either really late nov 22 night or really early nov 23 morning.....

# My project: a movie reccomender system 

# The Problem Area
## The Problem
I love to watch good movies, and a great movie makes me feel full of contentment by the end. However, it takes time and effort to determine what to watch, especially when we start to consider how much time you have to watch, what kind of movie I am looking for, and so on. The absolute last thing you want when you have spent 30 minutes hunting for movie, finally pick one, sit down and devote 2 hours of your precious time watching it just to rate it 2 stars and go to bed.

I want to build a product that adds values immediately, allowing users to better identify movies that are aligned with what they are looking for.

## The Opportunity
My product will offer the ability for users to connect their letterboxd account and get movie suggestions based on their existing movie ratings. They can determine which genre, director, actor, or length of film they want to see. Or they can choose to see something completely new! The goal is to create a movie curation experience that is personal, efficient, and effective.
I am choosing to work off of letterboxd because I feel it is already the most personalized movie rating platform, and that my product would amplify this benefit. 

## The Impact
This product will save users time in discovering new movies more efficiently, while also getting more effective suggestions so that at the end of the night, they are watching a movie they enjoy!

Anybody who has sat down at the end of their day to relax and throw on a movie has experienced this very un-relaxing stress around the enjoyment of film. I have identified a few key demgraphics that this product would cater to:

1. ***Casual Movie Enthusiasts:***
    - **Who They Are:** These users enjoy watching movies but do not necessarily have an in-depth knowledge of cinema. They might watch movies occasionally for leisure.
    - **How They Benefit:**
        - Time Efficiency: Casual movie enthusiasts can quickly find a movie that suits their current mood and time constraints, in an otherwise overwhelming field of options making movie-watching a more spontaneous and enjoyable activity.
        - Discovery of New Content: Your project introduces them to new and interesting films they might not have encountered otherwise, broadening their movie-watching horizons.
2. ***Working Professionals:***
    - **Who They Are:** These users have busy lives, often with limited free time. They use a movie on a Sunday night as a way to relax and prepare for the week ahead.
    - **How They Benefit:**
        - Time Optimization: This product helps make the most of their movie-watching opportunities. They can quickly find a movie that fits their available time, reducing the time spent on decision-making.
        - Stress Reduction: The recommendation system reduces the stress associated with choosing a movie, users can trust the suggestions and enjoy a relaxing movie night.
3. ***Movie Fanatics:***
    - **Who They Are:** These users have a deep passion for movies, and they may have already seen a significant number of films.
    - **How They Benefit:**
        - Avoiding Repetition: Movie fanatics often struggle to find new movies to watch. This product can help them discover hidden gems, classics they haven't seen, or lesser-known works from their favorite directors.
        - Efficient Exploration: Instead of spending time searching for new movies, they can focus on exploring their preferred genres, directors, actors, or other specific criteria with ease.
4. ***Users Looking for Personalized Recommendations:***
    - **Who They Are:** These users prefer tailored recommendations that align with their unique tastes and preferences. They may be really wanting to watch a western tonight, but haven’t seen one before and don’t know where to start.
    - **How They Benefit:**
        - Customized Suggestions: Your project offers personalized recommendations based on their previous ratings and preferences, resulting in movie choices that better match their individual tastes, even if in newer genres.
        - Increased Satisfaction: Users looking for personalized recommendations are more likely to enjoy the movies they watch, leading to higher satisfaction with their movie-watching experiences.

### Impact Summary: 
In the short term, I hope it makes my own personal movie decision process more efficient and effective. On a larger scale, I believe there are a few key points of societal value:

- **Time Savings**: If I can save the average person 30 minutes of time a week by making their decision making process easier, and cut that time down to 5 minutes, then with thousands of users , this tool could collectively save thousands of hours.
- **Improved User Experience:** By offering personalized and efficient movie recommendations, this project could enhance the user experience of thousands of movie enthusiasts. Users will find a higher success rate of doing what they set out for in the first place: enjoying film!
- **Discovery of New Films:** This project can introduce users to a broader range of movies, broadening their horizons and promoting diversity in their movie-watching habits.

# My Data How Data Science Will Provide this
I will be using a dataset scraped from Letterboxd that is available on Kaggle by Sam Learner. Find the dataset here: https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data

It is comprised of 3 tables: Movies, Ratings, and Users. Between these 3 tables I will build a ML model that will identify trends and correlations between the movies users' like. I will use this to build my reccomender system. The data is robust with 3 files, 28 total columns, and the rating table having over 11 million unique reviews to pull from. 

I will add the personalized suggestion by feeding the reccomender with the users rating data that I will build an HTML scraped to get. I will then feed this data to the model to predict which movie the user would rate the highest, thus making a high quality reccomendation. 
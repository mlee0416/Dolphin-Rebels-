# Restaurant-Analysis
Project 1

- Data Resources: US Census Demographic Data, Yelp API Fusion, Los Angeles County Census Data

- In this project you'll see elements of python to clean data from each data set as well as using python to call Yelp's API to find data in the 
througout the US.  
- With this data, you'll see the correlation between income, ethnicity, restaurant ratings, restaurant price range, etc. 

- Narrative: Have you ever wondered what might contributes to owning a successful restaurant? Most people would assume the quality of the food or the excellent service, but maybe there’s more to it. 

- The goal of our project is to explore the impact of income and ethnicity on the types of the restaurants that are popular in an area. With the help of Yelp’s API, US Census Data, and LA Census Data,  we are able to make a few observations that can be beneficial to restaurant businesses. 

PROCESS
- Census information is based on census tracts. We aggregate census tracts into county level information.
- We filtered census data for American counties with a population size greater than 100,000.
- We excluded Puerto Rico
- We created smaller datasets based on our filter criteria.
  - For example, we created a dataset of counties where the white population is greater than 80% of the population.
- We queried Yelp for the top 50 restaurants as ranked by their rating for each county in the dataset. 
- We pulled restaurant name, ranking, review count, price category and cuisine type.
- We analyzed the data



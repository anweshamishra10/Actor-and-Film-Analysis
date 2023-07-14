import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the data from CSV files into pandas dataframes
actor_data = pd.read_csv(r'C:/Users/ranji/actor_analysis/films_app/data/actor.csv')
film_actor_data = pd.read_csv(r'C:/Users/ranji/actor_analysis/films_app/data/film_actor.csv')
film_category_data = pd.read_csv(r'C:/Users/ranji/actor_analysis/films_app/data/film_category.csv')
category_data = pd.read_csv(r'C:/Users/ranji/actor_analysis/films_app/data/category.csv')

def analyze_actor_films(actor_id):
    # Retrieve actor's name based on actor_id
    actor_row = actor_data[actor_data['actor_id'] == actor_id]
    actor_name = actor_row['first_name'].values[0] + ' ' + actor_row['last_name'].values[0]

    # Filter film_actor table based on actor_id
    actor_films = film_actor_data[film_actor_data['actor_id'] == actor_id]

    # Merge film_actor and film_category tables to get film categories for the actor's films
    actor_films_categories = pd.merge(actor_films, film_category_data, on='film_id')

    # Merge actor_films_categories and category tables to get category names
    actor_films_categories = pd.merge(actor_films_categories, category_data, on='category_id')

    # Group by category and count the number of films
    films_per_category = actor_films_categories.groupby('name')['film_id'].count().reset_index()

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.bar(films_per_category['name'], films_per_category['film_id'])
    plt.xlabel('Film Category')
    plt.ylabel('Total Number of Films')
    plt.title(f'Number of Films per Category for Actor {actor_name}')
    plt.xticks(rotation=90)
    output_path = os.path.join('static', 'result.png')
    plt.savefig(output_path)  # Save the plot as an image

    # Return the actor name and the data as a pandas DataFrame
    return actor_name, films_per_category

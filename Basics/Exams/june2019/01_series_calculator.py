series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_length = float(input())

commercials_time = 0.2 * episode_length
total_episode_length = episode_length + commercials_time
special_episodes_additional_time = number_of_seasons * 10

total_time_needed = total_episode_length * number_of_episodes * number_of_seasons + special_episodes_additional_time

print(f"Total time needed to watch the {series_name} series is {int(total_time_needed)} minutes.")
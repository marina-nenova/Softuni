shooting_time = int(input())
number_of_scenes = int(input())
time_per_scene = int(input())

scene_construction = shooting_time * 0.15
scene_shooting = number_of_scenes * time_per_scene

shooting_time_needed = scene_construction + scene_shooting

difference = abs(shooting_time_needed - shooting_time)
if shooting_time_needed <= shooting_time:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")
# AI-Fitness-trainer
An AI model used to help with the workout session by keeping track of counts and movement using the mediapipe library . Then using the appropriate body part angles , the count of exercise is determined.

## Pull-Up Exercise
![Pull-Up](https://github.com/itzThillaiC/AI-Fitness-trainer/blob/main/output/output%20pull-up.gif?raw=true)

A pull-up is an upper-body strength exercise. The pull-up is a closed-chain movement where the body is suspended by the hands and pulls up.As this happens, the elbows flex and the shoulders adduct and extend to bring the elbows to the torso.

```
python main.py -t pull-up -vs videos/pull-up.mp4
```


## Push-Up Exercise
![Push-Up](https://github.com/itzThillaiC/AI-Fitness-trainer/blob/main/output/output%20push-up.gif?raw=true)


A push-up is a conditioning exercise performed in a prone position by raising and lowering the body with the straightening and bending of the arms while keeping the back straight and supporting the body on the hands and toes.

```
python main.py -t push-up -vs videos/push-up.mp4
```


## Sit-Up Exercise
![Sit-Up](https://github.com/itzThillaiC/AI-Fitness-trainer/blob/main/output/output%20sit-up.gif)


The sit-up is an abdominal endurance training exercise to strengthen, tighten and tone the abdominal muscles. It is similar to a crunch, but sit-ups have a fuller range of motion and condition additional muscles.
```
python main.py -t sit-up -vs videos/sit-up.mp4
```



## Walking Exercise
![Walking](https://github.com/itzThillaiC/AI-Fitness-trainer/blob/main/output/output%20walking%20exercise.gif)


```
python main.py -t walk -vs videos/walk.mp4
```



## Squat Exercise
![Squat](https://github.com/itzThillaiC/AI-Fitness-trainer/blob/main/output/output%20squat.gif)



A squat is a strength exercise in which the trainee lowers their hips from a standing position and then stands back up. During the descent of a squat, the hip and knee joints flex while the ankle joint dorsiflexes.

```
python main.py -t squat -vs videos/squat.mp4
```

For dynamically detecting your realtime movements using your webcam , use these commands below:
```
python main.py -t sit-up
# or python main.py -t pull-up
# or python main.py -t push-up
# or python main.py -t squat
# or python main.py -t walk
```


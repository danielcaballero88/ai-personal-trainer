#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" -d '{
  "weight": "60-65 kg",
  "height": "175-180 cm",
  "fitness_goal": "Muscle gain",
  "days_per_week": 3,
  "health_concerns": ["None"],
  "experience_level": "Intermediate",
  "cardio_comfort": "Like it",
  "workout_location": "Gym",
  "equipment": ["Dumbbells", "Resistance bands"],
  "flexibility_level": 8
}' http://localhost:8000/get-plan

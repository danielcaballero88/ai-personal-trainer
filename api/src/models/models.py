"""Pydantic models for the API"""

from enum import Enum
from pydantic import BaseModel, field_validator


class Weight(str, Enum):
    _45_50 = "45-50 kg"
    _50_55 = "50-55 kg"
    _55_60 = "55-60 kg"
    _60_65 = "60-65 kg"
    _65_70 = "65-70 kg"
    _75_80 = "75-80 kg"
    _80_85 = "80-85 kg"
    _85_90 = "85-90 kg"
    _90_95 = "90-95 kg"
    _95_100 = "95-100 kg"


class Height(str, Enum):
    BELOW_165 = "Below 165 cm"
    _165_175 = "165-175 cm"
    _175_180 = "175-180 cm"
    _180_185 = "180-185 cm"
    _190_PLUS = "190 cm and above"


class FitnessGoal(str, Enum):
    WEIGHT_LOSS = "Weight loss"
    MUSCLE_GAIN = "Muscle gain"
    OVERALL_FITNESS = "Overall fitness"
    ENDURANCE_IMPROVEMENT = "Endurance improvement"
    FLEXIBILITY_ENHANCEMENT = "Flexibility enhancement"


class HealthConcerns(str, Enum):
    NONE = "None"
    KNEE_PAIN = "Knee pain"
    BACK_PAIN = "Back pain"
    SHOULDER_ISSUES = "Shoulder issues"
    OTHER = "Other"


class ExperienceLevel(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class CardioComfort(str, Enum):
    LOVE_IT = "Love it"
    LIKE_IT = "Like it"
    NEUTRAL = "Neutral"
    DISLIKE_IT = "Dislike it"
    HATE_IT = "Hate it"


class WorkoutLocation(str, Enum):
    GYM = "Gym"
    HOME = "Home"
    BOTH = "Both"


class Equipment(str, Enum):
    DUMBBELLS = "Dumbbells"
    BARBELLS = "Barbells"
    KETTLEBELLS = "Kettlebells"
    RESISTANCE_BANDS = "Resistance bands"
    NONE = "None (bodyweight exercises only)"


class UserInputFields(str, Enum):
    WEIGHT = "weight"
    HEIGHT = "height"
    FITNESS_GOAL = "fitness_goal"
    DAYS_PER_WEEK = "days_per_week"
    HEALTH_CONCERNS = "health_concerns"
    EXPERIENCE_LEVEL = "experience_level"
    CARDIO_COMFORT = "cardio_comfort"
    WORKOUT_LOCATION = "workout_location"
    EQUIPMENT = "equipment"
    FLEXIBILITY_LEVEL = "flexibility_level"


class UserInput(BaseModel):
    weight: Weight
    height: Height
    fitness_goal: FitnessGoal
    days_per_week: int
    health_concerns: list[HealthConcerns]
    experience_level: ExperienceLevel
    cardio_comfort: CardioComfort
    workout_location: WorkoutLocation
    equipment: list[Equipment]
    flexibility_level: int

    @field_validator("days_per_week")
    @classmethod
    def validate_days_per_week(cls, value: int) -> int:
        if not 1 <= value <= 7:
            raise ValueError("Wrong value for days per week")
        return value

    @field_validator("flexibility_level")
    @classmethod
    def validate_flexibility_level(cls, value: int) -> int:
        if not 1 <= value <= 10:
            raise ValueError("Wrong value for flexibility level")
        return value

    @field_validator("health_concerns")
    @classmethod
    def validate_health_concerns(cls, value: list[HealthConcerns]) -> HealthConcerns:
        if "None" in value and len(value) > 1:
            raise ValueError(
                "If 'None' in health concerns, no other health concern should be given."
            )

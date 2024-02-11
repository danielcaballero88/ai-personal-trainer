from openai import OpenAI

from src.config import OPENAI_ORG, OPENAI_API_KEY
from src.models import UserInputFields, UserInput

openai_client = OpenAI(
    organization=OPENAI_ORG,
    api_key=OPENAI_API_KEY,
)


questions = {
    UserInputFields.WEIGHT: "Can you share your current weight?",
    UserInputFields.HEIGHT: "Can you share your current height?",
    UserInputFields.FITNESS_GOAL: "What is your primary fitness goal? (e.g., weight loss, muscle gain, overall fitness)",
    UserInputFields.DAYS_PER_WEEK: "How many days per week can you commit to working out?",
    UserInputFields.HEALTH_CONCERNS: "Are there any specific health concerns or injuries I should be aware of?",
    UserInputFields.EXPERIENCE_LEVEL: "What is your experience level with weight training? (Beginner, intermediate, advanced)",
    UserInputFields.CARDIO_COMFORT: "How comfortable are you with cardiovascular exercises? (e.g., running, cycling, swimming)",
    UserInputFields.WORKOUT_LOCATION: "Do you have access to a gym, or will you be working out at home?",
    UserInputFields.FLEXIBILITY_LEVEL: "On a scale of 1 to 10, how would you rate your flexibility?",
    UserInputFields.EQUIPMENT: "What equipment, if any, do you have available for your workouts?",
}


def parse_user_input(user_input: UserInput):
    output = ""
    for key, val in user_input.model_dump().items():
        output += f"Q: {questions[key]}\n"
        output += f"A: {val}\n"
    return output


def get_system_message():
    return {
        "role": "system",
        "content": (
            "You are a personal trainer in a Gym, you are an expert preparing "
            "working out plans for other people. I want you to prepare a plan "
            "for me according to the input I give you."
        )
    }


def get_user_message(user_input: UserInput):
    return {
        "role": "user",
        "content": (
            "Provide a training plan for a month, 3 days a week, aprox 1hr "
            "each day, full body weight training in the gym. Do it according "
            "to the following answers to each topic:"
            "\n\n"
            f"{parse_user_input(user_input)}"
        )
    }


def get_plan(user_input: UserInput):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            get_system_message(),
            get_user_message(user_input),
        ],
        # stream=True,
    )
    return response.choices[0].message.content

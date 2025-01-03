#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crew import AiJobHunter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI and ML',
        'type': 'Co-op',
        'term': 'Summer 2025 term',
        'difficulty_level': 'junior or intermediate',
        'preferred_country': 'Canada',
        'preferred_province': 'Ontario',
        'preferred_cities': 'Toronto or Markham or Waterloo or Oakville or Hamilton or Ottawa',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }
    AiJobHunter().crew().kickoff(inputs=inputs)

run()

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiJobHunter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AiJobHunter().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiJobHunter().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

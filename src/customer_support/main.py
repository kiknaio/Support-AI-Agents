#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from customer_support.crew import CustomerSupport

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
        'customer': 'TokenGrower.com',
        'person': 'George Kiknadze',
        'inquiry': 'I want to know if I can use React.js to build a website for my business. Does React support SEO, and how can I optimize my website for search engines?'
    }
    
    try:
        CustomerSupport().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer': 'Remote.ge',
        'person': 'George Kiknadze',
        'inquiry': 'I want to know, if I can use CrewAI to build AI crew for my platform. I want to use it to help professionals find remote jobs and give them recommendations based on their skills and preferences, but what are other areas where I can use it?'
    }
    try:
        CustomerSupport().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'customer': 'Remote.ge',
        'person': 'George Kiknadze',
        'inquiry': 'I want to know, if I can use CrewAI to build AI crew for my platform. I want to use it to help professionals find remote jobs and give them recommendations based on their skills and preferences, but what are other areas where I can use it?'
    }
    try:
        CustomerSupport().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
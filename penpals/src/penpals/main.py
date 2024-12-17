import warnings
from penpals.crew import PenPals

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    dailyEntry = input("What did you do today:\n")

    inputs = {
        'dailyEntry': dailyEntry
    }
    PenPals().crew().kickoff(inputs=inputs)

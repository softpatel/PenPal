import warnings
from penpals.crew import PenPals

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'dailyEntry': 'I woke up around 6am to use the bathroom then laid in bed until 8:30am. I ate a yogurt parfait, protein shake and eggs for breakfast. Started work in my home office and going to buy more groceries after work.'
    }
    PenPals().crew().kickoff(inputs=inputs)

# PenPals
PenPals is an AI-powered journaling app where you enter your daily entries and get helpful advice from your circle of advisors that track your progress.

Mentors you can add into your circle include:
- Financial advisor
- Health Advisor
(Future ideas)
- Fitness instructor
- Event planner
- Relationship guide
- Career guide

Start by choosing your advisors and then providing some details about yourself and some of the goals you have. Your advisors will track your progress via your daily entries and report any insights or advice.

# Instructions
To set up, download the project and input your selected LLM and associated API key into a .env file in the project's root directory.

Example .env file:
```
MODEL=claude-3-5-sonnet-20240620
ANTHROPIC_API_KEY=<insert your own API key>
```

To run the PenPals crew, input your daily entry into the dailyEntry field within the main.py file. Then open a terminal pointing to the project's root directory and run `crewai run`.

The feedback from each agent will be generated and saved into a markdown file within the project's root directory.
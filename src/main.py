from agents.users import user
from agents.animagine_agent import animagine_agent
from uagents import Bureau
if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:5000/submit", port=8000)
    bureau.add(animagine_agent)
    bureau.add(user)
    bureau.run()
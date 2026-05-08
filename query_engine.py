from database import run_query

def process_query(user_input):
    user_input = user_input.lower()

    if "open tickets" in user_input:
        results = run_query("SELECT * FROM tickets WHERE status='Open'")
        return results

    elif "closed tickets" in user_input:
        results = run_query("SELECT * FROM tickets WHERE status='Closed'")
        return results

    elif "wireless" in user_input:
        results = run_query("SELECT * FROM tickets WHERE service='Wireless'")
        return results

    elif "it manager" in user_input or "it contact" in user_input:
        results = run_query("SELECT * FROM directory WHERE department='IT'")
        return results

    else:
        return [("No matching result found.",)]
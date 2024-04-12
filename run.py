from jess.crew import create_crew_for_question


if __name__ == "__main__":
    messages_history = []
    message = ""
    while message != "exit":
        message = input("Enter your message: ")
        messages_history.append(f"user message: {message}")
        full_message = "\n".join(messages_history)
        answer = create_crew_for_question(full_message, verbose=False).kickoff()
        messages_history.append(f"jess: {answer}")
        print(answer)
        if len(messages_history) > 100:
            messages_history = messages_history[-2:]

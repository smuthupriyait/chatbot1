import random

# Sample event data
events = [
    {"name": "Marathon 2024", "date": "March 15, 2024", "location": "New York"},
    {"name": "Cycling Race 2024", "date": "April 22, 2024", "location": "San Francisco"},
    {"name": "Biking Event 2024", "date": "May 30, 2024", "location": "Los Angeles"},
]

def get_events():
    return events

def get_event_details(event_name):
    for event in events:
        if event['name'].lower() == event_name.lower():
            return event
    return None

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hi" in user_input or "hello" in user_input:
        return "Hi there! I'm here to help you find events and book tickets."
    elif "event" in user_input:
        event_list = ', '.join([f"{event['name']} on {event['date']} at {event['location']}" for event in get_events()])
        return f"Here are some upcoming events: {event_list}."
    elif "book" in user_input:
        return "To book tickets, please visit our booking page. If you need more information, check this link: [Booking Info](https://dummybookinglink.com)."
    elif "details" in user_input:
        event_name = user_input.split("details about")[-1].strip()
        event_details = get_event_details(event_name)
        if event_details:
            return (f"{event_details['name']} is happening on {event_details['date']} at {event_details['location']}. "
                    f"For more information, check this link: [Event Details](https://dummyeventlink.com).")
        else:
            return "I'm sorry, I couldn't find any details about that event. Please check our events page for more information."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. If you need more information, look at this link: [More Info](https://dummylink.com)."

# Example of running the chatbot
if __name__ == "__main__":
    print("Chatbot: Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == 'bye':
            break

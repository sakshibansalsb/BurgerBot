import google.generativeai as genai
import gradio as gr

# Replace with your actual API key
api_key = "AIzaSyBizxFLIQSrfhGMOoRb-0N2iA0lVOV-NUU"
genai.configure(api_key=api_key)

# Define the generative model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the conversation history (empty list)
chat = model.start_chat(history=[])

# Define function, which helps to execute any prompt
def get_llm_response(message):
    response = chat.send_message(message)
    return response.text

# Define the updated basic information about the chatbot
base_info = """
Welcome to Stellar Eats, where we serve the best gourmet burgers in town! 
I'm here to help you with your order. First, I'll need to know what you'd like to order from our menu. 
I can assist you with picking items from our burger selection, fries, toppings, and drinks. 
I'll also ask if your order is for pickup or delivery, and collect any additional details as needed.
"""

# Define updated delivery-related instructions
delivery_info = """
For delivery orders, I'll need your address to ensure timely delivery. 
I'll also gather payment information and confirm all your choices to make sure everything is perfect. 
Please take a look at our menu and let me know your preferences:
"""

# Define the updated menu structure
# Define available burger types
burger_type = """
Galactic Burger for 89 Rs \
Meteorite Burger for 199 Rs \
Spicy Veggie Burger for 109 Rs \
Classic Beef Burger for 139 Rs \
Double Meat Burger for 199 Rs \
"""
# Define available fries
fries = "50 Rs, 65 Rs, 85 Rs"

# Define available toppings
toppings = """
fresh lettuce 20 Rs  \
ripe tomato 20 Rs  \
crisp onion 20 Rs  \
dill pickles 20 Rs  \
sautéed mushrooms 20 Rs  \
extra cheddar cheese 25 Rs  \
spicy BBQ sauce 20 Rs  \
jalapeños 15 Rs
"""

# Define available drinks
drinks = """
iced tea 70 Rs, 50 Rs, 35 Rs \
lemonade 70 Rs, 50 Rs, 35 Rs \
sparkling water 60 Rs \
"""

# Function to create the welcome message with menu details
def create_welcome_message():
    """
    Generates the initial welcome message with updated menu information.

    Returns:
        str: The welcome message string.
    """
    return f"""
    {base_info}
    {delivery_info}
    Burger Menu:
    {burger_type}
    Fries Menu:
    {fries}
    Toppings:
    {toppings}
    Drinks Menu:
    {drinks}
    """

# Define greeting message
greeting_message = "Hello Sir/ Mam \n Welcome to Stellar Eats! 🍔 I'm excited to help you with your burger order today. \nWhat would you like to start with?"

# Define communication function
def bot(message, history):
    # If this is the first interaction, send the greeting message
    if not history:
        response = greeting_message
    else:
        # Otherwise, use the provided menu and conversation history
        prompt = create_welcome_message() + f"\nUser: {message}"
        response = get_llm_response(prompt)
    
    # Update history with the user message and the response
    if not history:
        history.append([greeting_message, "bot"])  # Add greeting to history
    history.append([message, "user"])
    history.append([response, "bot"])
    
    return response

# Create Gradio instance
demo = gr.ChatInterface(
    fn=bot, 
    examples=[
        "I'd like to order a Galactic Burger and fries.",
        "Can I have a Spicy Veggie Burger with extra cheddar cheese?",
        "I'd like a Lemonade and some sautéed mushrooms on my burger.",
        "What's the address for delivery?"
    ], 
    title="Stellar Eats Order Bot"
)

# Launch Gradio chatbot
demo.launch(debug=True, share=True)

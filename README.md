# BurgerBot Chatbot

BurgerBot is an interactive chatbot designed for taking orders for "Stellar Eats" . It allows users to place orders for burgers, fries, and drinks, and handle details for pickup or delivery.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

BurgerBot is built using a Large Language Model (LLM) integrated with Gradio for the chat interface. It helps users to place food orders and manage their requests in a conversational manner.

## Key Features

- Greet users and initiate conversation.
- Collect detailed orders for burgers, fries, drinks, and toppings.
- Manage delivery or pickup options.
- Display and confirm order summaries.
- Handle payment information for delivery orders.

## Architecture

The system is composed of the following components:

- **Chatbot Interface (Gradio)**: Provides the user interface for interacting with the chatbot.
- **Backend Processor**: Manages conversation context and prepares data for the LLM.
- **API Gateway**: Handles API requests and responses between the backend and the LLM.
- **Large Language Model (LLM)**: Processes user inputs and generates appropriate responses.

### Data Flow

1. **User Input → Chatbot Interface**: Users enter their messages or select options.
2. **Chatbot Interface → Backend Processor**: Sends user input for context management.
3. **Backend Processor → API Gateway**: Prepares and forwards the request to the LLM.
4. **API Gateway → LLM**: LLM processes the request and generates a response.
5. **LLM → API Gateway**: Returns the response to the API Gateway.
6. **API Gateway → Backend Processor**: Forwards the LLM's response.
7. **Backend Processor → Chatbot Interface**: Sends the response to be displayed.
8. **Chatbot Interface → User**: Displays the response to the user.

## Setup Instructions

To set up and run BurgerBot locally, follow these instructions:

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/burgerbot.git
    cd burgerbot
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```env
    API_KEY=your_actual_api_key_here
    ```

5. **Run the Application**

    ```bash
    python app.py
    ```

    By default, the application will start a Gradio interface accessible at [http://localhost:7860](http://localhost:7860).

## Usage

- **Greet and Order**: Start the chat by greeting the bot. Follow the instructions to place an order.
- **Order Types**: Specify whether your order is for pickup or delivery.
- **Menu**: Select from various burger types, fries, drinks, and toppings.
- **Confirm Order**: Review and confirm your order summary.

## Contributing

Contributions to BurgerBot are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch to your fork (`git push origin feature-branch`).
5. Create a Pull Request from your fork to the main repository.

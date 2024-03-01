# AI ChatBot using Django

This project implements an AI-powered chatbot using Django and the ChatGPT API. It provides a modern interface for users to interact with the chatbot.

## Technologies Used

- Python
- Django
- ChatGPT API
- Bootstrap 5
- CSS3
- jQuery
- Ajax
- Poetry for package management
- Anaconda for environment

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Rajeshkumar-14/django-ai-chatbot.git
    ```
2.  **Create and Activate Conda Environment:**

    - Create a new Conda environment:

      ```bash
      conda create --name chat-bot-env python=3.12
      ```

    - Activate the Conda environment:

      ```bash
      conda activate chat-bot-env
      ```

3.  **Create .env file:**

    - Create a `.env` file in the main directory for storing your OPENAI_API_KEY.

      ```bash
      OPENAI_API_KEY="your-api-key"
      ```

    - Remove spaces between the variable and equals and the value to avoid errors.

4.  **Install Dependencies:**

    - Install Poetry:

      ```bash
      pip install poetry
      ```

    - Run this command after installing Poetry:

      ```bash
      poetry install
      ```

5.  **Run the Django development server:**

         ```bash
         python manage.py runserver
         ```

    Access the booking system at [http://localhost:8000/](http://localhost:8000/)

## Usage

- Start a conversation by typing a message in the chatbox.
- Receive responses from the AI-powered chatbot.
- Interact with the chatbot using natural language.

## Contributing

- Contributions are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

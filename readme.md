# Color Palette App

A Python Flask web application that uses the OpenAI GPT-3.5-turbo model to generate color palettes based on the input prompts.

## Prerequisites

Before running this application, ensure that you have the following dependencies installed:

- Python 3.7 or above
- Pip

## Getting Started

Follow the steps below to get started with the Color Palette App:

1. Clone the repository to your local machine.

   ```
   git clone https://github.com/your_username/color-palette-app.git
   ```

2. Install the required dependencies by running the following command inside the project directory:

   ```
   pip install -r requirements.txt
   ```

3. Create a .env file and add an `OPENAI_API_KEY=` field with your open ai key value supplied to it.

## Running the App

After setting up the API key, start the Flask development server by running the following command:

```
python app.py
```

This will start the server and make the Color Palette App accessible at `http://localhost:5000`.

## Usage

Once the application is running, you can access it using a web browser. On the homepage, you will find a text input field where you can enter your prompt.

- Enter a description or a phrase related to the color palette you want to generate.
- Click the "Generate" button or press `Enter` to submit the prompt.

The OpenAI GPT-3.5-turbo model will generate and display a color palette based on your input prompt. You can try different prompts to explore various color combinations.


## License

The Color Palette App is released under the [MIT License](LICENSE). Feel free to modify and use the code as per your requirements.
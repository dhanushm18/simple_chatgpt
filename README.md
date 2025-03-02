# simple_chatgpt

- **`.env`**: Contains environment variables, including the Google API key.
- **`.gitignore`**: Specifies files and directories to be ignored by git.
- **`app.py`**: Streamlit application for text-based queries.
- **`vision.py`**: Streamlit application for image-based queries.
- **`requirements.txt`**: Lists the dependencies required for the project.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd simple_chatgpt
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/5) file in the root directory and add your Google API key:
    ```env
    GOOGLE_API-KEY="your-google-api-key"
    ```

## Running the Applications

### Text-based Query Application

To run the text-based query application, execute the following command:
```sh
streamlit run app.py

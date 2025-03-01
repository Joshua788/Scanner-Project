# Scanner-Project
# Port Scanner Web Application

This is a simple web-based port scanner tool built using Flask that allows users to scan ports on a target IP address. It allows scanning of a custom port range or the first 1000 ports by default. The app logs all activities and provides results in a user-friendly format.

## Features

- Scans an IP address for open ports.
- Option to scan a custom range of ports.
- Displays results in a clean table format.
- Error handling for invalid inputs.
- Logging for tracking port scan activities.

## Prerequisites

To run this project, you need the following:

- Python 3.12.9 or higher
- Virtual environment (optional but recommended)
- Flask version 2.2.2

## Installation Steps

1. **Clone the repository:**

   First, clone the project repository to your local machine:

   git clone https://github.com/Joshua788/scanner-project.git
   cd scanner-project

2. **Set up the virtual environment:**

   You can create a virtual environment to isolate the dependencies:

   - For Windows (PowerShell):

     python -m venv venv
     .\venv\bin\activate
   

   - For macOS/Linux:


     python3 -m venv venv
     source venv/bin/activate
    

3. **Install dependencies:**

   Install the required Python packages by running:


   pip install -r requirements.txt
  

4. **Run the application:**

   After setting up your environment, run the Flask application with:


   python scanner.py


   This will start the web server. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the port scanner.

## Usage

- Open the web application in your browser.
- Enter the IP address you want to scan.
- Optionally, check the "Use Custom Port Range" box to specify a custom start and end port range.
- Click on "Start Scan" to begin scanning.
- View the open ports on the results page.

## Folder Structure


scanner-project/
├── scanner.py                   # Main application file (Flask app)
├── requirements.txt         # List of required dependencies
├── templates/
│   ├── index.html           # HTML form to input the target IP
│   └── result.html          # Results page to display open ports
└── venv/                    # Virtual environment folder (not pushed to GitHub)


## Dependencies

This project requires the following Python packages:

- Flask==2.2.2
- (Any other required dependencies in your `requirements.txt`)

To install dependencies, use the command:
pip install -r requirements.txt


## Logging

- Logs are stored using Python's built-in `logging` library.
- Logs are saved with the timestamp of each scan attempt.

## Troubleshooting

- **"Invalid IP address" Error:**
  - Make sure the IP address entered is correctly formatted (IPv4).
  
- **"Port range must be between 1 and 65535" Error:**
  - Ensure you provide a valid range of ports within the 1-65535 range.

- **Server not starting:**
  - Make sure all dependencies are installed and your virtual environment is active.



## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, feel free to reach out to the repository owner at joshuaize@icloud.com.

# Energy Management

The Active Attributes API is designed to continuously scan video feeds for QR codes and extract defined attributes related to environmental and vehicular conditions. This project leverages Flask for the API server and uses OpenCV and Pyzbar for decoding QR codes from live video feeds.

## Features

- **Real-time QR code decoding**: Scans and decodes QR codes in real-time from a video feed.
- **Attribute extraction**: Identifies specific attributes from QR codes such as `night`, `cloudy`, vehicle counts, and charging statuses.
- **REST API**: Provides an endpoint to fetch the current set of active attributes extracted from the video feed.

## Installation

To run this API, you need Python installed on your system along with several libraries including Flask, OpenCV, and Pyzbar.

1. **Clone the repository**:
   - ```bash
     git clone https://your-repository-url.git
     ```
   - ```bash
     cd your-repository-directory
     ```

2. **Install dependencies**:
   - ```bash
     pip install Flask opencv-python pyzbar
     ```

3. **Set up a virtual environment (optional)**:
   - ```bash
     python -m venv venv
     ```
   - ```bash
     `venv\Scripts\activate`
     ```

## Usage

1. **Start the API server**:
   - ```bash
     python Api.py
     ```
   This will start the Flask server in debug mode on the default port 5000.

2. **Access the API**:
   - To get the current active attributes, use the following GET request:
     ```bash
     curl http://localhost:5000/api/attributes
     ```
   This endpoint returns a JSON object with the currently detected attributes such as:
   ```json
   {
     "cloudy": false,
     "night": true,
     "car": 3,
     "electricCars": 1,
     "electricScooters": 2,
     "chargingElectricCars": 1,
     "chargingElectricScooters": 1
   }

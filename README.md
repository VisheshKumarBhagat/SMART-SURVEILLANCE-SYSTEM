

# SMART Surveillance System

The SMART Surveillance System is a comprehensive security solution leveraging Python and OpenCV to deliver real-time monitoring capabilities. It integrates motion detection, facial recognition, entry/exit tracking, and automated recording into a unified graphical interface, providing robust environmental surveillance for both residential and commercial applications.

---

## Features

### 1. Motion Detection

- Detects motion using frame differencing and contour analysis.
- Saves anomaly images with timestamps in the `stolen/` directory.


### 2. Facial Recognition

- Uses Haar Cascade classifiers for face detection.
- Supports enrollment of new subjects and real-time identification.
- Stores training data in the `persons/` directory.


### 3. Entry/Exit Tracking

- Implements directional tracking across surveillance zones.
- Differentiates between ingress and egress events.
- Saves images of visitors in `visitors/in/` and `visitors/out/` directories.


### 4. Automated Recording

- Records video footage continuously and saves it in the `recordings/` directory.


### 5. Graphical User Interface (GUI)

- Built using Tkinter for easy navigation and control.
- Provides seven operational modes:
    - **Monitor**: Baseline motion detection.
    - **Rectangle**: Structural shape analysis.
    - **Noise**: Audio anomaly detection.
    - **Record**: Continuous video capture.
    - **In Out**: Directional movement tracking.
    - **Identify**: Facial recognition system.
    - **Exit**: Graceful shutdown procedure.

---

## Installation

Follow these steps to set up the SMART Surveillance System on your machine:

### Step 1: Create a Python Virtual Environment

Run the following commands to create an isolated Python environment:

#### For Windows:

```&lt;command&gt;
python -m venv venv
venv\Scripts\activate
```


#### For Linux/macOS:

```&lt;command&gt;
python3 -m venv venv
source venv/bin/activate
```


### Step 2: Install Dependencies

Install all required packages using the `requirements.txt` file:

```&lt;command&gt;
pip install -r requirements.txt
```

This will install dependencies such as:

- `opencv-python`
- `scikit-image`
- `pillow`
- `beepy`


### Step 3: Run the Application

Launch the main application by running the following command:

```&lt;command&gt;
python main.py
```

---

## Directory Structure

The system organizes data into the following directories:

- **recordings/**: Stores recorded video footage (MPEG-4 format).
- **visitors/**: Contains images of visitors classified by movement direction (`in/` and `out/`).
- **stolen/**: Saves images of detected anomalies with timestamps.
- **icons/**: Contains GUI assets (PNG format).

---

## System Requirements

For optimal performance, ensure your system meets the following specifications:

- Quad-core processor (2.4GHz or higher).
- At least 8GB RAM.
- Dedicated GPU compatible with OpenCV for faster processing.
- Minimum 500GB storage for video archives.

---

## Future Enhancements

The modular architecture ensures adaptability for future improvements, including:

- Integration with machine learning models for advanced analytics.
- IoT device interoperability for remote monitoring capabilities.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

Developed by:
1. [Vishesh Kumar Bhagat](https://github.com/VisheshKumarBhagat).
2. [Debojyoti Jha](http://github.com/jd3b)
3. [Shaurya Anand](https://github.com/Shaurya-rgb89)
4. [Shivam Agarwal](https://github.com/Kaljinx)
5. [Sparsh Mishra](https://github.com/Sparsh08Mishra)
6. [Sahasranshu Shastri](https://github.com/Sahasranshu-Shastri)
---

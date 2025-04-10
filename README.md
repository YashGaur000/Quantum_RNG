# Quantum Random Number Generator

A simple web application that generates random numbers using quantum mechanics principles. The application uses Qiskit for quantum computing simulation and Streamlit for the user interface.

## Features

- Generates random bits using quantum superposition
- Creates random numbers between 0 and 100
- Simple and intuitive web interface
- Real-time quantum simulation

## Setup

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute:
```bash
streamlit run quantum_rng.py
```

The application will open in your default web browser. Click the "Generate Random Number" button to generate a new random number using quantum mechanics!

## How it Works

The application uses a quantum circuit with a single qubit. It applies a Hadamard gate to create a superposition state, then measures the qubit to get a random bit (0 or 1). Multiple measurements are combined to generate a random number between 0 and 100. 
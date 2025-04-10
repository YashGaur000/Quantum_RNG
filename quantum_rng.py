import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def generate_quantum_random_number():
    try:
        # Create a quantum circuit with 1 qubit
        qc = QuantumCircuit(1, 1)
        
        # Apply Hadamard gate to create superposition
        qc.h(0)
        
        # Measure the qubit
        qc.measure(0, 0)
        
        # Use the Aer simulator
        simulator = AerSimulator()
        
        # Execute the circuit
        job = simulator.run(qc, shots=1)
        result = job.result()
        
        # Get the measurement result
        counts = result.get_counts()
        return int(list(counts.keys())[0])
    except Exception as e:
        st.error(f"Error generating quantum random number: {str(e)}")
        return None

def main():
    st.title("Quantum Random Number Generator")
    st.write("This application generates random numbers using quantum mechanics!")
    
    # Add some explanation
    st.markdown("""
    ### How it works:
    1. We create a quantum circuit with one qubit
    2. Apply a Hadamard gate to create superposition
    3. Measure the qubit to get a random bit (0 or 1)
    """)
    
    # Generate random number button
    if st.button("Generate Random Number"):
        with st.spinner("Generating quantum random number..."):
            random_bit = generate_quantum_random_number()
            if random_bit is not None:
                st.success(f"Generated random bit: {random_bit}")
                
                # Generate a random number between 0 and 100 using multiple bits
                num_bits = 7
                random_number = 0
                for _ in range(num_bits):
                    bit = generate_quantum_random_number()
                    if bit is None:
                        st.error("Failed to generate random number")
                        return
                    random_number = (random_number << 1) | bit
                
                random_number = random_number % 101  # Ensure number is between 0 and 100
                st.success(f"Generated random number (0-100): {random_number}")

if __name__ == "__main__":
    main() 
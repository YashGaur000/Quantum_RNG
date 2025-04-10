import streamlit as st
from quantum_rng import generate_quantum_random_number  # 🧠 Reuse the function

def main():
    st.title("🧪 Quantum Random Number Generator")
    st.write("Generate truly random numbers using quantum mechanics!")

    st.markdown("""
    ### ⚙️ How It Works:
    - A Hadamard gate is applied to a single qubit.
    - This creates superposition.
    - The qubit is then measured to collapse into 0 or 1 randomly.
    """)

    if st.button("Generate Quantum Random Number"):
        with st.spinner("Accessing the quantum realm..."):
            bit = generate_quantum_random_number()
            if bit is not None:
                st.success(f"Random bit: {bit}")

                st.info("Generating 7 bits to construct a number between 0–100...")
                number = 0
                for _ in range(7):
                    b = generate_quantum_random_number()
                    if b is None:
                        st.error("Quantum failure during generation.")
                        return
                    number = (number << 1) | b

                final_number = number % 101
                st.success(f"🎲 Quantum Random Number (0–100): {final_number}")

if __name__ == "__main__":
    main()

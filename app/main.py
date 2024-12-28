import os
from src.signal_capture import capture_signal

def main():
    print("Step 1: Capturing RF Signal...")

    # Path for saving the captured raw signal
    raw_signal_file = os.path.join(os.getcwd(), 'captured_signal.npy')

    try:
        # Call the capture_signal function with the desired frequency
        # For example, capture a signal at 900 MHz (valid frequency for the R820T tuner)
        capture_signal(raw_signal_file, frequency=900000000)
        print("Signal capture completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

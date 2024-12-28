import numpy as np
from rtlsdr import RtlSdr

def capture_signal(output_file, frequency=900000000):  # Default frequency set to 900 MHz
    """
    Captures the RF signal using the RTL-SDR device and saves the data to the specified file.

    :param output_file: Path to the output file where the captured signal will be stored
    :param frequency: The frequency to tune to (in Hz), default is 900 MHz
    """
    # Check if the frequency is within the valid range (24 MHz to 1.75 GHz)
    if not (24000000 <= frequency <= 1750000000):
        raise ValueError(f"Invalid frequency: {frequency}. Please choose a frequency between 24 MHz and 1.75 GHz.")

    # Initialize RTL-SDR device
    sdr = RtlSdr()
    try:
        # Set RTL-SDR parameters
        sdr.sample_rate = 2.048e6  # Sample rate (can be adjusted)
        sdr.gain = 'auto'  # Automatic gain control
        sdr.center_freq = frequency  # Set the center frequency

        # Capture samples (you can adjust the number of samples to capture)
        samples = sdr.read_samples(256*1024)

        # Save the captured samples to the output file (this could be a binary or CSV format)
        np.save(output_file, samples)  # Save as NumPy array for easy analysis

        print(f"Signal captured successfully to {output_file}")

    except Exception as e:
        print(f"Error during signal capture: {e}")
    finally:
        sdr.close()  # Always close the SDR to free resources

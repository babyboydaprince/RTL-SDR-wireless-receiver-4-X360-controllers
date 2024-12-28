import numpy as np

def decode_rf_signal(input_file, output_file):
    """
    Decodes raw RF samples into controller inputs.
    Args:
        input_file (str): Path to the raw RF samples file.
        output_file (str): Path to save the decoded inputs log.
    Returns:
        list: Decoded controller inputs.
    """
    try:
        # Load the raw samples
        with open(input_file, 'rb') as f:
            raw_data = f.read()
        samples = np.frombuffer(raw_data, dtype=np.complex64)

        # Analyze samples
        print("Analyzing signal...")
        decoded_inputs = []

        # Process the signal to find patterns (placeholder for actual decoding logic)
        magnitude = np.abs(samples)  # Calculate magnitude of the signal
        threshold = np.mean(magnitude) * 1.5  # Define a threshold to detect signal peaks

        # Example: Detect peaks above the threshold
        peaks = np.where(magnitude > threshold)[0]
        print(f"Detected {len(peaks)} peaks in the signal.")

        # Map peaks to simulated input events (placeholder logic)
        if len(peaks) > 0:
            decoded_inputs.append("Button A Pressed")
        if len(peaks) > 10:
            decoded_inputs.append("Joystick Moved Up")
        if len(peaks) > 20:
            decoded_inputs.append("Trigger Pulled Left")

        # Save decoded inputs to a log file
        with open(output_file, 'w') as f:
            for input_event in decoded_inputs:
                f.write(f"{input_event}\n")

        print(f"Decoded inputs saved to {output_file}")
        return decoded_inputs
    except Exception as e:
        print(f"Error decoding signal: {e}")
        return []

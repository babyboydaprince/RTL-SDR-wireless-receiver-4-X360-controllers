import pyvjoy

def send_to_virtual_controller(inputs):
    """
    Maps decoded inputs to a virtual controller using vJoy.
    Args:
        inputs (list): List of decoded controller input events.
    """
    try:
        # Initialize virtual joystick
        j = pyvjoy.VJoyDevice(1)
        print("Sending inputs to virtual controller...")

        for input_event in inputs:
            if "Button A" in input_event:
                j.set_button(1, 1)  # Press Button 1
            elif "Joystick Moved Up" in input_event:
                j.set_axis(pyvjoy.HID_USAGE_Y, 0)  # Move joystick up
            elif "Trigger Pulled Left" in input_event:
                j.set_button(2, 1)  # Press Button 2

            print(f"Processed: {input_event}")

        # Reset controller to default state
        j.reset()
        print("Inputs successfully sent to virtual controller.")
    except Exception as e:
        print(f"Error mapping inputs to virtual controller: {e}")

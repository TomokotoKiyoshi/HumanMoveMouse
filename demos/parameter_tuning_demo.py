# demos/parameter_tuning_demo.py
import time
from human_mouse.human_mouse_controller import HumanMouseController

def run_parameter_demo():
    """Demonstrates the effect of different controller parameters."""
    print("--- Starting Parameter Tuning Demo ---")

    point_A = (300, 500)
    point_B = (1000, 500)
    
    print("Demonstration will start in 3 seconds... Please observe the mouse path carefully.")
    time.sleep(3)

    # --- Part 1: Speed Factor ---
    print("\n1. Demonstrating 'speed_factor'.")
    controller = HumanMouseController(model_pkl="mouse_model.pkl")
    
    print("  - Speed: 0.5x (Slow)")
    controller.set_speed(0.5)
    controller.move(point_A, point_B)
    time.sleep(0.5)
    
    print("  - Speed: 1.0x (Normal)")
    controller.set_speed(1.0)
    controller.move(point_B, point_A)
    time.sleep(0.5)
    
    print("  - Speed: 3.0x (Fast)")
    controller.set_speed(3.0)
    controller.move(point_A, point_B)
    time.sleep(1)

    # --- Part 2: Jitter Amplitude ---
    print("\n2. Demonstrating 'jitter_amplitude'.")
    
    print("  - Jitter: 0.2 (Very smooth path)")
    low_jitter_controller = HumanMouseController(model_pkl="mouse_model.pkl", jitter_amplitude=0.2)
    low_jitter_controller.move(point_B, point_A)
    time.sleep(0.5)
    
    print("  - Jitter: 5.0 (Very shaky path)")
    high_jitter_controller = HumanMouseController(model_pkl="mouse_model.pkl", jitter_amplitude=5.0)
    high_jitter_controller.move(point_A, point_B)
    time.sleep(1)

    # --- Part 3: Number of Points ---
    print("\n3. Demonstrating 'num_points'.")
    
    print("  - Num Points: 20 (Faster, less smooth)")
    low_points_controller = HumanMouseController(model_pkl="mouse_model.pkl", num_points=20)
    low_points_controller.move(point_B, point_A)
    time.sleep(0.5)

    print("  - Num Points: 200 (Slower, very smooth)")
    high_points_controller = HumanMouseController(model_pkl="mouse_model.pkl", num_points=200)
    high_points_controller.move(point_A, point_B)
    
    print("\n--- Parameter Tuning Demo Finished ---")

if __name__ == '__main__':
    run_parameter_demo()
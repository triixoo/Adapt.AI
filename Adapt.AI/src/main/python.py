# AI Adapt - Smart Home System

class LightingControl:
    def __init__(self):
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print("Lights turned on.")

    def turn_off(self):
        self.status = "off"
        print("Lights turned off.")

    def adjust_brightness(self, level):
        if 0 <= level <= 100:
            print(f"Brightness set to {level}%.")
        else:
            print("Brightness level must be between 0 and 100.")


class HeatingControl:
    def __init__(self):
        self.temperature = 20  # default temperature in Celsius

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"Heating set to {temp}°C.")


class SmartLock:
    def __init__(self):
        self.is_locked = True

    def lock(self):
        self.is_locked = True
        print("Door is locked.")

    def unlock(self):
        self.is_locked = False
        print("Door is unlocked.")


class Sensor:
    def __init__(self, name):
        self.name = name
        self.status = "inactive"

    def activate(self):
        self.status = "active"
        print(f"{self.name} sensor activated.")

    def deactivate(self):
        self.status = "inactive"
        print(f"{self.name} sensor deactivated.")


class WaterControl:
    def __init__(self):
        self.water_flow = "off"

    def turn_on(self):
        self.water_flow = "on"
        print("Water flow turned on.")

    def turn_off(self):
        self.water_flow = "off"
        print("Water flow turned off.")


class CameraControl:
    def __init__(self):
        self.status = "off"

    def start_recording(self):
        self.status = "recording"
        print("Camera recording started.")

    def stop_recording(self):
        self.status = "off"
        print("Camera recording stopped.")


# Main Controller for AI Adapt
class AIAdaptController:
    def __init__(self):
        self.lighting = LightingControl()
        self.heating = HeatingControl()
        self.lock = SmartLock()
        self.sensors = {
            "motion": Sensor("Motion"),
            "fire": Sensor("Fire"),
            "gas": Sensor("Gas")
        }
        self.water_control = WaterControl()
        self.camera = CameraControl()

    def execute_command(self, command, *args):
        # Placeholder for command execution
        if command == "lights_on":
            self.lighting.turn_on()
        elif command == "lights_off":
            self.lighting.turn_off()
        elif command == "set_temperature":
            self.heating.set_temperature(args[0])
        elif command == "lock_door":
            self.lock.lock()
        elif command == "unlock_door":
            self.lock.unlock()
        elif command == "activate_sensor":
            sensor_name = args[0]
            if sensor_name in self.sensors:
                self.sensors[sensor_name].activate()
            else:
                print("Sensor not found.")
        elif command == "deactivate_sensor":
            sensor_name = args[0]
            if sensor_name in self.sensors:
                self.sensors[sensor_name].deactivate()
            else:
                print("Sensor not found.")
        elif command == "start_camera":
            self.camera.start_recording()
        elif command == "stop_camera":
            self.camera.stop_recording()
        elif command == "water_on":
            self.water_control.turn_on()
        elif command == "water_off":
            self.water_control.turn_off()
        else:
            print("Command not recognized.")

# Example usage:
if __name__ == "__main__":
    controller = AIAdaptController()
    controller.execute_command("lights_on")
    controller.execute_command("set_temperature", 22)
    controller.execute_command("unlock_door")
    controller.execute_command("activate_sensor", "motion")
    controller.execute_command("start_camera")

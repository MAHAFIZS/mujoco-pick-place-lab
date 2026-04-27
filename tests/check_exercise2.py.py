import os
import mujoco

def test_world_exists():
    assert os.path.exists("starter_code/world.xml")

def test_world_loads():
    mujoco.MjModel.from_xml_path("starter_code/world.xml")

def test_second_robot_present():
    with open("starter_code/world.xml", "r", encoding="utf-8") as f:
        text = f.read().lower()

    assert (
        "robot2" in text
        or "panda_robot2" in text
        or text.count("panda") >= 2
    ), "No clear evidence of second robot"

def test_screenshot_exists():
    path = "screenshots/two_robots.png"
    assert os.path.exists(path), "Missing screenshot"
    assert os.path.getsize(path) > 1000, "Screenshot too small"
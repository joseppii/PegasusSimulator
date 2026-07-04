"""
| Author: Marcelo Jacinto (marcelo.jacinto@tecnico.ulisboa.pt)
| License: BSD-3-Clause. Copyright (c) 2024, Marcelo Jacinto. All rights reserved.
"""

from .people_backend import PeopleBackend

# Try to make the ROS2 people backend available. Log the real import error instead of swallowing it.
try:
    from .ros2_people_backend import ROS2PeopleBackend
except Exception as e:
    import carb, traceback
    carb.log_warn(f"ROS2PeopleBackend will not be available — import failed: {e!r}\n{traceback.format_exc()}")
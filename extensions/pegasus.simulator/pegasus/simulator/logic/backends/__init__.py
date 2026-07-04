"""
| Author: Marcelo Jacinto (marcelo.jacinto@tecnico.ulisboa.pt)
| License: BSD-3-Clause. Copyright (c) 2023, Marcelo Jacinto. All rights reserved.
"""

from .backend import Backend, BackendConfig
from .px4_mavlink_backend import PX4MavlinkBackend, PX4MavlinkBackendConfig
from .ardupilot_mavlink_backend import ArduPilotMavlinkBackend, ArduPilotMavlinkBackendConfig

# Try to make the ROS2 backend available. This requires both a working ROS2 install (sourced before
# launching Isaac Sim) and the Isaac Sim ROS2 bridge. Log the real import error instead of swallowing
# it, since "ROS2 not available" is often caused by an Isaac Sim API change rather than a missing ROS2.
try:
    from .ros2_backend import ROS2Backend
except Exception as e:
    import carb, traceback
    carb.log_warn(f"ROS2Backend will not be available — import failed: {e!r}\n{traceback.format_exc()}")
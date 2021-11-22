#!/usr/bin/env python

import signal
import sys
import random
import numpy as np
from interbotix_xs_modules.arm import InterbotixManipulatorXS

# To initiate, start roslaunch first in background
# > roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=px100 use_rviz:=false &
# > python random_dance.py
#
# Kill background roslaunch process with:
# > ps u | grep roslaunch | awk 'NR==1{print $2}' | xargs kill


bot = InterbotixManipulatorXS("px100", "arm", "gripper")

def signal_handler(sig, frame):
    print("\nExiting cleanly")
    bot.arm.go_to_sleep_pose()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def main():
    print("Going to home pose...")
    bot.arm.go_to_home_pose()

    bot.gripper.set_pressure(1.0)
    dof = len(bot.arm.get_joint_commands())
    joints = np.empty(dof)
    np.set_printoptions(precision=3)

    while True:
      #  raw_input("Hit [Enter] to proceed to next waypoint")
        print("Setting next waypoint...")
        joints[0] = np.random.uniform(-np.pi/2, np.pi/2)
        joints[1] = np.random.uniform(-np.pi/2, 0)
        joints[2] = np.random.uniform(-np.pi/4, np.pi/4)
        joints[3] = np.random.uniform(-np.pi/2, np.pi/2)
        print(joints)

        pose = bot.arm.set_joint_positions(joints)
        if pose is False:
	        print("No valid path found for this joint state")
        else:
            if random.choice([False, False, True, False]):
                bot.gripper.close()
                bot.gripper.open()
        print("")
    

if __name__=='__main__':
    main()


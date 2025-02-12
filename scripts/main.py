#!/usr/bin/env python

import os
import sys
import glob
import rospy
from px100 import PX100
import utilities as util


IMAGE_NAME        = "/home/ubuntu/environment/aws_ws/src/robomaker_workshop/images/image_cap.png"
ACCESS_PROFILE    = "robomaker_workshop"

########################################################################################
#---------------------------- Start configurable variables -----------------------------#
########################################################################################

SIM_MODEL_ARN     = ""
REAL_MODEL_ARN    = ""
CONFIDENCE_THRESHOLD = 85

########################################################################################
#---------------------------- End configurable variables ------------------------------#
########################################################################################


def main():
  # Sim option will use move_it to drive arm in Gazebo
  # Otherwise script will attempt to move physical arm
  _sim = True if "--sim" in sys.argv else False
      
  # If accessing Rekognition model from an internal account,
  # then no separate role-based profile is needed
  _internal = True if "--internal" in sys.argv else False
  
  [os.remove(img) for img in glob.glob("*.png")]
  
  try:
    robot = PX100(simulated = _sim)
    
    if not _sim and not REAL_MODEL_ARN:
      rospy.logerr('Model ARN undefined for real hardware')
      return
      
    access_profile = "" if _internal else ACCESS_PROFILE
    model_arn = SIM_MODEL_ARN if _sim else REAL_MODEL_ARN
    model_name = model_arn.split('/')[-2]
    project_name = model_arn.split('/')[1]
    
    ########################################################################################
    #------------------------------------ Begin STEP 1 ------------------------------------#
    ########################################################################################

    ########################################################################################
    #------------------------------------- End STEP 1 -------------------------------------#
    ########################################################################################
   
   
    ########################################################################################
    #------------------------------------ Begin STEP 2 ------------------------------------#
    ########################################################################################

    ########################################################################################
    #------------------------------------- End STEP 2 -------------------------------------#
    ########################################################################################


    ########################################################################################
    #------------------------------------ Begin STEP 3 ------------------------------------#
    ########################################################################################

    ########################################################################################
    #------------------------------------- End STEP 3 -------------------------------------#
    ########################################################################################
  
     
    ########################################################################################
    #------------------------------------ Begin STEP 4 ------------------------------------#
    ########################################################################################

    ########################################################################################
    #------------------------------------- End STEP 4 -------------------------------------#
    ########################################################################################

  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return


if __name__ == '__main__':
  main()

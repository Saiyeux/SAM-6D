#! /bin/bash

# set the paths
export CAD_PATH=/home/surgicalai/Github/private/SAM-6D/SAM-6D/Data/Example/obj_000005.ply    # path to a given cad model(mm)
export RGB_PATH=/home/surgicalai/Github/private/SAM-6D/SAM-6D/Data/Example/rgb.png           # path to a given RGB image
export DEPTH_PATH=/home/surgicalai/Github/private/SAM-6D/SAM-6D/Data/Example/depth.png       # path to a given depth map(mm)
export CAMERA_PATH=/home/surgicalai/Github/private/SAM-6D/SAM-6D/Data/Example/camera.json    # path to given camera intrinsics
export OUTPUT_DIR=/home/surgicalai/Github/private/SAM-6D/SAM-6D/Data/Example/outputs         # path to a pre-defined file for saving results
export SEGMENTOR_MODEL=sam
export SEG_PATH=$OUTPUT_DIR/sam6d_results/detection_ism.json
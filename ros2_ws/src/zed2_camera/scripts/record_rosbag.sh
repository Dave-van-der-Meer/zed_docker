ros2 bag record \
    --max-cache-size 0 \
    --max-bag-size 2147483648 \
    -o test_bag_zed2 \
    -s mcap \
        /tf \
        /tf_static \
        /zed2/joint_states \
        /zed2/robot_description \
        /zed2/zed_node/atm_press \
        /zed2/zed_node/imu/data \
        /zed2/zed_node/imu/data_raw \
        /zed2/zed_node/imu/mag \
        /zed2/zed_node/left/camera_info \
        /zed2/zed_node/left/image_rect_color \
        /zed2/zed_node/left_cam_imu_transform \
        /zed2/zed_node/left_gray/camera_info \
        /zed2/zed_node/left_gray/image_rect_gray \
        /zed2/zed_node/right/camera_info \
        /zed2/zed_node/right/image_rect_color \
        /zed2/zed_node/right_gray/camera_info \
        /zed2/zed_node/right_gray/image_rect_gray \
        /vrpn_mocap/ZED2_camera_marker/pose


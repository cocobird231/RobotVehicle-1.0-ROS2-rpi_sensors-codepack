from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import yaml
from yaml import load, Loader

def generate_launch_description():
    commonFilePath = os.path.join(get_package_share_directory('py_gps'), 'launch/common.yaml')
    with open(commonFilePath, 'r') as f:
        data = yaml.load(f, Loader=Loader)
    return LaunchDescription([
        Node(
            package="py_gps",
            namespace=data['generic_prop']['namespace'],
            executable="pub",
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    "topic_GPS_nodeName" : data['topic_GPS']['nodeName'] + '_' + str(data['generic_prop']['id']) + '_node', 
                    "topic_GPS_topicName" : data['topic_GPS']['topicName'] + '_' + str(data['generic_prop']['id']), 
                    "topic_GPS_pubInterval_s" : data['topic_GPS']['publishInterval_s'], 
                    "module" : data['GPS_prop']['module'], 
                    "caster" : data['GPS_prop']['caster'], 
                    "port" : data['GPS_prop']['port'], 
                    "mountpoint" : data['GPS_prop']['mountpoint'], 
                    "username" : data['GPS_prop']['username'], 
                    "password" : data['GPS_prop']['password'], 

                    # Settings for Params class under vehicle_interfaces/params.h
                    # Do not change the settings rashly
                    "nodeName" : data['generic_prop']['nodeName'] + '_' + str(data['generic_prop']['id']) + '_node', 
                    "id" : data['generic_prop']['id'], 
                    "qosService" : data['generic_prop']['qosService'], 
                    "safetyService" : data['generic_prop']['safetyService'], 
                    "timesyncService" : data['generic_prop']['timesyncService'], 
                    "timesyncInterval_ms" : data['generic_prop']['timesyncInterval_ms'], 
                    "timesyncAccuracy_ms" : data['generic_prop']['timesyncAccuracy_ms'], 
                }
            ]
        )
    ])

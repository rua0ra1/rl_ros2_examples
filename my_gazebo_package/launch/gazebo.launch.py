<launch>
  <arg name="urdf_file" default="$(find my_gazebo_package)/urdf/my_robot.urdf"/>
  <arg name="gui" default="true"/>
  
  <node pkg="gazebo_ros" type="gazebo" name="gazebo" output="screen">
    <param name="robot_description" command="$(find xacro)/xacro --inorder $(arg urdf_file)"/>
    <param name="use_sim_time" value="true"/>
    <arg name="gui" value="$(arg gui)"/>
  </node>
</launch>

from setuptools import find_packages, setup

package_name = 'landmine_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='roboticsproject',
    maintainer_email='roboticsproject@todo.todo',
    description='Landmine detection system with GPR and obstacle avoidance',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'avoidance = landmine_robot.obstacle_avoidance:main',
            'gpr = landmine_robot.gpr_detector:main',
            'metallic_sensor = landmine_robot.metallic_sensor:main',  # Ensure correct path
            'landmine_visualizer = landmine_robot.landmine_visualizer:main',  # Add landmine_visualizer entry point
        ],
    },
)

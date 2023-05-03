from setuptools import setup
import os
from glob import glob

package_name = 'rl_cartpole_humble_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_data={'my_package': ['mesh/*.stl']},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob('urdf/*.urdf')),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('world/*.sdf'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ram',
    maintainer_email='thotaramcharanteja@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

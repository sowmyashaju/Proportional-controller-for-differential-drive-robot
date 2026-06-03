from setuptools import find_packages, setup

package_name = 'diff_drive_pid'

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
    maintainer='sowmya',
    maintainer_email='sowmya@todo.todo',
    description='Differential drive robot PID controller',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'controller = diff_drive_pid.controller:main',
        ],
    },
)

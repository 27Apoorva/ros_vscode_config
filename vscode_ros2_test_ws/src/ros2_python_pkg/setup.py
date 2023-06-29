from setuptools import setup

package_name = 'ros2_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nilutpolk',
    maintainer_email='nkelectronicshlnp@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ros2_python_pkg.publisher:main',
            'subscriber = ros2_python_pkg.subscriber:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'first_package'

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

    # The maintainer, maintainer_email, description
    # and license values must match the values in the 
    # package.xml file .
    maintainer='Destiny',
    maintainer_email='developer.oduwa@gmail.com',
    description='This is our first package ',
    license='New license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # as our entry point is the main function
            # in the first_package publisher.py file.
            'talker = first_package.publisher:main',
            'listener = first_package.subscriber:main'
        ],
    },
)

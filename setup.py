from distutils.core import setup

setup(
    name="notification_service",
    version="0.11",
    description="Interface and concretes for sending notifications",
    author="Chris Fernando",
    author_email="chris.t.fernando@gmail.com",
    url="https://github.com/chris-t-fernando/notification-service",
    packages=["notification_service"],
    install_requires=["slack_sdk", "pushover @ git+https://github.com/Wyattjoh/pushover"],
)
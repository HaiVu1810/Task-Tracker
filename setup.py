from setuptools import setup

setup(
    name='task-cli-app',
    version='1.0',
    py_modules=['task_cli', 'task_manager'],
    entry_points={
        'console_scripts': [
            'task-cli=task_cli:main', # Nó sẽ gọi hàm main() trong file task_cli.py
        ],
    },
)
# Command Plugin for OpenAI ChatGPT

This repository contains a command plugin for OpenAI ChatGPT. The plugin allows ChatGPT to execute Linux commands on the host and output the results.

## ChatGPT Plugin Developer

To run this, you'll need to be a plugin developer.
There's a waiting list for this: https://openai.com/waitlist/plugins


## ⚠️ Security Risks

Please be aware that this plugin can execute any command on the host system, potentially leading to data loss or other serious consequences if misused. It is recommended to use this plugin in a sandbox environment such as Docker and not to use it on a system containing sensitive data or that is accessible over the internet.

This repository is for developmental research only and is not intended for production use.

## Setup

To set up and run the command plugin, follow these steps:

1. **Clone the repository.** Use the command `git clone <repository_url>` to clone the repository to your local machine.

2. **Install Python.** The plugin is written in Python, so you'll need to have Python installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).

3. **Install the required Python packages.** The plugin requires the `quart` and `requests` Python packages. You can install these packages using pip, the Python package installer. Use the command `pip install quart requests` to install the packages.

4. **Set up a virtual environment (optional).** It's a good practice to set up a virtual environment when working with Python projects. This keeps the dependencies for the project separate from your global Python installation. You can use the `venv` module that comes with Python to create a virtual environment. Use the command `python3 -m venv env` to create a new virtual environment, and `source env/bin/activate` to activate it.

5. **Run the plugin.** You can run the plugin using the command `python3 main.py` or `python main.py`. This will start the plugin and it will begin listening for requests.

6. **Configure ChatGPT to use the plugin.** To configure ChatGPT to use the plugin, follow these steps:

* Navigate to https://chat.openai.com.
* In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
* Select "Plugin store"
* Select "Develop your own plugin"
* Enter in localhost:5003 since this is the URL the server is running on locally, then select "Find manifest file".

Remember, this plugin allows the execution of arbitrary commands on your system. Always ensure that the system running the plugin is secure and isolated from sensitive data or networks.

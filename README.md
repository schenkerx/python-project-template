# Python Project Template
A simple python project template.

## How to use
**Notice**: This python project template is designed to use with python 3.0+. If you are using python 2.7, please change the interpretor to yours in the line 7 of setup_dev_env.sh.

First you need having `virtualenv` installed.

Here's a checklist for you to initialize your project:
- Replace README.md with yours.
- Define dependencies and specify classifiers in setup.py.
- Change the package name to your project's -- that is, you should change the `app` folder to your package name, then change the `package` entry of the setup.py.

After tuning the template to meet your requirements, just run:

```
./setup_dev_env.sh
```

You are all set.

The dev script will create a virtualenv environment in a directory called "venv", and install all mandatory and optional dependencies into it.

To confirm that you're up and running, activate the virtualenv, and run the test suite:
```
. venv/bin/activate # Activate the virtualenv
py.test
```

## Testing
If you've followed the procedure above, you already have all the development requirements installed, and you can simply run the test suite:
```
py.test
```
from setuptools import find_packages,setup
Hypen_e_dot = '-e .'

def getreq(file_path):
    requirements = []
    with open (file_path,'r') as file:
        req = file.readlines()
        for i in req:
            line =  i.strip()
            if line == Hypen_e_dot:
                pass
            else:
                requirements.append(line)

    return requirements


    



setup(
    name='ML projects',
    version='0.0.1',
    author='Deepraj',
    author_email='work.deepraj@gmail.com',
    packages=find_packages(),
    install_requires = getreq('requirements.txt')
)

    
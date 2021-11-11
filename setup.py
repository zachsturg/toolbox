import setuptools

setuptools.setup(
    name='token_gen',
    version='0.0.1',
    author='Zach S',
    author_email='zachsturg@gmail.com',
    description='Testing installation of Package',
    long_description='This is my first package',
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests','hmac','time','base64'],
)

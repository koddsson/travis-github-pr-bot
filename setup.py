from distutils.core import setup
setup(
    name='travis_bot',
    packages=['travis_bot'],  # this must be the same as the name above
    version='0.1.1',
    description='A simple API call to comment message on PR from Travis',
    author='koddsson',
    author_email='koddsson@gmail.com',
    url='https://github.com/koddsson/travis-github-pr-bot',
    download_url='https://github.com/koddsson/travis-github-pr-bot/tarball/0.1.1',
    keywords=['travis', 'bot', 'github'],
    classifiers=[],
    scripts=['travis_bot/travis_bot.py'],
)

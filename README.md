[![Build Status](https://travis-ci.org/koddsson/travis-github-pr-bot.svg?branch=master)](https://travis-ci.org/koddsson/travis-github-pr-bot)

A pretty simple python script that will get output from `stdin` and comment
that output onto the pull request that initilized the build on travis.

Getting up and running.

1. Have travis build enabled github repo.
2. Have a dummy github account and get a token for it.
3. Add the dummy account token to the travis config file under  under `TRAVIS_BOT_GITHUB_TOKEN`.
4. Add the something equivalent following lines to your `.travis.yml` file,
   incidentally the following code will report `flake8` results to the PR.
```yaml
before_install:
  - pip install travis_bot
  - flake8 . | travis_bot
```

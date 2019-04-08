Feature: Installation behavior
  Scenario: Installation from install script
      Given an envvar FIBER_PREFIX=.
      When we run the install script
      Then the directory ./.fiber exists
      Then the directory ./.fiber/env exists
      Then the file ./.fiber/env/bin/.fiber exists
  Scenario: Installation from url
      Given an envvar FIBER_PREFIX=.
      When we run python3 -e "$(curl -fsSL https://raw.githubusercontent.com/ninowalker/dotfiber/master/install)"
      Then the directory ./.fiber exists
      Then the directory ./.fiber/env exists
      Then the file ./.fiber/env/bin/.fiber exists

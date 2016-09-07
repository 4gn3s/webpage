Title: Where did TDD go wrong
Date: 2016-09-06 18:00
Tags: testing, TDD, programming
Category: Programming videos

I have recently watched a very interesting talk given by Ian Cooper about the flaws of TDD. You can watch the whole talk [here](https://vimeo.com/68375232). Below are my notes taken while watching.

## Test behaviours, not implementations

#### A better TDD definition
New piece of **behaviour** means we should write a test

#### What is a unit test?
A unit test shouldn't have any side results; each test should run isolately from other tests. This does not mean that everything should be mocked out! Mocking out too much functionality creates over-implemented tests.

### When refactoring / changing internal implementation, no tests should fail.


## Tips for writing awesome tests:
* Don't jump too early into implementation details
* Only test the public (narrow) interface
* Write tests against use-cases. Pros:
    * less tests
    * testing only core module functionality
* Give tests names which indicate what is being tested
* Focus on making the test pass as quickly as you can. You can try to engineer it later
* Don't mock the internals, privates and adapters
* Mock other public interfaces and other ports
* Use the builder pattern
* Add integration tests to test port-adapter communication

## A recommended development routine:
1. Write a test for new behaviour and make it fail
2. Make the test pass without much engineering or architectual work
3. Refactor and clean the code
    * Do **NOT** write any more tests at this point! (they would be testing the implementation)

### The builder pattern
Using builders in the tests makes tests concise and clean. A builder returns a well build (ready) object; to test some of it's properties, we can override them for particular tests.

#### Software testing reversed ice cream cone
![Ice cream cone]({filename}/images/tests.png)

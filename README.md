#   ENTERSEKT QE Analyst Practical Assessment - OMDB API

The purpose of the assessment is to evaluate that the candidate has the fundamental practical ability and theoretic knowledge to be successful as a Quality Engineering Analyst at Entersekt

## **Practical Exercise**
1. Done
2. Done
3.  To run, `Install the Python Requests library: ***pip install requests***`
	3.1. *See file on repository: [OMDB_GETID.py](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/OMDB_GETID.py)*
	3.2. 	See images under folder [`../sampleImages(INPUT_OUTPUT)/`](https://github.com/sirzuks/OMDBGETBYIDREPO/tree/master/sampleImages%28INPUT_OUTPUT%29) 
4. *See file on repository: [EnterSektOMDBTestCases_Zukile.pdf](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/EnterSektOMDBTestCases_Zukile.pdf)*
5. *See file on repository: [OMDBTESTS.postman_collection.json](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/OMDBTESTS.postman_collection.json)*
	5.1. See images: [TESTS](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/sampleImages%28INPUT_OUTPUT%29/Tests.png), [TestResults](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/sampleImages%28INPUT_OUTPUT%29/TestResults.png), [OMDB Test Runner](https://github.com/sirzuks/OMDBGETBYIDREPO/blob/master/sampleImages%28INPUT_OUTPUT%29/OMDB%20Test%20Runner.png) 
`Note: These are POSTMAN tests. Import the OMDBTESTS.postman_collection.json on PostMan App and you will be able to run tests || Also see images attached for previous runs`

## **Theoretical Exercise**
**1\. Briefly explain the difference between a test case and a user story.**

User Story: 
> User stories are often written on small cards and supposed to be brief statements of desired functionality that can be later fleshed out to obtain functional requirements for developers to code to.

Test scenario: 
> Any functionality that can be tested.

  

**2\. Considering a Continuous Integration environment, when should execution of automated tests occur?**

In a CI environment, automated tests should in theory be run after a build is made available and send feedback with results to developers.

  

**3\. What type of testing is at an API level?**

Functional tests

  

**4\. When is the most effective time to involve a software quality engineer in the SDLC?**

The most effective time to involve a software quality engineer would be as early in the project as possible (requirements phase). Many companies do not involve QA until after design and requirements have been set. Because of this, many issues that could have been identified prior to development are not found until much later in the project and often cause redesigns mid project, sub-optimal quality, or even caveats for a release, all of which cause stress, lower morale and ultimately your user’s experience to suffer.


**5\. For the practical exercise, what percentage of automation vs manual testing would be ideal?**

*For the given task, it makes sense to only cover ~60%. That list includes:*

 - Checking for successful GET request
 - Checking for failed GET request upon omission of a parameter
 - Checking if server Response time is acceptable (less than 500ms)
 - Checking that the response is valid && has a body
 - Checking that the response satisfies objective of test (contains string)

*Other scenarios you would want to check (nice to have's) but need not automate:*

 - When *i* parameter is not valid
 - When *apikey* parameter is not valid
 - When searching for other / multiple ID's (not part of requirement so to automate for *one* search adds no value)

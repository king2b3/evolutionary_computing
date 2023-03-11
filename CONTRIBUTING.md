# Steps to contribute to the repo
*Please* follow our guidelines if you wish to contribute to this repo.
Pull requests NOT following this format will be rejected.

1. **Create an issue detailing the changes you wish to make.** This can be as simple as describing the file(s) you want to add, or the changes you wish to make to file(s).
	1. Descriptions aren't needed in simple issues, but more documentation is always preferred and appreciated.
	2. You may be asked to add more information to your issues by a reviewer(s).
2. **Fork the repo.** In Github fork this repo to your own profile.
3. **Create a new branch on your forked repo named after the issue.** Never make changes directly to the main branch.
	3. For example, if you created issue #8 in the original repo, then name your branch in your fork something along the lines of "issue-08". Commit all of your changes to his new branch in your forked repo.
	4. Make sure to add your name to the AUTHORS.md file so you can get credit for your work!
4. **Submit a pull request for your branch into the main branch.**
	5. This pull request will be reviewed and needs to be accepted by at least one reviewer. 
	6. If you would like to be a reviewer, please contact one of the authors found in the AUTHORS.md file.
	7. The reviewer(s) will close the issue in the main repo upon the merging of your branch.
___
## More detailed steps for contributing 
1. Create an issue describing the changes you wish to make.
	1. Submit this issue fully explaining the changes you wish to make. 
	2. For example, if you wish to add new file(s), the issue could be as simple as "New correct programs for testing". Take note of the issue number, we will use that later.
2. Fork the repo by clicking the fork button in the top right of the github page. 
	1. Select your github profile as the destination for the fork.
3. After this new forked repo has been created, clone the repo onto your machine.
	1. Click the green `Code` drop down menu and select the cloning option of your choice. If your system is set up to allow SSH, we recommend this over https.
4. Create a new branch in your forked repo to apply your changes to.
	1. Name the branch after the issue you are addressing. Lets say you are contributing to solve issue #9 `git checkout -b issue#09`
5. Commit all of your changes to your branch in this forked repo. Please attach the issue in your commit message. The following are valid ways to attach issues to your commit message. `close, closes, closed, fix, fixes, fixed, resolve, resolves, resolved`.
	1. To close multiple issues, you can do `close #01, close #02` as your commit message.
6. Submit a pull request. Do this on github by clicking the `Pull Request` tab and then clicking the `New pull request` button in the top left.
	1. Direct your merge to pull your code from your forked repo into the main branch of the original repo. Don't worry, it won't merge the code automatically, reviewers will confirm the pull request before it is completed. 
	2. Your pull request will be reviewed, and any feedback will be given if changes are needed. Don't worry about closing the issue you created, if you properly attached the issue number to your commit message, github should automatically close the issue for you. If you don't do this, the reviewers will close the issue.
7. If you want to be a reviewer, please contact one of the authors whose info is in the AUTHORS.md file. 
   1. Add your name to the AUTHORS.md file so you can get credit for your work! 
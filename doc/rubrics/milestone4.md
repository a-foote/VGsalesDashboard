# Milestone 4 - Finalizing your dashboard

This week you will make the last modifications to your app
and create a final product ready to use for your target audience!
You can choose if you want to continue working on the Python or R version.
This will include addressing your TAs feedback from previous milestones (1 and 2)
if you haven't done so already,
as well as your peer feedback from the last milestone.
We will also try to give recommendations during the lab
on how you can improve your app.

## 1. Submission instructions
rubric={mechanics:4}

- [Click here to view a description of the rubrics used to grade the questions](https://github.com/UBC-MDS/public/tree/master/rubric).

### Canvas submission

- Once you have finished the work for this milestone
  **you must create a release on GitHub.com before the submission deadline.**
    - Please [read the GitHub documentation on how to create a release via the online interface]( https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/releasing-projects-on-github). Name your release with the respective milestone name.
    - We will grade all files in the repo at the state they were in when you created the release.
      This means that you can continue to make changes in the repo without worrying about messing up your grading for the previous milestone.
- **The only thing you need to submit to Canvas is a link to your Github release**
    - Optionally include a link to an auto-deployed Heroku PR (see section 6).

### Tips for working collaboratively on GitHub

- Every time you work on the project, you should first pull the upstream changes.
- Use GitHub issues to track features that you are planning to implement
  and bugs in the app.
- Try to commit to git often when you work on this project.
    - If you are working together synchronously
      and a team-member has already approved your changes,
      you can commit directly to the main branch.
      Otherwise, create a pull-request and request a review from a teammate.
        - **The TAs will check that you have some issues and PRs in your repo for this milestone**
    - You can either work on different branches directly in the repo you created,
      or fork the repo and work on a branch in your own fork.

## 2. Deployment on Heroku
rubric={accuracy:3}

- Deploy your app on Heroku
  and **include the link to your deployed dashboard clearly visible near the top of your README**.
- Don't push to Heroku after the milestone deadline.
    - We will compare the milestone release commits with the deployed app
      so updating it after the deadline will give a late penalty.
      If you want your newest changes deployed online,
      you can create a new heroku repo.
- This week, you're also going to [setup Heroku's GitHub integration to automate your deploys](https://devcenter.heroku.com/articles/github-integration),
  so that you have a branch in your github repo that is automatically deployed to Heroku.
    - Create a new branch for this on GitHub that you name `deployment`.
- Don't wait to deploy until Saturday night,
  you will not have time to solve potential issues.
    - Deploy early and check that things are working,
      then redeploy every now and then.
    - After making the milestone release,
      make a final push to Heroku to redeploy the miletone app.
- Make sure to take away `debug=True` when you are deploying to Heroku,
  there should not be a blue debug button on the page your target audience will visit!

## 3. Tie it all together and deliver a production ready app
rubric={accuracy:10, quality:5, viz:20}

- You are creating your production-ready dashboard this week!
- This milestone's grading will be more focused on the final stage of your app
  as well as smaller details that we have been softer on previously,
  like a well-styled, and nicely laid out app
  (fully functional is still the most important).
- You should have address all your TAs feedback from M1 and M2 by now.
    - Either with comments addressing why feedback implementation is not needed or PRs implementing the changes.
    - You might not receive the written M3 feedback in time to help improve your app, so please speak to your TA and me during lab about what you can improve etc (in addition to feedback you received previously)
- You should address the feedback you received from your peer group last week the same way as above.
    - **If you didn't receive peer feedback last week, please DM me on slack as soon as possible**.
- If your app is sluggish and has poor performance overall,
  you can try the tips in lecture 7 or subset your data to make it snappier
  and a better experience for those using it.
- Set the title of the browser tab of your app my using the `title` parameter when calling `Dash()`.
    - E.g. `app = dash.Dash(__name__, title='Dashbord name', ...)`
- Again, the app should be easily usable,
  so focus on the most important things first.
- Note that TAs will be grading your app on Heroku in a full-screen window
- Now you are allowed to get hung up of minor styling details, since you will be graded on this in milestone 4 =)
    - However, please note that it does not need to be pixel perfect,
      especially not in a more advanced layout.
    - We will not be zooming in on your app and check the smallest alignment problems,
      but if something is clearly not aligned or there is a lack of overall styling to the app,
      then that's not good.
- Please modify your GitHub repo description in the top right corner where it says "About" to include
    - A short description of your app (might already be there)
    - The link to your deployed dashboard (it is often useful to still keep this in the README as well)
    - A few keywords describing which plots, widgets, and interactions you have used in your dashboards, [like I have done in my demo app](https://github.com/UBC-MDS/dashr-heroku-deployment-demo).
        - If I have time during the break, I will use these to make a resource where you can easily find each others dashboards without searching through the public GitHub repos directly. I think this will be useful to reference back to for capstone and later. You can DM me on slack if your group does not want to be part of this for some reason.

## 4. Reflection
rubric={reasoning:6}

In this section,
your group should document on what you have implemented in your dashboard so far
and explain what is not yet implemented.
It is important that you include what you know is not working in your dashboard,
so that your TAs can distinguish between features in development and bugs.
Since this is the last milestone,
you really need to motivate well
why you have not chosen to include some feature
that you were planning on including previously.

This week it is suitable to include thoughts
on the feedback you received from your peer and/or TA,
e.g.

- Has it been easy to use your app?
- Are there reoccurring themes in your feedback on what is good and what can be improved?
- Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?

This section should be around 300-500 words
and the `reflection-milestone4.md` document should live in your GitHub.com repo
in the `doc` folder.

## 5. Document your functions' functionality (Optional)
rubric={accuracy:1}

You have all already written good docstring for your functions, right???
Well then,
congrats!
Your good habits have been awarded with free points in this lab.
If not,
this is your chance to remedy the situation.
Write proper docstrings for all functions,
including a description of what the function parameters do,
as you have learnt in previous courses.
Clear comments where needed in the code is also a plus.

## 6. Setup app reviews with Heroku (Optional)
rubric={accuracy:1}

Heroku has a neat functionality where you can set it up
to atomically deploy branches when PRs are opened on GitHub.
This way you can test the dashboard live while reviewing a PR
without downloading your collaborator's branch and running it locally.
[Set up your repo accordingly](https://devcenter.heroku.com/articles/github-integration-review-apps)
and create at least one PR that triggers an auto-deployment.
Link this PR in `canvas-submission.html`.

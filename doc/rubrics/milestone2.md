# Milestone 2 - App development and deployment

In this milestone,
you will finish develop a prototype of your app
and deploy it on Heroku so that it is publicly accessible.
This app should be usable even if it does not have the full functionality
outlined in your proposal.
You don't need to implement all the feedback you received from your TA yet,
but it can be a good idea to get started on some of it
since you will need to have a addressed it all in milestone 4
(either implemented it or motivated why not in an issue).

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
rubric={accuracy:8}

- Deploy your app on Heroku
  and **include the link to your deployed dashboard clearly visible near the top of your README**.
- Don't push to Heroku after the milestone deadline.
    - We will compare the milestone release commits with the deployed app
      so updating it after the deadline will give a late penalty.
      If you want your newest changes online,
      you can create a new heroku repo.
- Since your `app.py` will be inside the `src` folder,
  you need to change the `Procfile` to `web: gunicorn src.app:server`
  instead of what it is in [the dash deployment docs](https://dash.plotly.com/deployment).
- I recommend creating `requirements.txt` manually
  and only fix the versions of dash and plotly.
    - Don't forget to include `gunicorn`.
- Don't wait to deploy until Saturday night
  after you have implemented every single feature you want.
  You will not have time to solve potential issues.
    - Deploy early and check that things are working,
      then redeploy every now and then,
      especially after adding new package dependencies.
    - After making the milestone2 release,
      make a final push to Heroku to redeploy the miletone2 app.

### GitHub folder structure

Since we now have a mix of many different file types,
let's tidy things up a bit.
Use a project structure similar to the example below:

```
project/
├── data/            .csv .hdf .pkl .feather
│   ├── processed/
│   └── raw/
├── src/             .py .R
├── reports/         .ipynb .Rmd
├── doc/             .md
├── environment.yaml (or/and requirements.txt)
├── README.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── LICENSE.md
```

The difference between the `reports` and `doc` folders
is that the former contains analytic reports often involving code
(such as notebooks)
whereas the latter is more project documentation.
So where should you put your project proposal and reflections?
I would suggest the `doc` folder,
but remember that these are guidelines and not a strict rule, there are other sensible folder structures too.
You can upload any analysis you do along the way to explore the data in the `reports` folder,
but the analysis itself will not be reviewed by the TAs.

## 3. Interactive Dash app in Python and Altair
rubric={accuracy:10, quality:5, viz:15}

- Implement the dashboard you outlined in your proposal.
- Keep your usage scenario and target audience in mind when designing your interface.
- Aim to implement most of your dashboard's functionality, but not everything.
    - Since the complexity varies between proposals,
      the rough goal here is to have around 3 plots
      and most of their widgets
      and interactivity implemented
    - The app should be clearly usable,
      so focus on the most important things first.
    - In the upcoming milestones you will have time to improve your app
      based on your proposal and the feedback you have received.
    - The TAs will give you feedback on how to adjust the overall complexity
      of your final app for milestone 3 and 4 (if needed). For this milestone,
      use the above directions.
- Your interface should be as self-documenting as possible,
  with appropriate labels for panes and widgets,
  legends documenting the meaning of visual encodings,
  and a meaningful title for the app.
- Note that TAs will be grading your app on Heroku in a full-screen window

It can be easy to get sucked into a rabbit hole when trying to implement a stubborn feature (I know this all too well myself =p).
While it is important to build your troubleshooting skills, it is often even more important to build your time management skills and we do not want one annoying bug to prevent you from completing your app.
Compromises may need to be made - this is a short project.
You can add the bells and whistles at the later milestones and
if you're struggling with a particularly tough problem,
save it for later and ask a TA for help!

## 4. Reflection
rubric={reasoning:6}

In this section, your group should document on what you have implemented in your dashboard so far and explain what is not yet implemented.
It is important that you include what you know is not working in your dashboard, so that your TAs can distinguish between features in development and bugs.

Reflect on what you think your dashboard does well what its limitations are, and what are good future improvements and additions.
This section should not be more than 500 words and the `reflection-milestone2.md` document should live in your GitHub.com repo in the `doc` folder.

## 5. Improve the README (Optional)
rubric={reasoning:2}

Expand on the README file to be a welcoming place for anyone coming
to your project for the first time.
For your project,
your README should cater to at least two groups of people
(on bigger projects these can be separated and put in different files):

1. Those potentially interested in using your dashboard
    - Include motivation behind your project and clearly explain
      what problem you are solving and why it is important.
    - You do not have to include detailed usage instructions,
      just high level what they can do in your dashboard and and the deployed link.
    - [This is a good example](https://github.com/KirstieJane/STEMMRoleModels)
2. Those interesting in helping you develop your dashboard
    - Potential contributors are interested in the above as well,
      but also need to know how they can install your app and how to run it locally
      (maybe they are great in Altair but have never used Dash).
    - Suggestions for what you would like help with and how to work in your project,
      some of this can go in contributing also.
    - [This is an example of a program I made as part of my thesis](https://gitlab.com/stemcellbioengineering/context-explorer/-/blob/master/README.md).

Including a table of contents can be useful,
as well as a short GIF of your dashboard doing something impressive.
No matter how many nice words you put down,
seeing the functionality right when they land on your GH page
is very useful to evoke interest.

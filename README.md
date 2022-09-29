# coffee_roast
Predict roasting temperature and time period for a delicious coffee.
The dataset in this project is formed by a set of trials done by Dr Andrew Ng, as instructed by him in the Deeplearning.ai course.
Read the roast instructions for better understanding of the step by step process of roasting.

Here is the final page link.
[coffee_heroku_app] https://coffee-roast-prediction.herokuapp.com/

# software and tools requirements
1. [GithubAccount] https://github.com/
2. [VSCodeIDE] https://code.visualstudio.com/
3. [HerokuAccount] https://heroku.com/
4. [GitCLI] https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line

# create new environment

```
conda create -n coffee python=3.10 -y
```
# activate environemnt and install dependencies.
once the environment is activated, packages can be installed in the virtual environmentusing pip install.
```
pip install <package_name>
```
# create requirements.txt file
This includes all the necessary packages. Their exact names must be written here.(case sensitive)

# edit gitignore file
Include virtual environment in gitignore to avoid committing the whole env structure to the repository.

# save model
Save the model from the jupyter notebook file into the working directory.
Make sure to include any preprocessing steps within the saved model.

# create app.py file
Create the app using Flask. Define all functions and return prediction from the loaded model.

# create html template
Create the html page and link to the app.py file accordingly.

# create procfile
Procfile is required by heroku to run the app.

# postman test
Use postman and test your outputs using POST request and sending raw data manually in json format.

# commit and push everything
Update repo with all the new files

# heroku setup
Create new app from heroku, link github repository and deploy app.

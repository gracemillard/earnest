# Earnest Takehome

this is a template I use for READMEs<br />
    I included a few templates I use a lot : requirements, setup, gitnore, vscode , logging


## Initialize Environment

```shell
conda create -n takehome python=3.8
conda activate takehome
cd src
pip install -r requirements-dev.txt -i https://pypi.org/simple
pip install -r handlers/requirements.txt -i https://pypi.org/simple

```

## How to run test

```shell
cd src/handlers
python3 -m tests.test
```

## TO DOs

Add check to make sure date format input is valid .... add checks to make sure any given input is valid

Optimize individual apply_ functions 

Write function to get file size and chunk it before passing it in thru the handler

Write function to check for type consistency in the dataframe (make sure stuff like age is all int and purge any charecters if encountered)

add more/better logging and exception handling

## The Ask
-  Complete as many of the following steps as you can. If you can’t complete a step that’s fine,
move on to the next. The steps in bold are stretch goals for extra credit - feel free to skip them if
you don’t have the time. Reorder steps if it makes more sense to you to do so.
The output of the project should be the last step you can accomplish, as well as the code used
throughout the process. Please leave brief comments in the code, and/or add a readme.md if
you prefer.

[1] Load the attached CSV 

[2] Perform as many of the following transformations as you can:
     ◦ Remove all rows where pdays is -1
     ◦ Split name into first name and second name columns (drop name)
     ◦ Replace the values in the age column with bucketed values, such that < 10 becomes 0, 10 <= x < 20 becomes 1, etc.
     ◦ Replace yes/no values with booleans
     ◦ Replace day and month with a single date column, of the form dd/MM
    ◦ Rename the y column “outcome"

[3] Add a column which categorizes geographical features in the address, where present.
    Note the dirtiness of the address data and that the exact categories :
      ▪ “water”, where the address contains e.g. lake, creek
      ▪ “relief”, where the address contains e.g. hill, canyon
      ▪ “flat”, where the address contains e.g. plain

[3] Group by the feature (if you created it, or by some other field if not) and filter out any empty
values, sort by the age bucket (or age if you didn’t do the bucketing), and return a row count.

[4] Write the row level data from step [2], and aggregated data from step[3] to both CSV and
parquet formats.

## The Deployment Plan
...tbd...


## Consideraions

-- How often will this be used  <br />
-- What needs to be modifiable? <br/>






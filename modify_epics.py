#!/bin/env python3
# This will change epics in ALL of your drafts. Might be risky a bit.
# Before you start: pip install jira

from jira import JIRA
from jira.client import ResultList
from typing import cast
from jira.resources import Issue

# Vars for authentification
user = 'user@email'
apikey = 'jira_api_token'
server = 'https://example.atlassian.net'
options = { 'server': server }

# Variables for issues to change
assignee = 'Name Surname'
project = 'Jira_project_name'
old_epic = 'Old_epic'
new_epic = 'New_epic'
 
# Authentification
jira = JIRA(options, basic_auth=(user,apikey) )

# Get all drafts for the user from the project
issues = cast(ResultList[Issue], jira.search_issues([f'assignee="{assignee}"', f'project={project}', f'status={status}'], maxResults=100))
 
for x in issues:
    issue = jira.issue(x)
    epic = str(issue.fields.customfield_10005)
    summary = str(issue.fields.summary)
    status = str(issue.fields.status)
    # Change epics
    if (status == "Draft") and (epic == old_epic):
        print(x)
        print(summary)
        print("Going to change epic")
        issue.update(customfield_10005=new_epic)



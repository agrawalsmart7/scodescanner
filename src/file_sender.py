import requests
import json
import sys
from jira import JIRA  
from utils import logs_handler

logger = logs_handler.create_logger(__name__, remote_logging=False)

def jira_token_retriever():
    with open("config.json", 'r') as configfile:
        configdata = json.load(configfile)
        configdata['jira'] == 'jira'
        for lists in configdata['jira']:
            if lists['jira_username'] == "" and lists['jira_api'] == "" and lists['project_id'] == "" and lists['serverurl']:
                logger.error("Please provide the valid Username and API and Project ID and ServerUrl")
                sys.exit()
            else:
                return (lists['jira_username'], lists['jira_api'], lists['project_id'], lists['serverurl'])

def jira_issue_creater(filename):
    jira_username, jira_api, project_id, serverurl = jira_token_retriever()
  
    options = {'server': serverurl}
    # Server Authentication

    jira = JIRA(options, basic_auth=(str(jira_username), str(jira_api)))

    new_issue = jira.create_issue(project=project_id, summary='New issue from SCodeScanner', description='Look into this one', issuetype={'name': 'Bug'})

    # Upload the file
    jira.add_attachment(issue=new_issue, attachment=filename)
    if jira:
        logger.info("File Successfully Sent to JIRA")


def slack_token_retriever(send_to_app):
    
    with open("config.json", 'r') as configfile:
        configdata = json.load(configfile)
        configdata['slack'] == 'slack'
        for lists in configdata['slack']:
            if lists['bot_token'] == "" and lists['channel_name'] == "":
                logger.error("Please provide the valid Bot_Token and Channel Name")
            else:
                return (lists['bot_token'], lists['channel_name'])

def slack_issue_creator(filename):
    token, channelname = slack_token_retriever("slack")
    with open(filename, 'r') as e:
        filedata = e.read()
    url = "https://slack.com/api/files.upload"

    data = {
        "token": token,
        "title": "ALERT - Findings from SCodeScanner",
        "messages": "SCodeScanner Found some security vulnerabilities inside the code, Please check and patch accordingly",
        "channels": channelname,
        "content": filedata,
        "filename": filename,
        "filetype": "text",
    }
    response = requests.post( url=url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    if response.status_code == 200:
        print('\n\n', logger.info("File Successfully Sent to Slack"))



import requests
import json
import pandas as pd
import datetime as dt
from datetime import datetime

headers = {
    "Accept": "application/json"
}

def ws_get_issues(config):
    # Get issue list for the given project.

    params = {}
    params['key'] = config['api_key']
    params['project_id'] = config['project_id']
    params['offset'] = config['offset']
    params['limit'] = config['maxResults']
    # if only using closed ticket, Specify 'closed' instead of '*'.
    params['status_id'] = '*'
    
    if 'from_date' in config and not 'to_date' in config:
        params['updated_on'] = '>=' + config['from_date']
    if not 'from_date' in config and 'to_date' in config:
        params['updated_on'] = '<=' + config['to_date']
    if 'from_date' in config and 'to_date' in config:
        params['updated_on'] = '><' + config['from_date'] +'|' + config['to_date']

    url = config['url']+'issues.json'
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=params)
    if response.status_code == 200:
        return json.loads(response.text)
    else: 
        print("error get ticket %s " % response.status_code)
        return None
    
def ws_get_projects(config):
    # Get project list.

    params = {}
    params['key'] = config['api_key']

    url = config['url']+'projects.json'
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=params)
    if response.status_code == 200:
        return json.loads(response.text)
    else: 
        print("error get project %s " % response.status_code)
        return {'issues':[]}
    
def ws_get_issue(config, issue_id):
    # Get one issue data including journals.

    params = {}
    params['key'] = config['api_key']
    params['include'] = 'journals'

    url = config['url']+'issues/'+str(issue_id)+'.json'
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=params)
    if response.status_code == 200:
        return json.loads(response.text)
    else: 
        print("error get ticket %s " % response.status_code)
        return None
    
def create_event_from_issue(issue):

    event = { }
    event['event_id'] = issue['id']
    event['tracker_id'] = issue['tracker']['id']
    event['tracker_name'] = issue['tracker']['name']
    event['status_id'] = '1'
    event['status_closed'] = issue['status']['is_closed']
    event['priority_id'] = issue['priority']['id']
    event['priority_name'] = issue['priority']['name']
    event['author_id'] = issue['author']['id']
    event['author_name'] = issue['author']['name']
    event['subject'] = issue['subject']
    event['description'] = issue['description']
    event['start_datetime'] = issue['created_on']
    event['due_date'] = issue['due_date']
    # TODO other columns exist.

    if 'assigned_to' in issue: 
        event['assigned_to_id'] = issue['assigned_to']['id']
        event['assigned_to_name'] = issue['assigned_to']['name']
    else:
        event['assigned_to_id'] = None
        event['assigned_to_name'] = None

    return event

def create_event_from_journal(issue, journal, detail):
    event = create_event_from_issue(issue)
    event['status_id'] = detail['new_value']
    event['start_datetime'] = journal['created_on']

    return event

# Useful function to only see the issue fields that are not None
def explore_issue_fields(issue):
    fields = issue['fields']
    print("Issue: %s" % issue['key'])
    for field in fields:
        if fields[field]:
            print("%s : %s" %(field, fields[field]))

def XformToIso(d):
    if d == '':
        return ''
    else:
        aDate = datetime.strptime(d,'%Y-%m-%dT%H:%M:%S%z')
    return  aDate.isoformat(sep = 'T', timespec = 'seconds')

# When loaded into Process Mining, the import works.
# To run/debug this program as a standalone code, we redefine the ProcessAppException class below
try:
    STANDALONE = 0
    from process_app import ProcessAppException
except: 
    class ProcessAppException(Exception):
        def __init__(self, message):
            self.message=message
            super().__init__(self.message)
        def getMessage(self):
            return self.message

def execute(context):
    my_config = context['config']

    # if any, check the minimal number of issue per project, unless we discard the project. Default is 0
    if 'minimalIssueNumber' not in my_config:
        my_config['minimalIssueNumber'] =  0
    if 'maxResults' not in my_config:
        my_config['maxResults'] =  100
    if 'startAt' not in my_config:
        my_config['startAt'] =  0

    # config['projects'] can be empty, or contain a list of projects separated by a comma
    # get the list of projects
    if 'projects' not in my_config:
        projects = ''
    else:
        projects = my_config['projects']
    if projects == '':
        # get all the projects
        projects = ws_get_projects(my_config)['projects']
        print("Redmine Projects : %s projects retrieved" % len(projects))
    else:
        my_config['projects'] = my_config['projects'].replace(' ','')
        project_keys = my_config['projects'].split(',')
        projects = []
        for project in project_keys:
            projects.append({'id': project})

    # from_date and to_date field to limit the scope whenever needed
    # check that the input dates have the expected date format
    date_format = '%Y-%m-%d'
    if 'from_date'in my_config:
        try:
        # formatting the date using strptime() function to raise an error if date format problem
            dt.datetime.strptime(my_config['from_date'], date_format)
        # If the date validation goes wrong
        except Exception as e:   # printing the appropriate text if ValueError occurs
            raise ProcessAppException("Incorrect from date format, should be like this 2022-10-08" + str(e))
    if 'to_date' in my_config:
        try:
        # formatting the date using strptime() function to raise an error if date format problem
            dt.datetime.strptime(my_config['to_date'], date_format)
        # If the date validation goes wrong
        except Exception as e:   # printing the appropriate text if ValueError occurs
            raise ProcessAppException("Incorrect to date format, should be like this 2022-10-08" + str(e))

    events = []

    # get the list of issues for each project. 
    for project in projects:
        my_config['project_id']=project['id']
        # We are paging to retrieve the issues
        page = 0
        retrieved_count = 0
        total_count = 1
        while retrieved_count < total_count:
            my_config['offset'] = page * my_config['maxResults']
            page += 1
            result = ws_get_issues(my_config)
            total_count = result['total_count']
            if total_count < my_config['minimalIssueNumber']:
                # discard projects with less than minimum issues (should that be a parameter?)
                print('Project key = %s , name = %s : contains %s issues <*** DISCARDED ***>' % (project['id'], project['name'], total_count) )
                break;
            issues = result['issues']
            retrieved_count += len(issues)

            print('Project %s: Retrieved %s issues' % (my_config['project_id'],retrieved_count))

            for issue in issues:
                # Create event from initial post.
                event = create_event_from_issue(issue)
                events.append(event)

                issue_w_journal = ws_get_issue(my_config, issue['id'])

                for journal in issue_w_journal['issue']['journals']:
                    for detail in journal['details']:
                        if detail['name'] == 'status_id':
                            event = create_event_from_journal(issue, journal, detail)
                            events.append(event)

    print("Total of %s events created from %s projects" % (len(events), len(projects)))
    eventlog_df = pd.DataFrame(events,dtype=str)

    # Format for final output

    # Change the date format such that it is automatically understood in Process Mining
    eventlog_df['start_datetime'] = eventlog_df['start_datetime'].apply(XformToIso)
    # Replace NaN by blank ''
    eventlog_df.fillna('', inplace=True)
    # force the type to strings
    eventlog_df.astype(str)

    # duedate is just a date, no need to transform, although it is not recognized by process mining 2022-01-01
    return  eventlog_df


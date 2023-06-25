import redmine
import json

if __name__ == "__main__":

    # Create a json file 'my_config.json' that includes your configuration
    try: 
        f = open('my_config.json')
        my_config = json.load(f)
    except Exception as e:
        # For testing, you can use this json configuration
        print("*** WARNING: %s. Create one, or update my_config object in the code" % e)
        my_config = {
            "url":"<REDMINE API URL>", # Works with https://<REDMINE>/
            "api_key":"<REDMINE API KEY>",
            "maxResults":100, # Paging size. Max = 100
            "startAt":0, # Paging offset
            "projects":"", # list of project keys separated by comma, or empty for all projects
            "minimalIssueNumber":0,
#            "from_date":"2023-01-01", # not set or YYYY-MM-DD as from udpate date
#            "to_date":"2023-12-31" # not set or YYYY-MM-DD as to update date
            }
    # STANDALONE variable used to print and generate CSV files (1 or 0)
    STANDALONE = 1
    context = {'config': my_config}
    eventlog_df = redmine.execute(context)
    print("End of local execution")
    if STANDALONE:
        print("Number of events in eventlog : %s" % len(eventlog_df))
        print(eventlog_df)
        eventlog_df.to_csv('redmineevents.csv', index=None)

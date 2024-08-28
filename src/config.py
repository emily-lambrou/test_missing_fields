import os

repository_owner = os.environ['GITHUB_REPOSITORY_OWNER']
repository_owner_type = os.environ['INPUT_REPOSITORY_OWNER_TYPE']
repository = os.environ['GITHUB_REPOSITORY']
repository_name = repository.split('/')[1]
server_url = os.environ['GITHUB_SERVER_URL']
is_enterprise = True if os.environ.get('INPUT_ENTERPRISE_GITHUB') == 'True' else False
dry_run = True if os.environ.get('INPUT_DRY_RUN') == 'True' else False

gh_token = os.environ['INPUT_GH_TOKEN']
project_number = int(os.environ['INPUT_PROJECT_NUMBER'])
api_endpoint = os.environ.get('GITHUB_GRAPHQL_URL', 'https://github.intranet.unicaf.org/api/graphql')

# Field names
status_field_name = os.environ['INPUT_STATUS_FIELD_NAME']
duedate_field_name = os.environ['INPUT_DUEDATE_FIELD_NAME']
timespent_field_name = os.environ['INPUT_TIMESPENT_FIELD_NAME']
release_field_name = os.environ['INPUT_RELEASE_FIELD_NAME']
estimate_field_name = os.environ['INPUT_ESTIMATE_FIELD_NAME']
priority_field_name = os.environ['INPUT_PRIORITY_FIELD_NAME']
size_field_name = os.environ['INPUT_SIZE_FIELD_NAME']
week_field_name = os.environ['INPUT_WEEK_FIELD_NAME']

notification_type = os.environ['INPUT_NOTIFICATION_TYPE']

if notification_type not in ['comment', 'email']:
    raise Exception(f'Unsupported notification type {notification_type}')

GRAPHQL_ENDPOINT = api_endpoint
GRAPHQL_HEADERS = {
    'Authorization': f'Bearer {gh_token}',
    'Content-Type': 'application/json'
}


# Define the required fields and their types
required_fields = {
    status_field_name: 'single_select',
    duedate_field_name: 'date',
    timespent_field_name: 'text',
    release_field_name: 'single_select',
    estimate_field_name: 'text',
    priority_field_name: 'single_select',
    size_field_name: 'single_select',
    week_field_name: 'iteration'
}

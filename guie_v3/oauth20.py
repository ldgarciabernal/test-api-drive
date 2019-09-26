import google.oauth2.credentials
import google_auth_oauthlib.flow
import flask
from googleapiclient.discovery import build
from flask import request, Flask

app = Flask(__name__)

def authorizated():
    # Use the credentials_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'credentials/credentials_secret.json',
        scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required. The value must exactly
    # match one of the authorized redirect URIs for the OAuth 2.0 client, which you
    # configured in the API Console. If this value doesn't match an authorized URI,
    # you will get a 'redirect_uri_mismatch' error.
    flow.redirect_uri = 'http://localhost:8080'

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    return flask.redirect(authorization_url)

def generate_report(year):
    format = request.args.get('format')

    state = flask.session['state']    
        
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'credentials/credentials_secret.json',
        scopes=['https://www.googleapis.com/auth/youtube.force-ssl'],
        state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    """
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}
    """
    drive = build('drive', 'v3', credentials=credentials)
    files = drive.files().list().execute()

    for file in files:
        print("File id: %s", file.get('id'))

def response():
    with app.test_request_context(
            '/make_report/2017', data={'format': 'short'}):
        generate_report('2019')   

    




